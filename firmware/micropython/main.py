from machine import Pin, I2C
import time

# ============================================================
# Pico 74xx IC Tester Rev A
# Hardware:
# - ZIF_1..ZIF_20 on Pico GPIO0..GPIO19
# - MCP23017 at I2C 0x20
# - OLED optional SSD1306 at 0x3C
# - I2C SDA GPIO20, SCL GPIO21
# ============================================================

I2C_SDA = 20
I2C_SCL = 21
MCP_ADDR = 0x20
OLED_ADDR = 0x3C

# ZIF pin to Pico GPIO mapping
ZIF_TO_GPIO = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7,
    9: 8,
    10: 9,
    11: 10,
    12: 11,
    13: 12,
    14: 13,
    15: 14,
    16: 15,
    17: 16,
    18: 17,
    19: 18,
    20: 19,
}

# Top-aligned chip insertion maps
MAP_14 = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
    8: 14, 9: 15, 10: 16, 11: 17, 12: 18, 13: 19, 14: 20,
}

MAP_16 = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
    9: 13, 10: 14, 11: 15, 12: 16, 13: 17, 14: 18, 15: 19, 16: 20,
}

MAP_20 = {i: i for i in range(1, 21)}

current_map = MAP_14
zif_pins = {}

# MCP23017 registers, BANK=0
IODIRA = 0x00
IODIRB = 0x01
GPPUA  = 0x0C
GPPUB  = 0x0D
GPIOA  = 0x12
GPIOB  = 0x13
OLATB  = 0x15

# MCP GPA inputs
BTN_NEXT = 0
BTN_TEST = 1
PKG14    = 2
PKG16    = 3
PKG20    = 4
V_3V3    = 5
V_5V     = 6

# MCP GPB outputs
RGB_R  = 0
RGB_G  = 1
RGB_B  = 2
BUZZER = 3

i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)

# ============================================================
# Minimal SSD1306 OLED driver
# ============================================================

class SSD1306:
    def __init__(self, i2c, addr=0x3C):
        self.i2c = i2c
        self.addr = addr
        self.w = 128
        self.h = 64
        self.buf = bytearray(self.w * self.h // 8)
        self.ok = False
        try:
            for cmd in [
                0xAE, 0x20, 0x00, 0x40, 0xA1, 0xC8, 0x81, 0x7F,
                0xA4, 0xA6, 0xA8, 0x3F, 0xD3, 0x00, 0xD5, 0x80,
                0xD9, 0xF1, 0xDA, 0x12, 0xDB, 0x40, 0x8D, 0x14, 0xAF
            ]:
                self.cmd(cmd)
            self.ok = True
        except Exception:
            self.ok = False

    def cmd(self, c):
        self.i2c.writeto(self.addr, bytes([0x80, c]))

    def clear(self):
        for i in range(len(self.buf)):
            self.buf[i] = 0

    def show(self):
        if not self.ok:
            return
        self.cmd(0x21)
        self.cmd(0)
        self.cmd(127)
        self.cmd(0x22)
        self.cmd(0)
        self.cmd(7)
        self.i2c.writeto(self.addr, bytes([0x40]) + self.buf)

    def pixel(self, x, y, c=1):
        if 0 <= x < self.w and 0 <= y < self.h:
            idx = x + (y // 8) * self.w
            if c:
                self.buf[idx] |= 1 << (y & 7)
            else:
                self.buf[idx] &= ~(1 << (y & 7))

    def text(self, s, x, y):
        # very small placeholder text output to terminal only
        # OLED driver initialized; install full font later if wanted
        pass

oled = None

# ============================================================
# MCP23017 functions
# ============================================================

def mcp_write(reg, val):
    i2c.writeto_mem(MCP_ADDR, reg, bytes([val & 0xFF]))

def mcp_read(reg):
    return i2c.readfrom_mem(MCP_ADDR, reg, 1)[0]

def mcp_init():
    # GPA all inputs
    mcp_write(IODIRA, 0xFF)

    # GPB0..3 outputs, GPB4..7 inputs/spare
    mcp_write(IODIRB, 0xF0)

    # Pullups on all GPA inputs
    mcp_write(GPPUA, 0xFF)

    # GPB pullups off
    mcp_write(GPPUB, 0x00)

    # outputs off
    mcp_write(OLATB, 0x00)

def mcp_input_low(bit):
    return (mcp_read(GPIOA) & (1 << bit)) == 0

def mcp_set_outputs(mask):
    mcp_write(OLATB, mask & 0xFF)

def rgb(r, g, b):
    mask = 0
    if r:
        mask |= 1 << RGB_R
    if g:
        mask |= 1 << RGB_G
    if b:
        mask |= 1 << RGB_B
    mcp_set_outputs(mask)

def buzzer(on):
    cur = mcp_read(GPIOB)
    if on:
        cur |= 1 << BUZZER
    else:
        cur &= ~(1 << BUZZER)
    mcp_write(OLATB, cur)

def beep(ms=80):
    buzzer(True)
    time.sleep_ms(ms)
    buzzer(False)

# ============================================================
# Hardware status
# ============================================================

def detect_package():
    if mcp_input_low(PKG14):
        rgb(1, 0, 0)
        return 14, MAP_14
    if mcp_input_low(PKG16):
        rgb(0, 1, 0)
        return 16, MAP_16
    if mcp_input_low(PKG20):
        rgb(0, 0, 1)
        return 20, MAP_20
    rgb(0, 0, 0)
    return None, None

def detect_voltage():
    if mcp_input_low(V_3V3):
        return "3.3V"
    if mcp_input_low(V_5V):
        return "5V"
    return "OFF"

def wait_button(bit):
    while not mcp_input_low(bit):
        time.sleep_ms(20)
    time.sleep_ms(40)
    while mcp_input_low(bit):
        time.sleep_ms(20)
    time.sleep_ms(40)

# ============================================================
# ZIF GPIO safety and access
# ============================================================

def all_zif_inputs():
    global zif_pins
    zif_pins = {}
    for zif, gpio in ZIF_TO_GPIO.items():
        zif_pins[zif] = Pin(gpio, Pin.IN, Pin.PULL_DOWN)

def dut_to_zif(dut_pin):
    return current_map[dut_pin]

def set_output(dut_pin, val):
    zif = dut_to_zif(dut_pin)
    gpio = ZIF_TO_GPIO[zif]
    zif_pins[zif] = Pin(gpio, Pin.OUT)
    zif_pins[zif].value(1 if val else 0)

def set_input(dut_pin):
    zif = dut_to_zif(dut_pin)
    gpio = ZIF_TO_GPIO[zif]
    zif_pins[zif] = Pin(gpio, Pin.IN, Pin.PULL_DOWN)

def read_pin(dut_pin):
    zif = dut_to_zif(dut_pin)
    return zif_pins[zif].value()

# ============================================================
# Test helpers
# ============================================================

def test_gate_2in(name, a_pin, b_pin, y_pin, func):
    ok = True
    set_input(y_pin)

    for a, b in [(0,0), (0,1), (1,0), (1,1)]:
        set_output(a_pin, a)
        set_output(b_pin, b)
        time.sleep_ms(2)

        expected = func(a, b)
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} B={} expected={} got={}".format(
                name, a, b, expected, got
            ))
            ok = False

    if ok:
        print("{} PASS".format(name))
    return ok

def test_inverter(name, a_pin, y_pin):
    ok = True
    set_input(y_pin)

    for a in [0, 1]:
        set_output(a_pin, a)
        time.sleep_ms(2)

        expected = 0 if a else 1
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} expected={} got={}".format(
                name, a, expected, got
            ))
            ok = False

    if ok:
        print("{} PASS".format(name))
    return ok

# ============================================================
# Chip tests
# ============================================================

def test_7400():
    print("Testing 7400 NAND")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 0 if a and b else 1),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 0 if a and b else 1),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 0 if a and b else 1),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 0 if a and b else 1),
    ])

def test_7402():
    print("Testing 7402 NOR")
    return all([
        test_gate_2in("Gate1", 2, 3, 1, lambda a,b: 0 if a or b else 1),
        test_gate_2in("Gate2", 5, 6, 4, lambda a,b: 0 if a or b else 1),
        test_gate_2in("Gate3", 8, 9, 10, lambda a,b: 0 if a or b else 1),
        test_gate_2in("Gate4", 11, 12, 13, lambda a,b: 0 if a or b else 1),
    ])

def test_7404():
    print("Testing 7404 inverter")
    return all([
        test_inverter("Inv1", 1, 2),
        test_inverter("Inv2", 3, 4),
        test_inverter("Inv3", 5, 6),
        test_inverter("Inv4", 9, 8),
        test_inverter("Inv5", 11, 10),
        test_inverter("Inv6", 13, 12),
    ])

def test_7408():
    print("Testing 7408 AND")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 1 if a and b else 0),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 1 if a and b else 0),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 1 if a and b else 0),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 1 if a and b else 0),
    ])

def test_7432():
    print("Testing 7432 OR")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 1 if a or b else 0),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 1 if a or b else 0),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 1 if a or b else 0),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 1 if a or b else 0),
    ])

def test_7486():
    print("Testing 7486 XOR")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 1 if a != b else 0),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 1 if a != b else 0),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 1 if a != b else 0),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 1 if a != b else 0),
    ])

CHIPS = [
    {"name": "7400 NAND", "pins": 14, "test": test_7400},
    {"name": "7402 NOR",  "pins": 14, "test": test_7402},
    {"name": "7404 INV",  "pins": 14, "test": test_7404},
    {"name": "7408 AND",  "pins": 14, "test": test_7408},
    {"name": "7432 OR",   "pins": 14, "test": test_7432},
    {"name": "7486 XOR",  "pins": 14, "test": test_7486},
]

# ============================================================
# UI
# ============================================================

selected = 0

def show_status():
    pkg, _ = detect_package()
    volt = detect_voltage()
    chip = CHIPS[selected]

    print("\n==============================")
    print("Pico 74xx Tester")
    print("Package:", pkg if pkg else "NONE")
    print("Voltage:", volt)
    print("IC:", chip["name"])
    print("NEXT = select, TEST = run")
    print("==============================")

def pass_feedback():
    for _ in range(2):
        rgb(0, 1, 0)
        beep(70)
        time.sleep_ms(120)
        rgb(0, 0, 0)
        time.sleep_ms(120)

def fail_feedback():
    rgb(1, 0, 0)
    beep(400)
    time.sleep_ms(250)
    rgb(0, 0, 0)

def running_feedback():
    rgb(1, 1, 1)
    time.sleep_ms(120)

# ============================================================
# Main
# ============================================================

print("Booting Pico 74xx Tester...")

all_zif_inputs()

try:
    mcp_init()
    print("MCP23017 OK")
except Exception as e:
    print("MCP23017 ERROR:", e)
    while True:
        time.sleep(1)

try:
    oled = SSD1306(i2c, OLED_ADDR)
    if oled.ok:
        print("OLED detected")
    else:
        print("OLED not detected")
except Exception:
    print("OLED not detected")

beep(80)

while True:
    all_zif_inputs()
    show_status()

    # blink RGB if voltage is OFF
    if detect_voltage() == "OFF":
        rgb(1, 1, 0)
        time.sleep_ms(150)
        rgb(0, 0, 0)

    if mcp_input_low(BTN_NEXT):
        wait_button(BTN_NEXT)
        selected = (selected + 1) % len(CHIPS)
        beep(40)
        continue

    if mcp_input_low(BTN_TEST):
        wait_button(BTN_TEST)

        pkg, pkg_map = detect_package()
        volt = detect_voltage()
        chip = CHIPS[selected]

        if pkg is None:
            print("ERROR: No package selected")
            fail_feedback()
            continue

        if volt == "OFF":
            print("ERROR: Voltage is OFF")
            fail_feedback()
            continue

        if pkg != chip["pins"]:
            print("ERROR: Wrong package selected")
            print("Chip needs {}-pin mode".format(chip["pins"]))
            fail_feedback()
            continue

        current_map = pkg_map

        print("Running test:", chip["name"])
        running_feedback()
        all_zif_inputs()

        result = chip["test"]()

        all_zif_inputs()

        if result:
            print("RESULT: PASS")
            pass_feedback()
        else:
            print("RESULT: FAIL")
            fail_feedback()

    time.sleep_ms(80)