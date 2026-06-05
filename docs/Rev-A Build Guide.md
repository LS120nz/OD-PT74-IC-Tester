# Overview

The Pico 74xx IC Tester is a Raspberry Pi Pico-based bench instrument designed to test common 74xx-series logic ICs used in retro-computing, repair, and electronics projects.

Rev A was developed as the initial proof-of-concept hardware platform to validate the tester architecture, firmware framework, user interface, and device test routines.

The primary goals of Rev A were:

* Validate RP2040 GPIO control of DUT (Device Under Test) pins
* Validate MCP23017 I/O expander integration
* Verify 14-pin, 16-pin, and 20-pin IC support
* Validate 3.3V and 5V DUT operation
* Test rotary encoder user interface
* Develop and validate device-specific IC test routines
* Establish a hardware platform for future revisions

Rev A successfully achieved these objectives and has been validated using a range of logic gates, counters, latches, registers, decoders, and shift-register devices.

The lessons learned during Rev A development directly led to the design of Rev B, which introduces self-powered operation, improved front-panel ergonomics, a two-board architecture, and expanded firmware capabilities.

This guide documents the assembly, bring-up, validation, and known issues of the Rev A hardware.

## Hardware Revision
---
Revision: Rev A
Board Version: v0.1
Status: Validated

##1. Bill of Materials (BOM)
---

### Major Components

| Qty | Part | Notes |
|-----|------|-------|
| 1 | Raspberry Pi Pico | RP2040 module |
| 1 | MCP23017 | I²C I/O expander |
| 1 | 20-pin Dip socket | DUT socket |
| 2 | Pushbuttons | TEST / NEXT |
| 1 | RGB LED | Status indicator |
| 1 | Active buzzer | Audible feedback |

### Passive Components

| Qty | Part            |
|-----|-----------------|
| 22 | 4.7k resistors   |
| 03 | 10k resistors    |
| 09 | 100nF capacitors |
| 04 | 330R resistors   |
| 01 | 10R resistors    |
| 01 | 2N3904 NPN transistor          |

### Connectors

| Qty | Part |
|-----|------|
| 2 | Pico header |
| 1 | OLED header |
| 1 | IC Power connector and jumper|
| 1 | IC sense connector and jumper|
| 1 | selector connector |


##2. Assembly Order
---
1. Resistors
2. Diodes
3. Capacitors
4. MCP23017 socket
5. Headers
6. Buttons
7. OLED header
9. ZIF/Dip socket
10. Pico

### Assembly Notes

- Inspect all resistor values before soldering.
- Verify BAT54S diode orientation carefully.
- Ensure MCP23017 pin 1 orientation is correct.
- Verify OLED header pinout before connecting display.
- Install the ZIF socket last to provide the best access to surrounding components.
- Fit the Pico only after all soldering and continuity checks have been completed.

##3. Pre-Power Checks
---
- Check for shorts between 3.3V and GND
- Check for shorts between 5V and GND
- Verify MCP23017 orientation
- Verify Pico orientation
- Verify OLED header orientation
- Verify DUT voltage switch operation

##4. Bring-Up Procedure
---

### A. Flash Firmware

- Connect the Pico via USB.
- Install the latest firmware.
- Open a serial terminal.

### B. Verify Serial Output

Expected:

Pico 74xx Tester
Firmware Version: x.x.x

- Confirm the firmware starts correctly.
- Confirm no startup errors are reported.

### C. Verify MCP23017

Run the I²C scan.

Expected:

I2C scan: ['0x20']

- MCP23017 should appear at address 0x20.

### D. Verify Buttons

Test:

- TEST button
- NEXT button

Expected:

Button presses detected correctly.

### E. Verify Rotary Encoder

Test:

- Clockwise rotation
- Counter-clockwise rotation
- Encoder push switch

Expected:

Selections change correctly and push-switch is detected.

### F. Verify RGB Status LED

Test:

- Red
- Green
- Blue

Expected:

Each colour illuminates correctly.

### G. Verify Buzzer

Run buzzer test.

Expected:

Audible tone is generated.

### H. Verify DUT Voltage Switching

Check:

- OFF position
- 3.3V position
- 5V position

Measure DUT VCC with a multimeter.

Expected:

OFF = 0V
3.3V = approximately 3.3V
5V = approximately 5V

### I. Verify Known-Good IC

Insert a known-good 74HC02 or 74HC00.

Run the device test.

Expected:

PASS

##5. Known Rev A Issues
--
BAT54S clamp diode orientation corrected
ZIF series resistors changed to 1kΩ
I²C reassigned to GPIO26/GPIO27
74163 test routine required additional validation
OLED SDA/SCL routing corrected during bring-up

##6. Validation Results
---
See supported-ics.md for the complete validated device list.

##7. Rev A Lessons Learned
---
Need self-powered operation
Need better front-panel ergonomics
Need modular UI board
Need improved OLED integration

##9. Validation Complete
---

Rev A bring-up is considered successful when:
- MCP23017 is detected
- Buttons function correctly
- Encoder functions correctly
- RGB LED functions correctly
- Buzzer functions correctly
- DUT voltage switching functions correctly
- At least one known-good IC passes testing

## Post Bring-Up Improvements

Following successful Rev A validation, the following enhancements were added:

- SSD1306 128x64 OLED display
- Shared I²C bus operation (MCP23017 + OLED)
- OLED status and test output
- Additional device test routines
- Rotary encoder menu system
- 
