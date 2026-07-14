# Changelog

All notable changes to the Pico 74xx IC Tester project are documented in this file.

The project follows a hardware revision (Rev-A, Rev-B, etc.) combined with semantic firmware versioning for public releases.

---

## Rev-B v1.0.0 — Initial Public Release

### Highlights

* First public release of the Rev-B hardware platform
* Stable MicroPython firmware
* Production enclosure completed
* Comprehensive project documentation
* Open-source hardware and firmware published on GitHub

### Added

#### Hardware

* Rev-B production PCB
* Raspberry Pi Pico (RP2040) controller
* MCP23017 I/O expander
* 20-pin ZIF socket
* 14-, 16- and 20-pin package support
* SSD1306 OLED display
* Rotary encoder navigation
* TEST and NEXT push buttons
* RGB status LED
* Audible buzzer
* 3.3 V / OFF / 5 V DUT power selection

#### Firmware

* Power-On Self Test (POST)
* Interactive menu system
* Automatic package detection
* DUT voltage detection
* Quick Test mode
* Full Functional Test mode
* Soak Test modes

  * 50 cycles
  * 500 cycles
  * Continuous
* OLED diagnostic messages
* USB serial diagnostics
* Modular IC definition library

### Improved

* Overall firmware stability
* Hardware diagnostics
* User interface responsiveness
* IC test framework
* Documentation and project structure

### Fixed

* 7403 open-collector NAND testing
* 74139 decoder verification
* 74163 counter verification
* 7414 inverter timing behaviour
* TEST button startup handling
* Package mismatch detection

### Validation

The following hardware functions have been verified:

* OLED display
* MCP23017 communication
* I²C bus
* Package detection
* DUT voltage selection
* Rotary encoder
* Quick Test mode
* Full Test mode
* Soak Test modes

Multiple 74LS devices have been validated on production Rev-B hardware using Quick, Full and Soak testing.

---

## Rev-A Development

Rev-A served as the proof-of-concept platform used during initial hardware and firmware development.

### Hardware

* Initial RP2040 platform
* MCP23017 interface
* OLED support
* Rotary encoder
* RGB LED
* Buzzer
* 20-pin ZIF socket

### Firmware

* Initial menu system
* Interactive IC selection
* Package detection
* Initial 74xx device library

### Validation

Early validation covered representative devices including:

* Logic gates
* Decoders
* Counters
* Registers
* Latches
* Shift registers

Rev-A successfully validated the overall hardware architecture and provided the foundation for the Rev-B production design.
