# Pico Tester Firmware

Firmware files for the Pico 74xx IC Tester.

## File List

# Firmware Versions

## Rev-A

**main.py**

Final Rev-A firmware release.

Features:

- USB terminal interface
- IC test framework
- MCP23017 support
- Basic user interface

---

## Rev-B1 & B1a

**main_rev_b1a.py**

Major user-interface update.

Features:

- SSD1306 OLED support
- Power-On Self Test (POST)
- Rotary encoder menu
- Quick / Full / Soak test modes
- Improved IC selection
- Improved diagnostics

---

## Rev-B2

**main_rev_b2.py**

Statistics and record-keeping release.

Features:

- Session PASS counter
- Session FAIL counter
- Lifetime PASS counter
- Lifetime FAIL counter
- Last tested device record
- Persistent stats.json storage
- OLED result statistics display

---

Current recommended version:

**Rev-B2**

## Notes

* Rev-A firmware is retained for reference.
* Rev-B.1 Stable is the recommended firmware for current hardware.
* Future development will continue from the Rev-B firmware branch.
