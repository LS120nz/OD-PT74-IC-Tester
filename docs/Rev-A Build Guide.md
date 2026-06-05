# Overview

The Pico 74xx IC Tester is a Raspberry Pi Pico-based bench instrument designed to test common 74xx-series logic ICs used in retro-computing, repair, and electronics projects.

Rev A was developed as the initial proof-of-concept hardware platform to validate the tester architecture, firmware framework, user interface, and device test routines.

The primary goals of Rev A were:

* Validate RP2040 GPIO control of DUT (Device Under Test) pins
* Validate MCP23017 I/O expander integration
* Verify 14-pin, 16-pin, and 20-pin IC support
* Validate 3.3V and 5V DUT operation
* Test OLED display integration
* Test rotary encoder user interface
* Develop and validate device-specific IC test routines
* Establish a hardware platform for future revisions

Rev A successfully achieved these objectives and has been validated using a range of logic gates, counters, latches, registers, decoders, and shift-register devices.

The lessons learned during Rev A development directly led to the design of Rev B, which introduces self-powered operation, improved front-panel ergonomics, a two-board architecture, and expanded firmware capabilities.

This guide documents the assembly, bring-up, validation, and known issues of the Rev A hardware.


## Bill of Materials (BOM)

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
| 01 | 2N3904           |

### Connectors

| Qty | Part |
|-----|------|
| 2 | Pico header |
| 1 | OLED header |
| 1 | IC Power connector and jumper|
| 1 | IC sence connector and jumper|
| 1 | selector connector |


##3. Assembly Order
---
1. Resistors
2. Diodes
3. Capacitors
4. MCP23017 socket
5. Headers
6. OLED header
7. Buttons
8. ZIF/Dip socket
9. Pico

##4. First Power-Up
---
10. Check 3.3V
then Check 5V
and Check for no shorts

##5. Bring-Up Procedure
---
Flash firmware
Check serial terminal
Verify MCP23017
Verify OLED
Verify buttons
Verify encoder
Verify RGB LED
Verify buzzer

##6. Known Rev A Issues
--
OLED SDA/SCL originally routed incorrectly
BAT54S orientation correction
1k resistor update
74163 test routine issue

##7. Validation Results
---
74HC00 PASS
74HC02 PASS
74HC03 PASS
...
74HC595 PASS

##8. Rev A Lessons Learned
---
Need self-powered operation
Need better front-panel ergonomics
Need modular UI board
Need improved OLED integration
