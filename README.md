# Pico 74xx IC Tester

![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)
![Hardware: CERN-OHL-S](https://img.shields.io/badge/Hardware-CERN--OHL--S-orange.svg)

A Raspberry Pi Pico-based tester for common 74xx-series DIP logic ICs.

This project was designed as a practical bench tool for checking suspect 74LS, 74HC, 74HCT, 74LVD, and related logic ICs used in retro computer and electronics projects.

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

## Current status

Rev A hardware has successfully passed initial 74HC02 NOR gate testing.

Confirmed working:
- RP2040 GPIO ↔ ZIF routing
- MCP23017 I2C interface
- 14-pin package mapping
- DUT voltage switching
- Logic test framework

Rev A bring-up fixes discovered:
- BAT54S clamp orientation corrected
- ZIF series resistors changed to 1k
- I2C moved to GPIO26/GPIO27
- V_OUT simplified to ZIF20
- Corrected 14-pin package mapping

Next steps:
- Validate additional 74xx IC families
- Complete Rev B schematic cleanup
- Add OLED support and expanded diagnostics

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
