# Rev A Bill of Materials

## Core Components

| Ref | Part | Qty | Notes |
|---|---|---:|---|
| U2 | Raspberry Pi Pico | 1 | RP2040 module |
| U1 | MCP23017 | 1 | I2C GPIO expander |
| D1-D20 | BAT54S | 20 | GPIO clamp protection |
| Q1 | 2N3904 | 1 | Buzzer driver |
| BZ1 | 1407 passive piezo buzzer | 1 | Passive type |

---

## User Interface

| Ref | Part | Qty | Notes |
|---|---|---:|---|
| SW1 | 2P3T rotary/package switch | 1 | 14/16/20-pin select |
| SW3 | DP3T ON-OFF-ON switch | 1 | 3.3V/OFF/5V |
| SW4 | Pushbutton | 1 | NEXT |
| SW5 | Pushbutton | 1 | TEST |
| D1 | RGB LED | 1 | Common cathode |

---

## Socket

| Ref | Part | Qty | Notes |
|---|---|---:|---|
| ZIF1 | 20-pin ZIF socket | 1 | DIP socket |

---

## Passives

| Value | Qty | Notes |
|---|---:|---|
| 4.7k resistor | 22 | GPIO protection |
| 2.2k resistor | 1 | Base resistor |
| 100k resistor | 1 | Pulldown |
| 330R resistor | 3 | RGB LED |
| 10k resistor | 1 | Reset Pullup |
| 100nF capacitor | 4 | Decoupling |
| 10uF capacitor | 1 | Bulk filtering |

---

## Optional

| Part | Qty | Notes |
|---|---:|---|
| SSD1306 OLED | 1 | I2C display |
