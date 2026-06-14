# Pico Tester Firmware

Firmware files for the Pico 74xx IC Tester.

## File List

### Rev-A

**main.py**

Final Rev-A firmware release.

Features:

* Basic IC testing
* OLED support
* MCP23017 support
* Rotary encoder navigation
* Package and voltage detection

---

### Rev-B

**main_rev_b1_stable.py**

Current stable firmware release.

Features:

* Power-On Self Test (POST)
* I²C device diagnostics
* OLED status and error screens
* Package detection (14/16/20 pin)
* DUT voltage detection (3.3V / 5V)
* Quick test mode
* Full test mode
* Soak 50 mode
* Soak 500 mode
* Soak Infinite mode
* Improved IC validation routines

Status:

* Stable
* Active development continues with additional IC support and validation

---

## Notes

* Rev-A firmware is retained for reference.
* Rev-B.1 Stable is the recommended firmware for current hardware.
* Future development will continue from the Rev-B firmware branch.
