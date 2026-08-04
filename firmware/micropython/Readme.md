# Firmware

This directory contains the firmware for the **OD-PT74 Pico 74xx Logic IC Tester**.

## Supported Hardware

- Hardware Revision: Rev-C
- Firmware Version: v1.0.0

## Files

| File | Description |
|------|-------------|
| `main.py` | Main OD-PT74 application firmware |
| `ssd1306.py` | SSD1306 OLED display driver |

## Installation

1. Install MicroPython on the Raspberry Pi Pico.
2. Copy `main.py` to the Pico.
3. Copy `ssd1306.py` to the Pico.
4. Reboot the Pico.

The firmware will start automatically.

## Notes

This firmware is intended for the Rev-C OD-PT74 hardware.

*Copyright © 2026 Otter Designs*

OD-PT74 Firmware v1.0.0