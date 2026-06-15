# Changelog

## v0.1.0 - Rev A Validated

### Hardware

* Initial Rev A hardware completed
* RP2040 Pico controller
* MCP23017 I/O expander
* 20-pin ZIF socket
* 14/16/20 pin package support
* OLED display support
* Rotary encoder support
* RGB LED support
* Buzzer support

### Firmware

* Interactive IC selection
* Package auto-detection
* Voltage selection support
* Initial 74xx device library

### Validation

* Logic gates verified
* Decoders verified
* Counters verified
* Registers verified
* Latches verified
* Shift registers verified

### Documentation

* Initial project documentation
* Build guide
* Usage guide
* Supported IC database
* Rev B roadmap

===================

# Rev-B.1 Stable

## Added

* Power-On Self Test (POST)
* OLED POST status screen
* Full test mode
* Soak 50 mode
* Soak 500 mode
* Soak Infinite mode
* OLED error display support

## Fixed

* 7403 open collector NAND test
* 74139 decoder test
* 74163 counter test
* 7414 inverter timing responsiveness
* TEST button startup handling
* Package mismatch handling

## Verified

* OLED display operation
* MCP23017 operation
* Encoder navigation
* Package detection
* Voltage detection
* Quick, Full and Soak modes

### Rev-B.1 Validation Update

Additional real-hardware validation completed:

check - Supported-ics.md

**Old SN74LS157: suspect/faulty, enable/input loading issue
- New TI SN74LS157N: PASS
- Added and verified 74LS74 dual D flip-flop test
- 
These devices passed Quick, Full and Soak testing, confirming compatibility with the 74LS logic family.
### Rev-B.2 Statistics Update

For Rev-B.2:

1. Session counters
2. Lifetime counters (stats.json)
3. Statistics screen
4. Reset statistics option
