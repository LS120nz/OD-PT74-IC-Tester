# Pico 74xx IC Tester Overview

## Introduction

The Pico 74xx IC Tester is an open-source bench instrument designed to verify the functionality of standard 74xx-series digital logic integrated circuits.

Built around the Raspberry Pi Pico (RP2040), the tester provides a dedicated hardware platform with modular MicroPython firmware, allowing common logic devices to be tested quickly and consistently without requiring external test equipment.

The project is intended for electronics enthusiasts, retro-computing hobbyists, educators, repair technicians, and anyone working with TTL or CMOS logic devices.

---

## Project Goals

The primary objectives of the project are:

* Provide a simple, reliable tester for common 74xx logic ICs.
* Support the most widely used DIP package formats.
* Deliver consistent and repeatable functional testing.
* Present an intuitive user interface suitable for bench use.
* Maintain an open, modular architecture that is easy to extend.
* Encourage community contributions for additional IC definitions.

---

## Rev-B Design Scope

Rev-B is designed specifically for testing standard logic devices using conventional pin assignments.

Supported device families include:

* 74LS
* 74HC
* 74HCT
* Selected compatible 74xx logic families

Supported package sizes are:

* 14-pin DIP
* 16-pin DIP
* 20-pin DIP

The Rev-B hardware assumes conventional power pin locations used by the majority of standard 74xx devices.

Devices requiring non-standard power arrangements, external adapters, analogue measurements, or specialised timing analysis are intentionally outside the scope of this revision.

---

## Hardware Overview

The tester consists of a dedicated hardware platform featuring:

* Raspberry Pi Pico (RP2040)
* 20-pin ZIF socket
* OLED graphical display
* MCP23017 I/O expander
* Rotary encoder navigation
* TEST and NEXT push buttons
* DUT voltage selection (3.3 V / OFF / 5 V)
* RGB status LED
* Audible buzzer

The hardware has been designed for robustness, ease of assembly, and reliable bench operation.

---

## Firmware Overview

The firmware is written in MicroPython using a modular architecture.

Major software components include:

* Hardware abstraction layer
* Display driver
* Menu system
* IC definition library
* Test engine
* Self-test routines
* Diagnostic utilities

Separating IC definitions from the test engine allows new devices to be added without modifying the core firmware.

---

## Testing Philosophy

The objective of the tester is to verify the logical behaviour of supported integrated circuits rather than perform exhaustive electrical characterisation.

Available test modes include:

* Quick Test
* Full Functional Test
* Soak Test (50, 500, or Continuous cycles)

Each device is exercised using predefined test vectors appropriate to its logical function.

---

## Current Status

Rev-B represents the current production hardware and is considered feature complete.

Development is now focused on:

* expanding the verified IC library
* firmware refinement
* documentation improvements
* community contributions

---

## Future Development

Future work will continue under the Rev-C Logic IC Diagnostic Analyzer project.

Planned capabilities include:

* Support for larger package formats
* Adapter-based device testing
* Non-standard power pin configurations
* Advanced timing analysis
* Oscilloscope-style diagnostic tools
* Enhanced device characterisation

These features are intentionally outside the design scope of Rev-B to keep the platform simple, reliable, and focused on testing the most commonly encountered 74xx logic devices.

---

## Repository Documentation

Additional information is available throughout the repository:

* README – project introduction and quick start
* Getting Started – assembly and first use
* Build Guide – hardware construction
* Usage Guide – operating instructions
* Supported ICs – verified device list
* Troubleshooting – common problems and solutions
* CHANGELOG – project revision history

Refer to these documents for detailed instructions and technical reference material.




