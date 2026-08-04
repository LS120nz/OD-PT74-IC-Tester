# ============================================================
# OD-PT74
# Pico 74xx Logic IC Tester
#
# Hardware : Rev-C
# Firmware : v1.0.0
#
# Author    : Otter Designs
#
# Release : Public v1.0.0
#
# Description:
# The OD-PT74 is a Raspberry Pi Pico based logic IC tester for
# the 74xx family of TTL logic devices.
#
# The firmware controls the GPIO test interface, MCP23017 I/O
# expander, SSD1306 OLED display and user interface to perform
# functional testing of supported ICs.
# ============================================================
# ============================================================
# File Structure
#
#   Imports
#   Product Information
#   Hardware Configuration
#   User Interface Pins
#   ZIF Pin Mapping
#   Package Pin Maps
#   MCP23017 Definitions
#   OLED Functions
#   MCP23017 Functions
#   Hardware Helper Functions
#   GPIO/ZIF Functions
#   Generic Test Helpers
#   Individual IC Test Functions
#   Chip Database
#   Statistics Functions
#   Menu Functions
#   Main Program
# ============================================================
from machine import Pin, SoftI2C
import time
try:
    import ujson as json
except:
    import json
  
# ------------------------------------------------------------
# Product Information
# ------------------------------------------------------------

PRODUCT_NAME = "OD-PT74"
PRODUCT_DESCRIPTION = "Pico 74xx Logic IC Tester"

HARDWARE_REV = "Rev-C"
FIRMWARE_VERSION = "v1.0.0"
COPYRIGHT = "© 2026 Otter Designs"
AUTHOR = "Otter Designs"

# ------------------------------------------------------------
# Hardware Configuration
# ------------------------------------------------------------

I2C_SDA = 26
I2C_SCL = 27
MCP_ADDR = 0x20

# ------------------------------------------------------------
# User Interface Pins
# ------------------------------------------------------------

enc_a = Pin(20, Pin.IN, Pin.PULL_UP)
enc_b = Pin(21, Pin.IN, Pin.PULL_UP)
enc_sw = Pin(22, Pin.IN, Pin.PULL_UP)
last_enc_a = enc_a.value()

# ------------------------------------------------------------
# ZIF Pin Mapping
# ------------------------------------------------------------

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

MAP_8 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 17,
    6: 18,
    7: 19,
    8: 20,
}

MAP_14 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 14,
    9: 15,
    10: 16,
    11: 17,
    12: 18,
    13: 19,
    14: 20,
}

MAP_16 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 13,
    10: 14,
    11: 15,
    12: 16,
    13: 17,
    14: 18,
    15: 19,
    16: 20,
}

MAP_20 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    16: 16,
    17: 17,
    18: 18,
    19: 19,
    20: 20,
}

# ------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------

current_map = MAP_14
zif_pins = {}

# ------------------------------------------------------------
# MCP23017 Register Definitions
# ------------------------------------------------------------

IODIRA = 0x00
IODIRB = 0x01
GPPUA  = 0x0C
GPPUB  = 0x0D
GPIOA  = 0x12
GPIOB  = 0x13
OLATB  = 0x15

# ------------------------------------------------------------
# MCP23017 GPIO Assignments
# ------------------------------------------------------------
# MCP GPA inputs
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

i2c = SoftI2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=100000)

try:
    import ssd1306
    OLED_AVAILABLE = True
except:
    OLED_AVAILABLE = False
    
oled = None

# ------------------------------------------------------------
# OLED Initialisation
# ------------------------------------------------------------

def oled_init():
    global oled

    if not OLED_AVAILABLE:
        print("OLED driver not found")
        return

    try:
        oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
        oled.fill(0)
        oled.text(PRODUCT_NAME, 0, 0)
        oled.text("Firmware", 0, 16)
        oled.text(FIRMWARE_VERSION, 0, 32)
        oled.show()
        print("OLED OK")
    except Exception as e:
        oled = None
        print("OLED ERROR:", e)

# ------------------------------------------------------------
# OLED Utility Functions
# ------------------------------------------------------------

def oled_clear():
    if oled:
        oled.fill(0)

def oled_show():
    if oled:
        oled.show()

def oled_text(txt, x, y):
    if oled:
        oled.text(str(txt), x, y)

# ------------------------------------------------------------
# OLED User Interface Screens
# ------------------------------------------------------------

def oled_main(chip, family, mode, pkg, volt, field):
    if not oled:
        return

    oled.fill(0)

    # OLED is intentionally kept simple.
    # Detailed information stays on the terminal.
    prefix_ic = ">" if field == 0 else " "
    prefix_fam = ">" if field == 1 else " "
    prefix_mode = ">" if field == 2 else " "

    oled.text(prefix_ic + chip["name"][:15], 0, 0)
    oled.text(prefix_fam + "Fam: " + family, 0, 16)
    oled.text(prefix_mode + mode, 0, 28)

    status = "{}pin  {}".format(pkg if pkg else "--", volt)
    oled.text(status[:16], 0, 44)
    oled.text("READY", 0, 56)

    oled.show()
    
def oled_info(chip):
    if not oled:
        return

    oled.fill(0)

    oled.text(chip["name"][:16], 0, 0)
    oled.text("Pins: {}".format(chip["pins"]), 0, 16)

    oled.text("Family:", 0, 32)
    oled.text(families[selected_family], 64, 32)

    oled.text("TEST=Exit", 0, 56)

    oled.show()
    
def oled_running(chip, mode):
    if not oled:
        return

    oled.fill(0)
    oled.text(chip["name"][:16], 0, 0)
    oled.text("Running...", 0, 24)
    oled.text(mode, 0, 40)
    oled.show()


def oled_result(chip, result):
    if not oled:
        return

    oled.fill(0)
    oled.text(chip["name"][:16], 0, 0)

    if result:
        oled.text("PASS", 44, 14)
    else:
        oled.text("FAIL", 44, 14)

    oled.text("S P{} F{}".format(session_pass, session_fail), 0, 32)
    oled.text("L P{} F{}".format(
        stats["lifetime_pass"],
        stats["lifetime_fail"]
    ), 0, 44)

    oled.text("TEST=Menu", 0, 56)
    oled.show()

def oled_soak(chip, passes, target):
    if not oled:
        return

    oled.fill(0)
    oled.text(chip["name"][:16], 0, 0)
    oled.text("SOAK", 0, 20)

    if target is None:
        oled.text("{} / INF".format(passes), 0, 40)
    else:
        oled.text("{} / {}".format(passes, target), 0, 40)

    oled.show()

def oled_error(msg):
    if not oled:
        return

    oled.fill(0)
    oled.text("ERROR", 44, 0)
    oled.text(str(msg)[:16], 0, 24)
    oled.text("See terminal", 0, 48)
    oled.show()

# ------------------------------------------------------------
# MCP23017 Functions
# ------------------------------------------------------------

def mcp_write(reg, val):
    i2c.writeto_mem(MCP_ADDR, reg, bytes([val & 0xFF]))

def mcp_read(reg):
    return i2c.readfrom_mem(MCP_ADDR, reg, 1)[0]

def mcp_init():
    mcp_write(IODIRA, 0xFF)  # GPA inputs
    mcp_write(IODIRB, 0xF0)  # GPB0..3 outputs
    mcp_write(GPPUA, 0xFF)   # GPA pullups
    mcp_write(GPPUB, 0x00)
    mcp_write(OLATB, 0x00)

print("I2C scan:", [hex(x) for x in i2c.scan()])

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

# ------------------------------------------------------------
# Hardware Detection
# ------------------------------------------------------------

def detect_package():
    val = mcp_read(GPIOA)

    if (val & 0x04) == 0:
        rgb(1, 0, 0)
        return 14, MAP_14

    if (val & 0x08) == 0:
        rgb(0, 1, 0)
        return 16, MAP_16

    if (val & 0x10) == 0:
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

# ------------------------------------------------------------
# ZIF GPIO Functions
# ------------------------------------------------------------

def all_zif_inputs():
    global zif_pins
    zif_pins = {}

    for zif, gpio in ZIF_TO_GPIO.items():
        zif_pins[zif] = Pin(gpio, Pin.IN)

    time.sleep_ms(2)

def dut_to_zif(dut_pin):
    return current_map[dut_pin]

def set_output(dut_pin, val):
    zif = dut_to_zif(dut_pin)
    gpio = ZIF_TO_GPIO[zif]

    p = Pin(gpio, Pin.OUT)
    p.value(1 if val else 0)

    zif_pins[zif] = p

def set_input(dut_pin):
    zif = dut_to_zif(dut_pin)
    gpio = ZIF_TO_GPIO[zif]
    zif_pins[zif] = Pin(gpio, Pin.IN)

def set_input_pullup(dut_pin):
    zif = dut_to_zif(dut_pin)
    gpio = ZIF_TO_GPIO[zif]
    zif_pins[zif] = Pin(gpio, Pin.IN, Pin.PULL_UP)

def set_input_pulldown(dut_pin):
    zif = dut_to_zif(dut_pin)
    gpio = ZIF_TO_GPIO[zif]
    zif_pins[zif] = Pin(gpio, Pin.IN, Pin.PULL_DOWN)
    
def read_pin(dut_pin):
    zif = dut_to_zif(dut_pin)
    return zif_pins[zif].value()

# ------------------------------------------------------------
# Test helpers
# ------------------------------------------------------------

def test_gate_2in(name, a_pin, b_pin, y_pin, func):
    ok = True

    for a, b in [(0,0), (0,1), (1,0), (1,1)]:
        all_zif_inputs()

        set_output(a_pin, a)
        set_output(b_pin, b)
        set_input(y_pin)

        time.sleep_ms(50)

        expected = func(a, b)
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} B={} expected={} got={}".format(
                name, a, b, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_gate_2in_oc(name, a_pin, b_pin, y_pin, func):
    ok = True

    for a, b in [(0,0), (0,1), (1,0), (1,1)]:
        all_zif_inputs()

        set_output(a_pin, a)
        set_output(b_pin, b)

        # Open-collector outputs need a pull-up because the IC only pulls low.
        set_input_pullup(y_pin)

        time.sleep_ms(50)

        expected = func(a, b)
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} B={} expected={} got={}".format(
                name, a, b, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_buffer_oc(name, a_pin, y_pin):
    ok = True

    for a in [0, 1]:
        all_zif_inputs()

        set_output(a_pin, a)
        set_input_pullup(y_pin)

        time.sleep_ms(50)

        expected = 1 if a else 0
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} expected={} got={}".format(
                name, a, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_inverter_oc(name, a_pin, y_pin):
    ok = True

    for a in [0, 1]:
        all_zif_inputs()

        set_output(a_pin, a)
        set_input_pullup(y_pin)

        time.sleep_ms(50)

        expected = 0 if a else 1
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} expected={} got={}".format(
                name, a, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_gate_3in(name, a_pin, b_pin, c_pin, y_pin, func):
    ok = True

    set_input(y_pin)

    tests = [
        (0,0,0),
        (0,0,1),
        (0,1,0),
        (0,1,1),
        (1,0,0),
        (1,0,1),
        (1,1,0),
        (1,1,1),
    ]

    for a,b,c in tests:

        set_output(a_pin, a)
        set_output(b_pin, b)
        set_output(c_pin, c)

        time.sleep_ms(100)

        expected = func(a,b,c)
        got = read_pin(y_pin)

        print(
            name,
            "A={} B={} C={} expected={} got={}".format(
                a,b,c,expected,got
            )
        )

        if got != expected:
            ok = False

    if ok:
        print(name, "PASS")

    return ok

def test_gate_4in(name, a_pin, b_pin, c_pin, d_pin, y_pin, func):
    ok = True

    tests = [
        (0,0,0,0), (0,0,0,1), (0,0,1,0), (0,0,1,1),
        (0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1),
        (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1),
        (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1),
    ]

    for a,b,c,d in tests:
        all_zif_inputs()
        set_output(a_pin, a)
        set_output(b_pin, b)
        set_output(c_pin, c)
        set_output(d_pin, d)
        set_input(y_pin)

        time.sleep_ms(50)

        expected = func(a,b,c,d)
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} B={} C={} D={} expected={} got={}".format(
                name, a,b,c,d,expected,got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_gate_8in(name, pins, y_pin, func):
    ok = True

    tests = [
        [0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1],
    ]

    for values in tests:
        all_zif_inputs()

        for pin, val in zip(pins, values):
            set_output(pin, val)

        set_input(y_pin)

        time.sleep_ms(50)

        expected = func(values)
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL inputs={} expected={} got={}".format(
                name, values, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_inverter(name, a_pin, y_pin):
    ok = True

    for a in [0, 1]:
        all_zif_inputs()

        set_output(a_pin, a)
        set_input(y_pin)

        time.sleep_ms(50)

        expected = 0 if a else 1
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} expected={} got={}".format(
                name, a, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def expect_decoder_outputs(y0, y1, y2, y3, expected):
    return [
        y0 == expected[0],
        y1 == expected[1],
        y2 == expected[2],
        y3 == expected[3],
    ]
def test_buffer_3state(name, oe_pin, a_pin, y_pin, oe_active_low=True):
    ok = True

    # Enabled test
    enable_val = 0 if oe_active_low else 1

    for a in [0, 1]:
        all_zif_inputs()

        set_output(oe_pin, enable_val)
        set_output(a_pin, a)
        set_input(y_pin)

        time.sleep_ms(50)

        got = read_pin(y_pin)

        if got != a:
            print("{} FAIL ENABLED A={} expected={} got={}".format(
                name, a, a, got
            ))
            ok = False

    # Disabled / Hi-Z test
    disable_val = 1 if oe_active_low else 0

    all_zif_inputs()
    set_output(oe_pin, disable_val)
    set_output(a_pin, 0)
    set_input_pullup(y_pin)
    time.sleep_ms(50)
    got_hi = read_pin(y_pin)

    all_zif_inputs()
    set_output(oe_pin, disable_val)
    set_output(a_pin, 1)
    set_input_pulldown(y_pin)
    time.sleep_ms(50)
    got_lo = read_pin(y_pin)

    if got_hi != 1 or got_lo != 0:
        print("{} FAIL Hi-Z expected pullup=1 pulldown=0 got {}/{}".format(
            name, got_hi, got_lo
        ))
        ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

def test_shiftreg_74164():
    print("Testing 74164 8-bit shift register")

    ok = True

    # Pins
    # 1=A, 2=B, 8=GND
    # 9..13,15,16,17 = Q outputs
    # 8 CLK
    # 9 CLR\

    q_pins = [3,4,5,6,10,11,12,13]

    # -------------------------
    # Reset test
    # -------------------------

    all_zif_inputs()

    # CLR low
    set_output(9, 0)

    # CLK low
    set_output(8, 0)

    for q in q_pins:
        set_input(q)

    time.sleep_ms(50)

    got = [read_pin(q) for q in q_pins]

    if got != [0]*8:
        print("RESET FAIL got={}".format(got))
        ok = False

    # -------------------------
    # Shift in 10101010
    # -------------------------

    pattern = [1,0,1,0,1,0,1,0]

    all_zif_inputs()

    # CLR high = enabled
    set_output(9, 1)

    # B high permanently
    set_output(2, 1)

    set_output(8, 0)

    for bit in pattern:

        # A input
        set_output(1, bit)

        time.sleep_ms(10)

        # rising edge
        set_output(8, 1)
        time.sleep_ms(10)

        # falling edge
        set_output(8, 0)
        time.sleep_ms(10)

    for q in q_pins:
        set_input(q)

    time.sleep_ms(50)

    got = [read_pin(q) for q in q_pins]

    expected = list(reversed(pattern))

    if got != expected:
        print("SHIFT FAIL expected={} got={}".format(expected, got))
        ok = False

    all_zif_inputs()

    if ok:
        print("74164 PASS")

    return ok

def test_octal_buffer_244():
    ok = True

    # Group 1 enable = pin 1
    # Group 2 enable = pin 19

    # -------------------------
    # Group 1
    # -------------------------

    pairs1 = [
        (2,18),
        (4,16),
        (6,14),
        (8,12),
    ]

    for a_pin, y_pin in pairs1:
        ok &= test_buffer_3state(
            "BUF {}->{}".format(a_pin, y_pin),
            1,
            a_pin,
            y_pin,
            True
        )

    # -------------------------
    # Group 2
    # -------------------------

    pairs2 = [
        (11,9),
        (13,7),
        (15,5),
        (17,3),
    ]

    for a_pin, y_pin in pairs2:
        ok &= test_buffer_3state(
            "BUF {}->{}".format(a_pin, y_pin),
            19,
            a_pin,
            y_pin,
            True
        )

    return ok

def test_bus_transceiver_245():
    ok = True

    # ---------------------------------
    # A -> B direction
    # DIR=1, OE=0
    # ---------------------------------

    pairs = [
        (2,18),
        (3,17),
        (4,16),
        (5,15),
        (6,14),
        (7,13),
        (8,12),
        (9,11),
    ]

    for a_pin, b_pin in pairs:

        for val in [0,1]:

            all_zif_inputs()

            # OE low = enabled
            set_output(19, 0)

            # DIR high = A -> B
            set_output(1, 1)

            set_output(a_pin, val)
            set_input(b_pin)

            time.sleep_ms(50)

            got = read_pin(b_pin)

            if got != val:
                print("A->B FAIL {}->{} val={} got={}".format(
                    a_pin, b_pin, val, got
                ))
                ok = False

    # ---------------------------------
    # B -> A direction
    # DIR=0, OE=0
    # ---------------------------------

    for a_pin, b_pin in pairs:

        for val in [0,1]:

            all_zif_inputs()

            set_output(19, 0)

            # DIR low = B -> A
            set_output(1, 0)

            set_output(b_pin, val)
            set_input(a_pin)

            time.sleep_ms(50)

            got = read_pin(a_pin)

            if got != val:
                print("B->A FAIL {}->{} val={} got={}".format(
                    b_pin, a_pin, val, got
                ))
                ok = False

    # ---------------------------------
    # Hi-Z test
    # ---------------------------------

    all_zif_inputs()

    # OE high = disabled
    set_output(19, 1)
    set_output(1, 1)

    set_output(2, 1)

    set_input_pulldown(18)

    time.sleep_ms(50)

    if read_pin(18) != 0:
        print("Hi-Z FAIL")
        ok = False

    all_zif_inputs()

    if ok:
        print("74245 PASS")

    return ok

def test_register_74273():
    print("Testing 74273 octal D register with clear")

    ok = True

    # 1 = CLR\
    # 11 = CLK

    d_pins = [3,4,7,8,13,14,17,18]
    q_pins = [2,5,6,9,12,15,16,19]

    patterns = [
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
    ]

    # -------------------------
    # Clear test
    # -------------------------

    all_zif_inputs()

    set_output(1, 0)  # CLR low
    set_output(11, 0)

    for q in q_pins:
        set_input(q)

    time.sleep_ms(50)

    got = [read_pin(q) for q in q_pins]

    if got != [0]*8:
        print("CLEAR FAIL got={}".format(got))
        ok = False

    # -------------------------
    # Register tests
    # -------------------------

    for pattern in patterns:

        all_zif_inputs()

        # CLR inactive
        set_output(1, 1)

        # CLK low
        set_output(11, 0)

        for d,val in zip(d_pins, pattern):
            set_output(d, val)

        for q in q_pins:
            set_input(q)

        time.sleep_ms(20)

        # rising edge
        set_output(11, 1)
        time.sleep_ms(20)

        # back low
        set_output(11, 0)
        time.sleep_ms(20)

        got = [read_pin(q) for q in q_pins]

        if got != pattern:
            print("LOAD FAIL expected={} got={}".format(
                pattern, got
            ))
            ok = False

        # change D inputs
        inverse = [0 if x else 1 for x in pattern]

        for d,val in zip(d_pins, inverse):
            set_output(d, val)

        time.sleep_ms(50)

        got_hold = [read_pin(q) for q in q_pins]

        if got_hold != pattern:
            print("HOLD FAIL expected={} got={}".format(
                pattern, got_hold
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("74273 PASS")

    return ok

def test_latch_373_family(name, le_pin, oe_pin, d_pins, q_pins):
    print("Testing", name)

    ok = True

    patterns = [
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
    ]

    for pattern in patterns:
        all_zif_inputs()

        # Enable outputs: /OE low
        set_output(oe_pin, 0)

        # Transparent latch: LE high
        set_output(le_pin, 1)

        for d_pin, val in zip(d_pins, pattern):
            set_output(d_pin, val)

        for q_pin in q_pins:
            set_input(q_pin)

        time.sleep_ms(50)

        got = [read_pin(q) for q in q_pins]

        if got != pattern:
            print("TRANSPARENT FAIL expected={} got={}".format(pattern, got))
            ok = False

        # Latch current value: LE low
        set_output(le_pin, 0)
        time.sleep_ms(20)

        # Change D inputs to inverse; Q should not change
        inverse = [0 if x else 1 for x in pattern]

        for d_pin, val in zip(d_pins, inverse):
            set_output(d_pin, val)

        time.sleep_ms(50)

        got_hold = [read_pin(q) for q in q_pins]

        if got_hold != pattern:
            print("HOLD FAIL expected={} got={}".format(pattern, got_hold))
            ok = False

    # Hi-Z output disable test
    all_zif_inputs()

    set_output(oe_pin, 1)  # /OE high = disabled
    set_output(le_pin, 0)

    for q_pin in q_pins:
        set_input_pulldown(q_pin)

    time.sleep_ms(50)

    got_pd = [read_pin(q) for q in q_pins]

    for q_pin in q_pins:
        set_input_pullup(q_pin)

    time.sleep_ms(50)

    got_pu = [read_pin(q) for q in q_pins]

    if got_pd != [0]*8 or got_pu != [1]*8:
        print("Hi-Z FAIL pulldown={} pullup={}".format(got_pd, got_pu))
        ok = False

    all_zif_inputs()

    if ok:
        print(name, "PASS")

    return ok

def test_register_374_family(name, clk_pin, oe_pin, d_pins, q_pins):
    print("Testing", name)

    ok = True

    patterns = [
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
    ]

    for pattern in patterns:
        all_zif_inputs()

        # Enable outputs: /OE low
        set_output(oe_pin, 0)

        # Clock low first
        set_output(clk_pin, 0)

        for d_pin, val in zip(d_pins, pattern):
            set_output(d_pin, val)

        for q_pin in q_pins:
            set_input(q_pin)

        time.sleep_ms(20)

        # Rising edge loads data
        set_output(clk_pin, 0)
        time.sleep_ms(20)
        set_output(clk_pin, 1)
        time.sleep_ms(20)

        got = [read_pin(q) for q in q_pins]

        if got != pattern:
            print("LOAD FAIL expected={} got={}".format(pattern, got))
            ok = False

        # Change D inputs, Q should hold until next clock
        inverse = [0 if x else 1 for x in pattern]

        for d_pin, val in zip(d_pins, inverse):
            set_output(d_pin, val)

        time.sleep_ms(50)

        got_hold = [read_pin(q) for q in q_pins]

        if got_hold != pattern:
            print("HOLD FAIL expected={} got={}".format(pattern, got_hold))
            ok = False

    # Hi-Z output disable test
    all_zif_inputs()

    set_output(oe_pin, 1)  # /OE high = disabled
    set_output(clk_pin, 0)

    for q_pin in q_pins:
        set_input_pulldown(q_pin)

    time.sleep_ms(50)
    got_pd = [read_pin(q) for q in q_pins]

    for q_pin in q_pins:
        set_input_pullup(q_pin)

    time.sleep_ms(50)
    got_pu = [read_pin(q) for q in q_pins]

    if got_pd != [0]*8 or got_pu != [1]*8:
        print("Hi-Z FAIL pulldown={} pullup={}".format(got_pd, got_pu))
        ok = False

    all_zif_inputs()

    if ok:
        print(name, "PASS")

    return ok

def clock_pulse(pin):
    set_output(pin, 1)
    time.sleep_ms(5)
    set_output(pin, 0)
    time.sleep_ms(5)
    set_output(pin, 1)
    time.sleep_ms(5)

def test_counter_74393():
    print("Testing 74393 dual 4-bit ripple counter")

    ok = True

    # Counter A
    # CLR1=2
    # CLK1=1
    # Q0=3 Q1=4 Q2=5 Q3=6

    # Counter B
    # CLK2=13
    # CLR2=12
    # Q0=11 Q1=10 Q2=9 Q3=8

    counters = [
        (1, 2, [3,4,5,6], "A"),
        (13,12,[11,10,9,8], "B"),
    ]

    for clk_pin, clr_pin, q_pins, label in counters:

        # -------------------------
        # Clear test
        # -------------------------

        all_zif_inputs()

        set_output(clr_pin, 1)
        set_output(clk_pin, 0)

        for q in q_pins:
            set_input(q)

        time.sleep_ms(20)

        set_output(clr_pin, 0)
        time.sleep_ms(20)

        got = [read_pin(q) for q in q_pins]

        if got != [0,0,0,0]:
            print("CLR FAIL {} got={}".format(label, got))
            ok = False

        # release clear
        set_output(clr_pin, 0)

        # -------------------------
        # Count test
        # -------------------------

        for count in range(16):

            got = [read_pin(q) for q in q_pins]

            expected = [
                (count >> 0) & 1,
                (count >> 1) & 1,
                (count >> 2) & 1,
                (count >> 3) & 1,
            ]

            if got != expected:
                print("{} COUNT FAIL count={} expected={} got={}".format(
                    label, count, expected, got
                ))
                ok = False

            clock_pulse(clk_pin)
            time.sleep_ms(10)

    all_zif_inputs()

    if ok:
        print("74393 PASS")

    return ok

def test_gate_3in_safe(name, a_pin, b_pin, c_pin, y_pin, func):
    ok = True

    tests = [
        (0,0,0),
        (0,0,1),
        (0,1,0),
        (0,1,1),
        (1,0,0),
        (1,0,1),
        (1,1,0),
        (1,1,1),
    ]

    for a,b,c in tests:
        all_zif_inputs()

        set_output(a_pin, a)
        set_output(b_pin, b)
        set_output(c_pin, c)
        set_input(y_pin)

        time.sleep_ms(50)

        expected = func(a,b,c)
        got = read_pin(y_pin)

        if got != expected:
            print("{} FAIL A={} B={} C={} expected={} got={}".format(
                name, a, b, c, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("{} PASS".format(name))

    return ok

# ------------------------------------------------------------
# Chip tests
# ------------------------------------------------------------

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

def test_7403():
    print("Testing 7403 open-collector NAND")
    return all([
        test_gate_2in_oc("Gate1", 1, 2, 3, lambda a,b: 0 if a and b else 1),
        test_gate_2in_oc("Gate2", 4, 5, 6, lambda a,b: 0 if a and b else 1),
        test_gate_2in_oc("Gate3", 9, 10, 8, lambda a,b: 0 if a and b else 1),
        test_gate_2in_oc("Gate4", 12, 13, 11, lambda a,b: 0 if a and b else 1),
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

def test_7405():
    print("Testing 7405 open-collector inverter")
    return all([
        test_inverter_oc("Inv1", 1, 2),
        test_inverter_oc("Inv2", 3, 4),
        test_inverter_oc("Inv3", 5, 6),
        test_inverter_oc("Inv4", 9, 8),
        test_inverter_oc("Inv5", 11, 10),
        test_inverter_oc("Inv6", 13, 12),
    ])


def test_7406():
    print("Testing 7406 open-collector inverter")
    return test_7405()


def test_7407():
    print("Testing 7407 open-collector buffer")
    return all([
        test_buffer_oc("Buf1", 1, 2),
        test_buffer_oc("Buf2", 3, 4),
        test_buffer_oc("Buf3", 5, 6),
        test_buffer_oc("Buf4", 9, 8),
        test_buffer_oc("Buf5", 11, 10),
        test_buffer_oc("Buf6", 13, 12),
    ])

def test_7408():
    print("Testing 7408 AND")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 1 if a and b else 0),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 1 if a and b else 0),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 1 if a and b else 0),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 1 if a and b else 0),
    ])

def test_7410():
    print("Testing 7410 triple 3-input NAND")

    ok = True

    # Gate1: 1,2,13 -> 12
    ok &= test_gate_3in(
        "Gate1",
        1, 2, 13, 12,
        lambda a,b,c: 0 if (a and b and c) else 1
    )

    # Gate2: 3,4,5 -> 6
    ok &= test_gate_3in(
        "Gate2",
        3, 4, 5, 6,
        lambda a,b,c: 0 if (a and b and c) else 1
    )

    # Gate3: 9,10,11 -> 8
    ok &= test_gate_3in(
        "Gate3",
        9, 10, 11, 8,
        lambda a,b,c: 0 if (a and b and c) else 1
    )

    return ok

def test_7411():
    print("Testing 7411 triple 3-input AND")

    return all([
        test_gate_3in_safe(
            "Gate1",
            1, 2, 13, 12,
            lambda a,b,c: 1 if (a and b and c) else 0
        ),
        test_gate_3in_safe(
            "Gate2",
            3, 4, 5, 6,
            lambda a,b,c: 1 if (a and b and c) else 0
        ),
        test_gate_3in_safe(
            "Gate3",
            9, 10, 11, 8,
            lambda a,b,c: 1 if (a and b and c) else 0
        ),
    ])

def test_7414():
    print("Testing 7414 Schmitt inverter")
    return all([
        test_inverter("Inv1", 1, 2),
        test_inverter("Inv2", 3, 4),
        test_inverter("Inv3", 5, 6),
        test_inverter("Inv4", 9, 8),
        test_inverter("Inv5", 11, 10),
        test_inverter("Inv6", 13, 12),
    ])

def test_7421():
    print("Testing 7421 dual 4-input AND")
    return all([
        test_gate_4in("Gate1", 1, 2, 4, 5, 6, lambda a,b,c,d: 1 if a and b and c and d else 0),
        test_gate_4in("Gate2", 9, 10, 12, 13, 8, lambda a,b,c,d: 1 if a and b and c and d else 0),
    ])

def test_7430():
    print("Testing 7430 8-input NAND")
    return test_gate_8in(
        "Gate1",
        [1, 2, 3, 4, 5, 6, 11, 12],
        8,
        lambda vals: 0 if all(vals) else 1
    )

def test_7432():
    print("Testing 7432 OR")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 1 if a or b else 0),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 1 if a or b else 0),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 1 if a or b else 0),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 1 if a or b else 0),
    ])
def test_7474():
    print("Testing 7474 dual D flip-flop")

    ok = True

    # 7474 pinout
    # FF1:
    # 1  = /CLR1
    # 2  = D1
    # 3  = CLK1
    # 4  = /PRE1
    # 5  = Q1
    # 6  = /Q1
    #
    # FF2:
    # 8  = /Q2
    # 9  = Q2
    # 10 = /PRE2
    # 11 = CLK2
    # 12 = D2
    # 13 = /CLR2
    #
    # 7  = GND
    # 14 = VCC

    flipflops = [
        # name, clr, d, clk, pre, q, nq
        ("FF1", 1, 2, 3, 4, 5, 6),
        ("FF2", 13, 12, 11, 10, 9, 8),
    ]

    for name, clr, d, clk, pre, q, nq in flipflops:
        print("Testing", name)

        # -------------------------
        # Async clear
        # -------------------------
        all_zif_inputs()

        set_output(pre, 1)   # inactive
        set_output(clr, 0)   # active clear
        set_output(clk, 0)
        set_output(d, 1)

        set_input(q)
        set_input(nq)

        time.sleep_ms(50)

        qv = read_pin(q)
        nqv = read_pin(nq)

        if qv != 0 or nqv != 1:
            print("{} CLEAR FAIL Q={} /Q={}".format(name, qv, nqv))
            ok = False

        # -------------------------
        # Async preset
        # -------------------------
        all_zif_inputs()

        set_output(clr, 1)   # inactive
        set_output(pre, 0)   # active preset
        set_output(clk, 0)
        set_output(d, 0)

        set_input(q)
        set_input(nq)

        time.sleep_ms(50)

        qv = read_pin(q)
        nqv = read_pin(nq)

        if qv != 1 or nqv != 0:
            print("{} PRESET FAIL Q={} /Q={}".format(name, qv, nqv))
            ok = False

        # -------------------------
        # Clock D=0
        # -------------------------
        all_zif_inputs()

        set_output(clr, 1)   # inactive
        set_output(pre, 1)   # inactive
        set_output(clk, 0)
        set_output(d, 0)

        set_input(q)
        set_input(nq)

        time.sleep_ms(20)

        set_output(clk, 1)
        time.sleep_ms(20)
        set_output(clk, 0)
        time.sleep_ms(20)

        qv = read_pin(q)
        nqv = read_pin(nq)

        if qv != 0 or nqv != 1:
            print("{} CLOCK D=0 FAIL Q={} /Q={}".format(name, qv, nqv))
            ok = False

        # -------------------------
        # Clock D=1
        # -------------------------
        all_zif_inputs()

        set_output(clr, 1)
        set_output(pre, 1)
        set_output(clk, 0)
        set_output(d, 1)

        set_input(q)
        set_input(nq)

        time.sleep_ms(20)

        set_output(clk, 1)
        time.sleep_ms(20)
        set_output(clk, 0)
        time.sleep_ms(20)

        qv = read_pin(q)
        nqv = read_pin(nq)

        if qv != 1 or nqv != 0:
            print("{} CLOCK D=1 FAIL Q={} /Q={}".format(name, qv, nqv))
            ok = False

    all_zif_inputs()

    if ok:
        print("7474 PASS")

    return ok

def test_7486():
    print("Testing 7486 XOR")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 1 if a != b else 0),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 1 if a != b else 0),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 1 if a != b else 0),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 1 if a != b else 0),
    ])

def test_74125():
    print("Testing 74125 quad tri-state buffer, active-low enable")
    return all([
        test_buffer_3state("Buf1", 1, 2, 3, True),
        test_buffer_3state("Buf2", 4, 5, 6, True),
        test_buffer_3state("Buf3", 10, 9, 8, True),
        test_buffer_3state("Buf4", 13, 12, 11, True),
    ])

def test_74126():
    print("Testing 74126 quad tri-state buffer, active-HIGH enable")
    return all([
        test_buffer_3state("Buf1", 1, 2, 3, False),
        test_buffer_3state("Buf2", 4, 5, 6, False),
        test_buffer_3state("Buf3", 10, 9, 8, False),
        test_buffer_3state("Buf4", 13, 12, 11, False),
    ])

def test_74132():
    print("Testing 74132 Schmitt NAND")
    return all([
        test_gate_2in("Gate1", 1, 2, 3, lambda a,b: 0 if a and b else 1),
        test_gate_2in("Gate2", 4, 5, 6, lambda a,b: 0 if a and b else 1),
        test_gate_2in("Gate3", 9, 10, 8, lambda a,b: 0 if a and b else 1),
        test_gate_2in("Gate4", 12, 13, 11, lambda a,b: 0 if a and b else 1),
    ])

def test_74138():
    print("Testing 74138 3-to-8 decoder")

    ok = True

    # Pinout:
    # A=1, B=2, C=3
    # G2A=4 active LOW
    # G2B=5 active LOW
    # G1=6 active HIGH
    # outputs active LOW:
    # Y0=15, Y1=14, Y2=13, Y3=12
    # Y4=11, Y5=10, Y6=9,  Y7=7

    out_pins = [15,14,13,12,11,10,9,7]

    for value in range(8):
        all_zif_inputs()

        a = value & 1
        b = (value >> 1) & 1
        c = (value >> 2) & 1

        # Enable decoder
        set_output(4, 0)  # G2A low
        set_output(5, 0)  # G2B low
        set_output(6, 1)  # G1 high

        set_output(1, a)
        set_output(2, b)
        set_output(3, c)

        for y in out_pins:
            set_input(y)

        time.sleep_ms(50)

        got = [read_pin(y) for y in out_pins]

        expected = [1,1,1,1,1,1,1,1]
        expected[value] = 0

        if got != expected:
            print("DECODE FAIL value={} expected={} got={}".format(
                value, expected, got
            ))
            ok = False

    # Disabled tests: all outputs HIGH
    all_zif_inputs()

    set_output(4, 1)  # disable via G2A high
    set_output(5, 0)
    set_output(6, 1)

    for y in out_pins:
        set_input(y)

    time.sleep_ms(50)

    got = [read_pin(y) for y in out_pins]

    if got != [1]*8:
        print("DISABLE FAIL expected all HIGH got={}".format(got))
        ok = False

    all_zif_inputs()

    if ok:
        print("74138 PASS")

    return ok

def test_74139():
    print("Testing 74139 dual 2-to-4 decoder")

    ok = True

    tests = [
        (0,0,[0,1,1,1]),
        (1,0,[1,0,1,1]),
        (0,1,[1,1,0,1]),
        (1,1,[1,1,1,0]),
    ]

    # Decoder 1: /G=1, A=2, B=3, Y0..Y3=4,5,6,7
    for a,b,expected in tests:
        all_zif_inputs()

        set_output(1, 0)
        set_output(2, a)
        set_output(3, b)

        for y in [4,5,6,7]:
            set_input(y)

        time.sleep_ms(50)

        got = [read_pin(y) for y in [4,5,6,7]]

        if got != expected:
            print("DEC1 FAIL A={} B={} expected={} got={}".format(
                a, b, expected, got
            ))
            ok = False

    # Decoder 2: /G=15, A=14, B=13, Y0..Y3=12,11,10,9
    for a,b,expected in tests:
        all_zif_inputs()

        set_output(15, 0)
        set_output(14, a)
        set_output(13, b)

        for y in [12,11,10,9]:
            set_input(y)

        time.sleep_ms(50)

        got = [read_pin(y) for y in [12,11,10,9]]

        if got != expected:
            print("DEC2 FAIL A={} B={} expected={} got={}".format(
                a, b, expected, got
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("74139 PASS")

    return ok

def test_74157():
    print("Testing 74157 quad 2-to-1 multiplexer")

    ok = True

    # Correct 74157 pinout
    # 1  = SEL
    # 2  = 1A
    # 3  = 1B
    # 4  = 1Y
    # 5  = 2A
    # 6  = 2B
    # 7  = 2Y
    # 8  = GND
    # 9  = 3Y
    # 10 = 3B
    # 11 = 3A
    # 12 = 4Y
    # 13 = 4B
    # 14 = 4A
    # 15 = /G enable, active LOW
    # 16 = VCC

    channels = [
        (2, 3, 4),      # 1A, 1B, 1Y
        (5, 6, 7),      # 2A, 2B, 2Y
        (11, 10, 9),    # 3A, 3B, 3Y
        (14, 13, 12),   # 4A, 4B, 4Y
    ]

    patterns = [
        ([0, 1, 0, 1], [1, 0, 1, 0]),
        ([1, 1, 0, 0], [0, 0, 1, 1]),
    ]

    for a_vals, b_vals in patterns:

        all_zif_inputs()
        set_output(15, 0)  # /G enabled
        set_output(1, 0)   # select A

        for i, (a_pin, b_pin, y_pin) in enumerate(channels):
            set_output(a_pin, a_vals[i])
            set_output(b_pin, b_vals[i])
            set_input(y_pin)

        time.sleep_ms(50)

        got = [read_pin(y_pin) for _, _, y_pin in channels]

        if got != a_vals:
            print("SEL=A FAIL expected={} got={}".format(a_vals, got))
            ok = False

        all_zif_inputs()
        set_output(15, 0)  # /G enabled
        set_output(1, 1)   # select B

        for i, (a_pin, b_pin, y_pin) in enumerate(channels):
            set_output(a_pin, a_vals[i])
            set_output(b_pin, b_vals[i])
            set_input(y_pin)

        time.sleep_ms(50)

        got = [read_pin(y_pin) for _, _, y_pin in channels]

        if got != b_vals:
            print("SEL=B FAIL expected={} got={}".format(b_vals, got))
            ok = False

    # Disable test: /G high forces outputs LOW
    all_zif_inputs()
    set_output(15, 1)

    for a_pin, b_pin, y_pin in channels:
        set_output(a_pin, 1)
        set_output(b_pin, 1)
        set_input(y_pin)

    time.sleep_ms(50)

    got = [read_pin(y_pin) for _, _, y_pin in channels]

    if got != [0, 0, 0, 0]:
        print("DISABLE FAIL expected=[0, 0, 0, 0] got={}".format(got))
        ok = False

    all_zif_inputs()

    if ok:
        print("74157 PASS")

    return ok

def test_74163():
    print("Testing 74163 4-bit synchronous counter")

    ok = True

    # 74163 pinout
    # 1  = /CLR synchronous clear
    # 2  = CLK
    # 3  = A
    # 4  = B
    # 5  = C
    # 6  = D
    # 7  = ENP
    # 9  = /LOAD
    # 10 = ENT
    # 11 = QD
    # 12 = QC
    # 13 = QB
    # 14 = QA

    q_pins = [14, 13, 12, 11]  # QA,QB,QC,QD

    all_zif_inputs()

    set_output(2, 0)    # CLK low
    set_output(9, 1)    # /LOAD inactive
    set_output(7, 1)    # ENP enabled
    set_output(10, 1)   # ENT enabled

    for q in q_pins:
        set_input(q)

    # -------------------------
    # Synchronous clear to 0
    # -------------------------
    print("Clearing counter")

    set_output(1, 0)    # /CLR active low

    time.sleep_ms(20)
    set_output(2, 1)    # rising edge clears
    time.sleep_ms(20)
    set_output(2, 0)
    time.sleep_ms(20)

    set_output(1, 1)    # /CLR inactive

    got = [read_pin(q) for q in q_pins]

    if got != [0, 0, 0, 0]:
        print("CLEAR FAIL expected=[0, 0, 0, 0] got={}".format(got))
        ok = False

    # -------------------------
    # Count test
    # -------------------------
    for count in range(16):
        got = [read_pin(q) for q in q_pins]

        expected = [
            (count >> 0) & 1,
            (count >> 1) & 1,
            (count >> 2) & 1,
            (count >> 3) & 1,
        ]

        if got != expected:
            print("COUNT FAIL count={} expected={} got={}".format(
                count, expected, got
            ))
            ok = False

        set_output(2, 1)
        time.sleep_ms(20)
        set_output(2, 0)
        time.sleep_ms(20)

    all_zif_inputs()

    if ok:
        print("74163 PASS")

    return ok

def test_74164():
    return test_shiftreg_74164()

def test_74244():
    print("Testing 74244 octal tri-state buffer")
    return test_octal_buffer_244()

def test_74245():
    print("Testing 74245 octal bus transceiver")
    return test_bus_transceiver_245()

def test_74165():
    print("Testing 74165 parallel-in serial-out shift register")

    ok = True

    # Pinout:
    # 1 = /PL parallel load, active LOW
    # 2 = CLK
    # 7 = QH serial out
    # 9 = QH\ inverted serial out
    # 10 = SER
    # 15 = CLK INH
    # Parallel inputs:
    # A=11, B=12, C=13, D=14, E=3, F=4, G=5, H=6

    data_pins = [11,12,13,14,3,4,5,6]
    pattern = [1,0,1,0,1,0,1,0]

    all_zif_inputs()

    set_output(15, 0)   # clock enable
    set_output(2, 0)    # CLK low
    set_output(10, 0)   # serial input low

    for pin, val in zip(data_pins, pattern):
        set_output(pin, val)

    set_input(7)
    set_input(9)

    # parallel load
    set_output(1, 0)
    time.sleep_ms(20)
    set_output(1, 1)
    time.sleep_ms(20)

    got_bits = []
    got_inv_bits = []

    for i in range(8):
        got_bits.append(read_pin(7))
        got_inv_bits.append(read_pin(9))

        # clock next bit
        set_output(2, 1)
        time.sleep_ms(20)
        set_output(2, 0)
        time.sleep_ms(20)

    # 74165 shifts H first from QH after load
    expected = pattern
    expected_inv = [0 if x else 1 for x in expected]

    if got_bits != expected:
        print("SHIFT FAIL expected={} got={}".format(expected, got_bits))
        ok = False

    if got_inv_bits != expected_inv:
        print("INV SHIFT FAIL expected={} got={}".format(
            expected_inv, got_inv_bits
        ))
        ok = False

    all_zif_inputs()

    if ok:
        print("74165 PASS")

    return ok

def test_74174():
    print("Testing 74174 hex D flip-flop")

    ok = True

    # Pinout:
    # 1 = /CLR
    # 9 = CLK

    # D pins
    d_pins = [3, 4, 6, 11, 13, 14]

    # Q pins
    q_pins = [2, 5, 7, 10, 12, 15]

    patterns = [
        [0,0,0,0,0,0],
        [1,1,1,1,1,1],
        [1,0,1,0,1,0],
        [0,1,0,1,0,1],
    ]

    all_zif_inputs()

    # -------------------------
    # Clear test
    # -------------------------

    set_output(1, 0)  # /CLR active
    set_output(9, 0)  # CLK low

    for q in q_pins:
        set_input(q)

    time.sleep_ms(50)

    got = [read_pin(q) for q in q_pins]

    if got != [0]*6:
        print("CLEAR FAIL got={}".format(got))
        ok = False

    # release clear
    set_output(1, 1)

    # -------------------------
    # Pattern tests
    # -------------------------

    for pattern in patterns:

        all_zif_inputs()

        set_output(1, 1)  # /CLR inactive
        set_output(9, 0)  # CLK low

        for d,val in zip(d_pins, pattern):
            set_output(d, val)

        for q in q_pins:
            set_input(q)

        time.sleep_ms(20)

        # rising edge clocks data
        set_output(9, 1)
        time.sleep_ms(20)
        set_output(9, 0)
        time.sleep_ms(20)

        got = [read_pin(q) for q in q_pins]

        if got != pattern:
            print("LOAD FAIL expected={} got={}".format(
                pattern, got
            ))
            ok = False

        # change D inputs, outputs should hold
        inverse = [0 if x else 1 for x in pattern]

        for d,val in zip(d_pins, inverse):
            set_output(d, val)

        time.sleep_ms(50)

        got_hold = [read_pin(q) for q in q_pins]

        if got_hold != pattern:
            print("HOLD FAIL expected={} got={}".format(
                pattern, got_hold
            ))
            ok = False

    all_zif_inputs()

    if ok:
        print("74174 PASS")

    return ok

def test_74273():
    return test_register_74273()

def test_74373():
    return test_latch_373_family(
        "74373 octal transparent latch",
        11,  # LE
        1,   # /OE
        [3,4,7,8,13,14,17,18],     # D0-D7
        [2,5,6,9,12,15,16,19],     # Q0-Q7
    )

    return ok

def test_74374():
    return test_register_374_family(
        "74374 octal D register",
        11,  # CLK
        1,   # /OE
        [3,4,7,8,13,14,17,18],     # D0-D7
        [2,5,6,9,12,15,16,19],     # Q0-Q7
    )

def test_74393():
    return test_counter_74393()

def test_74573():
    return test_latch_373_family(
        "74573 octal transparent latch",
        11,  # LE
        1,   # /OE
        [2,3,4,5,6,7,8,9],          # D0-D7
        [19,18,17,16,15,14,13,12],  # Q0-Q7
    )

def test_74574():
    return test_register_374_family(
        "74574 octal D register",
        11,  # CLK
        1,   # /OE
        [2,3,4,5,6,7,8,9],          # D0-D7
        [19,18,17,16,15,14,13,12],  # Q0-Q7
    )

def test_74595():
    print("Testing 74595 serial-in/parallel-out register")

    ok = True

    # Pinout:
    # 10 = /SRCLR
    # 11 = SRCLK
    # 12 = RCLK (latch)
    # 13 = /OE
    # 14 = SER

    # Outputs:
    # QA=15 QB=1 QC=2 QD=3
    # QE=4  QF=5 QG=6 QH=7

    q_pins = [15,1,2,3,4,5,6,7]

    pattern = [1,0,1,0,1,0,1,0]

    all_zif_inputs()

    # enable outputs
    set_output(13, 0)   # /OE low

    # shift register clear inactive
    set_output(10, 1)

    # clocks low
    set_output(11, 0)
    set_output(12, 0)

    # serial input
    set_output(14, 0)

    for q in q_pins:
        set_input(q)

    time.sleep_ms(20)

    # -------------------------
    # Shift bits in
    # -------------------------

    for bit in pattern:

        set_output(14, bit)

        time.sleep_ms(10)

        # shift clock pulse
        set_output(11, 1)
        time.sleep_ms(10)
        set_output(11, 0)
        time.sleep_ms(10)

    # -------------------------
    # Latch outputs
    # -------------------------

    set_output(12, 1)
    time.sleep_ms(20)
    set_output(12, 0)

    time.sleep_ms(20)

    got = [read_pin(q) for q in q_pins]

    expected = list(reversed(pattern))

    if got != expected:
        print("SHIFT/LATCH FAIL expected={} got={}".format(
            expected, got
        ))
        ok = False

    # -------------------------
    # Clear test
    # -------------------------

    set_output(10, 0)  # /SRCLR active
    time.sleep_ms(20)
    set_output(10, 1)

    # latch cleared register
    set_output(12, 1)
    time.sleep_ms(20)
    set_output(12, 0)

    time.sleep_ms(20)

    got_clear = [read_pin(q) for q in q_pins]

    if got_clear != [0]*8:
        print("CLEAR FAIL got={}".format(got_clear))
        ok = False

    all_zif_inputs()

    if ok:
        print("74595 PASS")

    return ok

CHIPS = [
    {"name": "7400 NAND", "pins": 14, "test": test_7400},
    {"name": "7402 NOR",  "pins": 14, "test": test_7402},
    {"name": "7403 NAND OC", "pins": 14, "test": test_7403},
    {"name": "7404 INV",  "pins": 14, "test": test_7404},
    {"name": "7405 INV OC",  "pins": 14, "test": test_7405},
    {"name": "7406 INV OC",  "pins": 14, "test": test_7406},
    {"name": "7407 BUF OC",  "pins": 14, "test": test_7407},
    {"name": "7408 AND",  "pins": 14, "test": test_7408},
    {"name": "7410 3NAND", "pins": 14, "test": test_7410},
    {"name": "7411 3AND", "pins": 14, "test": test_7411},
    {"name": "7414 SCHMITT INV", "pins": 14, "test": test_7414},
    {"name": "7421 4AND", "pins": 14, "test": test_7421},
    {"name": "7430 8NAND", "pins": 14, "test": test_7430},
    {"name": "7432 OR",   "pins": 14, "test": test_7432},
    {"name": "7474 DFF", "pins": 14, "test": test_7474},
    {"name": "7486 XOR",  "pins": 14, "test": test_7486},
    {"name": "74125 3STATE BUF", "pins": 14, "test": test_74125},
    {"name": "74126 3STATE BUF", "pins": 14, "test": test_74126},
    {"name": "74132 SCHMITT NAND", "pins": 14, "test": test_74132},
    {"name": "74138 DECODER", "pins": 16, "test": test_74138},
    {"name": "74139 DECODER", "pins": 16, "test": test_74139},
    {"name": "74157 MUX", "pins": 16, "test": test_74157},
    {"name": "74163 COUNTER", "pins": 16, "test": test_74163},
    {"name": "74164 SHIFTREG", "pins": 14, "test": test_74164},
    {"name": "74165 SHIFTREG", "pins": 16, "test": test_74165},
    {"name": "74174 DFF", "pins": 16, "test": test_74174},
    {"name": "74244 OCTAL BUF", "pins": 20, "test": test_74244},
    {"name": "74245 BUS XCVR", "pins": 20, "test": test_74245},
    {"name": "74273 D REG", "pins": 20, "test": test_74273},
    {"name": "74373 LATCH", "pins": 20, "test": test_74373},
    {"name": "74374 D REG", "pins": 20, "test": test_74374},
    {"name": "74393 COUNTER", "pins": 14, "test": test_74393},
    {"name": "74573 LATCH", "pins": 20, "test": test_74573},
    {"name": "74574 D REG", "pins": 20, "test": test_74574},
    {"name": "74595 SHIFTREG", "pins": 16, "test": test_74595},
]

selected = 0

families = ["HC", "HCT", "LS", "LVC"]
test_modes = ["Quick", "Full", "Soak 50", "Soak 500", "Soak INF", "Info"]

selected_family = 0
selected_mode = 0
selected_field = 0   # 0=IC, 1=Family, 2=Mode
last_enc_sw = enc_sw.value()

def show_status():
    pkg, _ = detect_package()
    volt = detect_voltage()
    chip = CHIPS[selected]

    print("\n==============================")
    print(PRODUCT_NAME)
    print("Package:", pkg if pkg else "NONE")
    print("Voltage:", volt)
    print("IC:", chip["name"])
    print("NEXT = select, TEST = run")
    print("==============================")

    oled_main(
        chip,
        families[selected_family],
        test_modes[selected_mode],
        pkg,
        volt,
        selected_field
    )

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

def power_on_self_test():
    print("\n========== POST ==========")

    devices = [hex(x) for x in i2c.scan()]
    print("I2C devices:", devices)

    if "0x20" in devices:
        print("MCP23017 ..... PASS")
    else:
        print("MCP23017 ..... FAIL")

    if "0x3c" in devices or "0x3d" in devices:
        print("OLED ......... PASS")
    else:
        print("OLED ......... FAIL")

    pkg, _ = detect_package()
    print("Package ......", pkg)

    volt = detect_voltage()
    print("Voltage ......", volt)

    print("TEST Button ..", "PRESSED" if mcp_input_low(BTN_TEST) else "RELEASED")

    print("POST COMPLETE")
    print("==========================\n")

    if oled:
        oled.fill(0)
        oled.text("POST PASS", 0, 0)
        oled.text("MCP OK", 0, 16)
        oled.text("OLED OK", 64, 16)
        oled.text("PKG {}".format(pkg), 0, 32)
        oled.text(volt, 64, 32)
        oled.text("Starting...", 0, 52)
        oled.show()
        time.sleep_ms(2000)
  
def load_stats():
    try:
        with open("stats.json", "r") as f:
            return json.load(f)
    except:
        return {
            "lifetime_pass": 0,
            "lifetime_fail": 0,
            "last_result": "NONE",
            "last_ic": "NONE"
        }

def save_stats():
    try:
        with open("stats.json", "w") as f:
            json.dump(stats, f)
    except Exception as e:
        print("STATS SAVE ERROR:", e)

def print_stats():
    session_total = session_pass + session_fail
    lifetime_total = stats["lifetime_pass"] + stats["lifetime_fail"]

    print("SESSION:  PASS={} FAIL={} TOTAL={}".format(
        session_pass, session_fail, session_total
    ))

    print("LIFETIME: PASS={} FAIL={} TOTAL={}".format(
        stats["lifetime_pass"],
        stats["lifetime_fail"],
        lifetime_total
    ))

    print("LAST: {} {}".format(
        stats["last_result"],
        stats["last_ic"]
    ))
stats = load_stats()

session_pass = 0
session_fail = 0

# ------------------------------------------------------------
# Program Initialisation
# ------------------------------------------------------------

# Display firmware banner on the serial console.
print(PRODUCT_NAME)

all_zif_inputs()

try:
    mcp_init()
    print("MCP23017 OK")
    oled_init()

    power_on_self_test()
    print("System Ready")
    
except Exception as e:
    
    print("MCP23017 ERROR:", e)
    while True:
        time.sleep(1)

beep(80)

last_pkg = None
last_volt = None
last_selected = None

# ------------------------------------------------------------
# Main Loop
# ------------------------------------------------------------

time.sleep_ms(500)

last_test_btn = False
last_family = None
last_mode = None
last_field = None

while True:
    all_zif_inputs()

    pkg, pkg_map = detect_package()
    volt = detect_voltage()
    chip = CHIPS[selected]

    if (
        pkg != last_pkg or
        volt != last_volt or
        selected != last_selected or
        selected_family != last_family or
        selected_mode != last_mode or
        selected_field != last_field
    ):
        show_status()

        last_pkg = pkg
        last_volt = volt
        last_selected = selected
        last_family = selected_family
        last_mode = selected_mode
        last_field = selected_field

    if volt == "OFF":
        rgb(1, 1, 0)
        time.sleep_ms(120)
        rgb(0, 0, 0)
        detect_package()

    # ----------------------------------------------------
    # TEST button - edge triggered
    # ----------------------------------------------------

    test_btn = mcp_input_low(BTN_TEST)

    if test_btn and not last_test_btn:
        wait_button(BTN_TEST)

        pkg, pkg_map = detect_package()
        volt = detect_voltage()
        chip = CHIPS[selected]
        mode = test_modes[selected_mode]

        if mode == "Info":
            oled_info(chip)

            while True:
                if mcp_input_low(BTN_TEST):
                    wait_button(BTN_TEST)
                    show_status()
                    break

                time.sleep_ms(20)

            last_test_btn = False
            continue

        if pkg is None:
            print("ERROR: No package selected")
            oled_error("NO PACKAGE")
            fail_feedback()
            detect_package()
            last_pkg = None
            last_test_btn = False
            continue

        if volt == "OFF":
            print("ERROR: Voltage is OFF")
            oled_error("NO POWER")
            fail_feedback()
            detect_package()
            last_pkg = None
            last_test_btn = False
            continue

        if pkg != chip["pins"]:
            print("ERROR: Wrong package selected")
            print("Selected package: {}-pin".format(pkg))
            print("Chip requires:    {}-pin".format(chip["pins"]))

            oled_error("WRONG PKG")
            fail_feedback()

            detect_package()
            last_pkg = None
            last_test_btn = False
            continue

        current_map = pkg_map

        oled_running(chip, mode)

        print("Running test:", chip["name"])
        running_feedback()

        all_zif_inputs()

        if mode == "Quick":
            result = chip["test"]()

        elif mode == "Full":
            result = True

            for i in range(5):
                print("Full pass {}/5".format(i + 1))

                if not chip["test"]():
                    result = False
                    break

        elif mode.startswith("Soak"):
            result = True
            passes = 0

            if mode == "Soak 50":
                target = 50
            elif mode == "Soak 500":
                target = 500
            else:
                target = None   # unlimited

            while True:
                passes += 1
                print("Soak pass", passes)

                if not chip["test"]():
                    result = False
                    break

                oled_soak(chip, passes, target)

                if target is not None and passes >= target:
                    result = True
                    break

                if mcp_input_low(BTN_TEST):
                    wait_button(BTN_TEST)
                    result = True
                    break

        else:
            print("ERROR: Unknown test mode:", mode)
            oled_error("BAD MODE")
            result = False

        all_zif_inputs()

        if result:
            session_pass += 1
            stats["lifetime_pass"] += 1
            stats["last_result"] = "PASS"
            stats["last_ic"] = chip["name"]

            save_stats()

            print("RESULT: PASS")
            print_stats()

            oled_result(chip, True)
            pass_feedback()

        else:
            session_fail += 1
            stats["lifetime_fail"] += 1
            stats["last_result"] = "FAIL"
            stats["last_ic"] = chip["name"]

            save_stats()

            print("RESULT: FAIL")
            print_stats()

            oled_result(chip, False)
            fail_feedback()

        # Keep result on OLED. Press TEST once more to return to menu.
        wait_button(BTN_TEST)
        show_status()

        detect_package()
        last_pkg = None
        last_test_btn = False
        continue

    last_test_btn = test_btn

    # ----------------------------------------------------
    # Rotary encoder - A falling edge version
    # ----------------------------------------------------

    sw = enc_sw.value()

    if sw == 0 and last_enc_sw == 1:
        time.sleep_ms(40)

        if enc_sw.value() == 0:
            selected_field = (selected_field + 1) % 3
            show_status()
            beep(30)

            while enc_sw.value() == 0:
                time.sleep_ms(20)

            time.sleep_ms(15)

    last_enc_sw = sw

    # ----------------------------------------------------
    # Rotary encoder - simple reliable version
    # ----------------------------------------------------

    a = enc_a.value()

    if last_enc_a == 1 and a == 0:
        if enc_b.value() == 0:
            direction = 1
        else:
            direction = -1

        if selected_field == 0:
            selected = (selected + direction) % len(CHIPS)
        elif selected_field == 1:
            selected_family = (selected_family + direction) % len(families)
        elif selected_field == 2:
            selected_mode = (selected_mode + direction) % len(test_modes)

        oled_main(
            CHIPS[selected],
            families[selected_family],
            test_modes[selected_mode],
            pkg,
            volt,
            selected_field
        )

        # Force terminal status refresh when menu choice changes.
        last_selected = None

        time.sleep_ms(2)

    last_enc_a = a
    
# ============================================================
# End of File
# ============================================================