# Pico 74xx IC Tester
An open-source bench instrument for testing classic 74xx logic ICs.
![Pico 74xx IC Tester](images/RevB-Case-top.jpg)
*Rev B hardware assembled in the first 3D printed enclosure.*
---

| Feature | Value |
|---------|-------|
| MCU | Raspberry Pi Pico (RP2040) |
| IC Packages | 14, 16, 20-pin DIP |
| Display | 128×64 OLED |
| Test Modes | Quick, Full, Soak |
| Voltage | 3.3 V / 5 V |
| Interface | Rotary encoder + buttons |
| Firmware | MicroPython |
| License | MIT / CERN-OHL-S |
---

![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)
![Hardware: CERN-OHL-S](https://img.shields.io/badge/Hardware-CERN--OHL--S-orange.svg)

A Raspberry Pi Pico based tester for 74xx-series logic ICs.

Designed as a practical bench instrument for testing 74LS, 74HC, 74HCT and compatible logic devices used in retro-computing, repair, and electronics projects. The tester supports 14-pin, 16-pin and 20-pin DIP devices, automatic package detection, OLED status display, and a growing library of validated IC tests.

## Rev-B Scope

Rev-B focuses on common 74LS, 74HC, 74HCT and some 74LVC logic devices using standard 14-pin, 16-pin and 20-pin DIP packages with conventional power pin assignments.

More specialised devices, non-standard power pin arrangements, adapter-based devices and advanced diagnostic functions are planned for the future Rev-C Logic IC Diagnostic Analyzer.

## Project Highlights

- Raspberry Pi Pico (RP2040) based logic IC tester
- Supports 14, 16 and 20-pin DIP 74xx devices
- 40+ verified IC definitions
- Quick, Full and Soak testing modes
- Power-On Self Test (POST)
- OLED user interface with rotary encoder
- Fully open-source hardware and firmware

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

## Hardware Overview

Rev B hardware has been assembled and successfully brought up.

Rev A served as the proof-of-concept platform, while Rev B introduces the production-style hardware, integrated enclosure, 
improved user interface, and expanded firmware.

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

## Project Status

**Status:** Stable Release (Rev-B)

## Current Release: Rev-B v1.0.0

### Firmware Status

- Stable modular firmware architecture
- Menu-driven user interface
- OLED display and diagnostics operational
- Quick, Full and Soak test modes implemented
- Ongoing expansion of the verified IC library

### Hardware Status

- Rev A: Proof-of-concept platform completed
- Rev B: Production hardware validated
- Enclosure: First production design completed
- Firmware: Stable and operational
- IC library: Ongoing validation and expansion
  
## Firmware Features

### Core Features Verified

- Modular two-board architecture
- Separate user-interface board for improved ergonomics and future upgrades
- Power-On Self Test (POST)
- MCP23017 detection
- SSD1306 OLED detection
- I²C bus diagnostics
- Package detection (14, 16, 20 pin)
- DUT voltage detection (3.3V / 5V)
- Rotary encoder navigation
- Quick test mode
- Full test mode
- Soak 50 mode
- Soak 500 mode
- Soak Infinite mode
- OLED status and error screens
- Wrong package detection and warning
- Serial terminal diagnostics

## Test Modes

- Quick Test
- Full Functional Test
- Soak 50
- Soak 500
- Continuous Soak
- Power-On Self Test (POST)
  
### Notes

The tester performs a Power-On Self Test (POST) during startup and reports:

- I²C devices detected
- MCP23017 status
- OLED status
- Selected package size
- DUT voltage selection
- TEST button state
  
Results are displayed on both the serial terminal and OLED display.

## Ongoing Validation

The Rev-B platform is feature complete.

Current work focuses on expanding the verified IC library through hardware validation and community contributions.

- Validate additional 74LS devices
- Validate remaining supported HC devices
- Continue expanding the supported IC database

## Community Contributions

Additional IC test definitions are welcome.

If you implement support for a new device, please include:

- Test source code
- Pin mapping
- Hardware validation
- Quick / Full / Soak results

Verified contributions will be considered for future releases.

## Getting Started

1. Build the Rev-B hardware.
2. Install MicroPython on the Raspberry Pi Pico.
3. Copy `main.py` to the Pico.
4. Power on the tester.
5. Select the IC package size, insert the device, and press **TEST**.
   
## Documentation
The Rev-B platform is feature complete. Ongoing work focuses on expanding the verified IC library and maintaining the firmware, while advanced diagnostic features are planned for the separate Rev-C project.

- [Build Guide](docs/build-guide.md)
- [Usage Guide](docs/usage-guide.md)
- [Supported ICs](docs/supported-ics.md)
- [Bring-up Checklist](docs/bringup-checklist.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Rev B Roadmap](docs/rev-b-roadmap.md)


## Project Evolution

- **Rev A** — Prove the electronics and firmware.
- **Rev B** — Build a polished, practical bench instrument.

## Future Development

Rev-B will continue to receive verified IC definitions and maintenance updates.

Development of advanced diagnostic features will continue in the separate **Logic IC Diagnostic Analyzer (Rev-C)** project.

## Repository Structure

```
hardware/
├── revA/
└── revB/

firmware/
└── revB/

docs/
```

## License

Hardware licensed under **CERN-OHL-S v2**.

Firmware and documentation licensed under the **MIT License**.

## Acknowledgements

Developed by **Otter Designs**, New Zealand.

Inspired by the retro-computing, electronics repair, and open-source hardware communities.

Special thanks to everyone who tests devices, reports issues, and contributes new IC definitions.

---

**If you build one, we'd love to see it! Feel free to share photos, improvements, and additional verified IC definitions through GitHub.**
