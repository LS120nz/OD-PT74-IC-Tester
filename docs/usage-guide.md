# Pico 74xx IC Tester - User Guide

---

## Overview

The Pico 74xx IC Tester is a Raspberry Pi Pico-based bench tool for testing common DIP 74xx-series logic ICs.

The tester supports:

- 14-pin DIP logic ICs
- 16-pin DIP logic ICs
- 20-pin DIP logic ICs
- 3.3V and 5V logic families
- USB serial terminal output
- Optional OLED display output

The tester is intended for checking:

- 74HC series
- 74HCT series
- 74LS series
- compatible logic ICs

---

## Safety Notes

### Important

- Never insert or remove ICs while powered if possible.
- Always select the correct package size before testing.
- Always select the correct logic voltage before testing.
- Do not insert chips backwards.
- Do not test unknown ICs that may not be standard 74xx logic devices.

---

## Controls

### Package Selector

Selects the active power and ground pins for the ZIF socket.

| Position | Package |
|---|---|
| 0 | Off    |
| 1 | 14-pin |
| 2 | 16-pin |
| 3 | 20-pin |

The tester automatically detects the selected package.

---

### Voltage Selector

Selects DUT (Device Under Test) voltage.

| Position | Voltage |
|---|---|
| 1 | 3.3V |
| 2 | OFF |
| 3 | 5V |

The tester automatically detects the selected voltage.

---

### Buttons

#### NEXT

Cycles through supported IC types.
(check supported IC list)

#### TEST

Runs the currently selected IC test.
- Quick Test
- Full Test
- Soak 50
- Soak 100
- Soak Unlimited
- Check

---

## RGB LED Status

| LED State | Meaning |
|---|---|
| Red | 14-pin mode |
| Green | 16-pin mode |
| Blue | 20-pin mode |
| Blinking Yellow | Voltage OFF |
| White Flash | Test running |
| Green Blink | PASS |
| Red Blink | FAIL |

---

## ZIF Socket Usage

### Important

All ICs are inserted aligned to the top of the ZIF socket.

Pin 1 must always match the Pin 1 marking on the PCB.

---

### 14-pin IC placement

Insert the IC into the top 14 socket positions.

Example:

```text
Top of socket
┌─────────────┐
│ 14-pin IC   │
│■■■■■■■■■■■■■│
└─────────────┘
```
