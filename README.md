# Pico 74xx IC Tester
![Pico 74xx IC Tester](images/RevB-Case-top.jpg)
*Rev B hardware assembled in the first 3D printed enclosure.*
---
![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)
![Hardware: CERN-OHL-S](https://img.shields.io/badge/Hardware-CERN--OHL--S-orange.svg)

A Raspberry Pi Pico based tester for 74xx-series logic ICs.

Designed as a practical bench instrument for testing 74LS, 74HC, 74HCT and compatible logic devices used in retro-computing, repair, and electronics projects. The tester supports 14-pin, 16-pin and 20-pin DIP devices, automatic package detection, OLED status display, and a growing library of validated IC tests.

## Rev-B Scope

Rev-B focuses on common 74LS, 74HC, 74HCT and some 74LVC logic devices using standard 14-pin, 16-pin and 20-pin DIP packages with conventional power pin assignments.

More specialised devices, non-standard power pin arrangements, adapter-based devices and advanced diagnostic functions are planned for the future Rev-C Logic IC Diagnostic Analyzer.

## Features

- Tests common 14-pin, 16-pin, and 20-pin 74xx logic ICs
- Raspberry Pi Pico / RP2040 based
- 20-pin ZIF socket
- 3.3V / OFF / 5V DUT voltage selector
- 14 / 16 / 20-pin package selector
- GPIO protection using series resistors and clamp diodes
- MCP23017 I/O expander for buttons, switch sensing, RGB LED, and buzzer
- USB terminal output
- SSD1306 128×64 OLED display

## Current Status

Rev B hardware has been assembled and successfully brought up.

Rev A served as the proof-of-concept platform, while Rev B introduces the production-style hardware, integrated enclosure, improved user interface, and expanded firmware.

### Verified Hardware

- RP2040 Pico controller
- MCP23017 I/O expander
- 20-pin ZIF socket interface
- 14-pin, 16-pin and 20-pin package support
- 3.3V / OFF / 5V DUT voltage selection
- SSD1306 128×64 OLED display
- Rotary encoder interface
- TEST and NEXT pushbuttons
- RGB status LED
- Buzzer
- Shared I²C bus (MCP23017 + OLED)

### Supported Device Categories

Current firmware includes support for
- logic gates
- decoders
- counters
- registers
- latches
- buffers
- shift registers
- Individual device validation is ongoing.

## Project Status

**Status:** Active Development

## Current Release: Rev-B.1 v0.2.0.

### Firmware Status

- Core framework stable
- Menu system operational
- OLED interface operational
- IC library under continuous expansion
  
-------------------------------

### Hardware Status

* Rev A: Hardware validated
* Rev B: Hardware assembled and operational
* Firmware: Stable core framework complete
* IC library: Continuing expansion and validation

Future advanced development is planned under the **Logic IC Diagnostic Analyzer** project.

## Rev-B.1 Firmware Status

### Core Features Verified

+ Modular two-board architecture
+ Separate user-interface board for improved ergonomics and future upgrades
* Power-On Self Test (POST)
* MCP23017 detection
* SSD1306 OLED detection
* I²C bus diagnostics
* Package detection (14, 16, 20 pin)
* DUT voltage detection (3.3V / 5V)
* Rotary encoder navigation
* Quick test mode
* Full test mode
* Soak 50 mode
* Soak 500 mode
* Soak Infinite mode
* OLED status and error screens
* Wrong package detection and warning
* Serial terminal diagnostics

### Notes

The tester performs a Power-On Self Test (POST) during startup and reports:

* I²C devices detected
* MCP23017 status
* OLED status
* Selected package size
* DUT voltage selection
* TEST button state

Results are displayed on both the serial terminal and OLED display.

### Remaining Development

- Validate additional 74LS devices
- Validate remaining supported HC devices
- Continue expanding the supported IC database
- Refine OLED user interface


## Documentation

- [Build Guide](docs/build-guide.md)
- [Usage Guide](docs/usage-guide.md)
- [Supported ICs](docs/supported-ics.md)
- [Bring-up Checklist](docs/bringup-checklist.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Rev B Roadmap](docs/rev-b-roadmap.md)

## Hardware

See:

```text
hardware/revA/
hardware/revB/
```

Hardware: CERN-OHL-S v2

Firmware/docs: MIT

---
