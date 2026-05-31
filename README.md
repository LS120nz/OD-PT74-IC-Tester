# Pico 74xx IC Tester
![Pico 74xx IC Tester](images/assembled.jpg)
*Rev A prototype during hardware validation and firmware bring-up.*
---
![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)
![Hardware: CERN-OHL-S](https://img.shields.io/badge/Hardware-CERN--OHL--S-orange.svg)

A Raspberry Pi Pico based tester for 74xx-series logic ICs.

Designed as a practical bench instrument for testing 74LS, 74HC, 74HCT and compatible logic devices used in retro-computing, repair, and electronics projects. The tester supports 14-pin, 16-pin and 20-pin DIP devices, automatic package detection, OLED status display, and a growing library of validated IC tests.

## Features

- Tests common 14-pin, 16-pin, and 20-pin 74xx logic ICs
- Raspberry Pi Pico / RP2040 based
- 20-pin ZIF socket
- 3.3V / OFF / 5V DUT voltage selector
- 14 / 16 / 20-pin package selector
- GPIO protection using series resistors and clamp diodes
- MCP23017 I/O expander for buttons, switch sensing, RGB LED, and buzzer
- USB terminal output
- Optional OLED output

## Current Status

Rev A hardware has been assembled and validated.

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

### Verified IC Families

- Logic gates
- Decoders
- Counters
- Registers
- Latches
- Shift registers

### Status

Rev A validation complete.

## Rev B Development

Current work includes:

- Self-powered operation
- On-board 5V / 3.3V regulation
- OLED user interface
- Two-board mechanical design
- 3D printed enclosure
- Improved front-panel ergonomics
- enhanced selectable tests for ic's

## Documentation

- [Build Guide](docs/build-guide.md)
- [Usage Guide](docs/usage-guide.md)
- [Supported ICs](docs/supported-ics.md)
- [Bring-up Checklist](docs/bringup-checklist.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Rev B Roadmap](docs/rev-b-roadmap.md)

## Hardware
See:

---text
hardware/revA/

---

Hardware: CERN-OHL-S v2

Firmware/docs: MIT

---
