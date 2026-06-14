# Supported ICs

## Verified Devices

These devices have been tested on real hardware and are known to pass.

### 14-pin Devices

| IC      | Function                 | Status   |
| ------- | ------------------------ | -------- |
| 74HC00  | Quad 2-input NAND        | Verified |
| 74HC02  | Quad 2-input NOR         | Verified |
| 74HC03  | Quad 2-input NAND OC     | Verified |
| 74HC05  | Hex inverter OC          | Verified |
| 74HC06  | Hex inverter / driver OC | Verified |
| 74HC07  | Hex buffer / driver OC   | Verified |
| 74HC10  | Triple 3-input NAND      | Verified |
| 74HC14  | Hex Schmitt inverter     | Verified |
| 74HC21  | Dual 4-input AND         | Verified |
| 74HC30  | 8-input NAND             | Verified |
| 74HC125 | Quad tri-state buffer    | Verified |
| 74HC126 | Quad tri-state buffer    | Verified |
| 74HC132 | Quad Schmitt NAND        | Verified |
| 74HC164 | 8-bit shift register     | Verified |
| 74HC393 | Dual binary counter      | Verified |

### 16-pin Devices

| IC      | Function                              | Status               |
| ------- | ------------------------------------- | -------------------- |
| 74HC138 | 3-to-8 decoder                        | Verified             |
| 74HC139 | Dual 2-to-4 decoder                   | Verified             |
| 74HC163 | 4-bit counter                         | Verified             |
| 74HC165 | 8-bit PISO shift register             | Verified             |
| 74HC174 | Hex D flip-flop                       | Verified             |
| 74HC595 | Serial-in parallel-out shift register | Verified             |

### 20-pin Devices

| IC      | Function              | Status   |
| ------- | --------------------- | -------- |
| 74HC244 | Octal buffer          | Verified |
| 74HC245 | Octal bus transceiver | Verified |
| 74HC273 | Octal D flip-flop     | Verified |
| 74HC373 | Octal latch           | Verified |
| 74HC374 | Octal D flip-flop     | Verified |
| 74HC573 | Octal latch           | Verified |
| 74HC574 | Octal D flip-flop     | Verified |

## Implemented but Not Yet Hardware Verified

| IC     | Function         |
| ------ | ---------------- |
| 74HC04 | Hex inverter     |
| 74HC08 | Quad 2-input AND |
| 74HC32 | Quad 2-input OR  |
| 74HC86 | Quad 2-input XOR |

## Planned Devices

| IC      | Function             |
| ------- | -------------------- |
| 74HC74  | Dual D flip-flop     |
| 74HC157 | Quad 2:1 multiplexer |

## Notes

* Verified devices have been tested on physical hardware.
* Implemented devices have firmware support but have not yet been validated with a physical IC.
* Additional 74LS, 74HCT and compatible devices will be added as testing continues.
