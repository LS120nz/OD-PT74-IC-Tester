# Project Milestones

## Current Release

Hardware: Rev-C
Firmware: v1.0.0
Status: Public Release

The OD-PT74 has progressed through three hardware revisions, culminating in the Rev-C production design.

### Verified Hardware

* RP2040 Pico controller
* MCP23017 I/O expander
* 20-pin ZIF socket interface
* 14-pin package support
* 16-pin package support
* 20-pin package support
* 3.3V / OFF / 5V DUT voltage selection
* Rotary encoder interface
* TEST and NEXT pushbuttons
* SSD1306 128×64 OLED display
* I²C bus shared between MCP23017 and OLED
* Fault detection and reporting
* Dual 5 V / 3.3 V power indicators

### Verified ICs

Refer to the *Supported ICs* Guide for the current list of validated devices.

### Validation Highlights

The tester has successfully identified defective ICs during validation testing, including:

* Faulty 74HC393 device detected and confirmed
* Incorrect 74163 test implementation identified during firmware validation
* Multiple pin-mapping and package-mapping issues corrected during bring-up

### Project Timeline

✅ Rev-A
Initial concept and functional prototype.

✅ Rev-B
Major redesign and feature validation.

✅ Rev-C
Production hardware.
Public GitHub release.
Documentation complete.
Firmware v1.0.0.

### Future Development

- Additional IC definitions
- Firmware enhancements
- Community contributions
- OD-ADU development

## Related Documentation

| Document | Description |
|----------|-------------|
| [🏠 Project Home](../../README.md) | Return to the main project page |
| [📖 Documentation Index](../README.md) | Documentation overview |
