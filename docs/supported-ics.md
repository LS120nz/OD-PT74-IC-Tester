# Supported ICs

## Rev-B Scope

Rev-B focuses on standard 74xx-series logic ICs using 14-pin, 16-pin, and 20-pin DIP packages with normal power pin arrangements.

More specialised devices, odd power-pin devices, adapter-based parts, and deeper diagnostic testing are being moved to the future Rev-C Logic IC Diagnostic Analyzer.

---

## Verified Devices

These devices have been tested on real hardware and are known to pass.

### 14-pin Devices

| IC      | Function                 | Status   | Notes           |
| ------- | ------------------------ | -------- | --------------- |
| 74HC00  | Quad 2-input NAND        | Verified |                 |
| 74LS00  | Quad 2-input NAND        | Verified |                 |
| 74HC02  | Quad 2-input NOR         | Verified |                 |
| 74LS02  | Quad 2-input NOR         | Verified |                 |
| 74HC03  | Quad 2-input NAND OC     | Verified |                 |
| 74LS04  | Hex inverter             | Verified | Faulty IC found |
| 74HC05  | Hex inverter OC          | Verified |                 |
| 74HC06  | Hex inverter / driver OC | Verified |                 |
| 74LS06  | Hex inverter / driver OC | Verified |                 |
| 74HC07  | Hex buffer / driver OC   | Verified |                 |
| 74LS07  | Hex buffer / driver OC   | Verified |                 |
| 74HC08  | Quad 2-input AND         | Verified |                 |
| 74HC10  | Triple 3-input NAND      | Verified |                 |
| 74LS11  | Triple 3-input AND       | Verified | Faulty IC found |
| 74HC14  | Hex Schmitt inverter     | Verified |                 |
| 74HC21  | Dual 4-input AND         | Verified |                 |
| 74LS27  | Triple 3-input NOR       | Verified |                 |
| 74HC30  | 8-input NAND             | Verified |                 |
| 74HC32  | Quad 2-input OR          | Verified |                 |
| 74LS32  | Quad 2-input OR          | Verified |                 |
| 74LS74  | Dual D flip-flop         | Verified |                 |
| 74LS86  | Quad 2-input XOR         | Verified |                 |
| 74HC125 | Quad tri-state buffer    | Verified |                 |
| 74HC126 | Quad tri-state buffer    | Verified |                 |
| 74HC132 | Quad Schmitt NAND        | Verified |                 |
| 74HC164 | 8-bit shift register     | Verified |                 |
| 74HC393 | Dual binary counter      | Verified |                 |

### 16-pin Devices

| IC      | Function                              | Status   | Notes           |
| ------- | ------------------------------------- | -------- | --------------- |
| 74HC138 | 3-to-8 decoder                        | Verified |                 |
| 74HC139 | Dual 2-to-4 decoder                   | Verified |                 |
| 74LS139 | Dual 2-to-4 decoder                   | Failed   | Faulty IC found |
| 74LS151 | 8-input digital multiplexer           | Verified |                 |
| 74LS153 | Dual 4-input multiplexer              | Verified |                 |
| 74LS157 | Quad 2:1 multiplexer                  | Verified | TI ICs verified |
| 74LS161 | 4-bit synchronous binary counter      | Verified |                 |
| 74HC163 | 4-bit counter                         | Verified | Faulty IC found |
| 74HC165 | 8-bit PISO shift register             | Verified |                 |
| 74HC174 | Hex D flip-flop                       | Verified |                 |
| 74LS194 | 4-bit bidirectional shift register    | Verified |                 |
| 74HC595 | Serial-in parallel-out shift register | Verified |                 |
| 74LS85  | 4-bit magnitude comparator            | Verified |                 |

### 20-pin Devices

| IC      | Function              | Status   | Notes           |
| ------- | --------------------- | -------- | --------------- |
| 74HC244 | Octal buffer          | Verified | Faulty IC found |
| 74HC245 | Octal bus transceiver | Verified |                 |
| 74HC273 | Octal D flip-flop     | Verified |                 |
| 74HC373 | Octal latch           | Verified |                 |
| 74HC374 | Octal D flip-flop     | Verified |                 |
| 74HC573 | Octal latch           | Verified |                 |
| 74HC574 | Octal D flip-flop     | Verified |                 |

### LVC Devices

| IC       | Function              | Status             | Notes             |
| -------- | --------------------- | ------------------ | ----------------- |
| 74LVC245 | Octal bus transceiver | Pending Validation | Test at 3.3V only |

---

## Not Yet Tested / No IC Available

Firmware support may exist, but these have not yet been validated on physical ICs.

| IC      | Function             | Status |
| ------- | -------------------- | ------ |
| 74HC04  | Hex inverter         | No IC  |
| 74HC11  | Triple 3-input AND   | No IC  |
| 74HC27  | Triple 3-input NOR   | No IC  |
| 74HC74  | Dual D flip-flop     | No IC  |
| 74HC86  | Quad 2-input XOR     | No IC  |
| 74HC151 | 8-input multiplexer  | No IC  |
| 74HC153 | Dual 4-input mux     | No IC  |
| 74HC157 | Quad 2:1 multiplexer | No IC  |
| 74HC161 | 4-bit counter        | No IC  |
| 74HC194 | Shift register       | No IC  |

---

## Deferred to Rev-C

These devices are being moved to the future Rev-C Logic IC Diagnostic Analyzer because they need special handling, adapter support, odd power pins, or deeper debugging.

| IC      | Reason / Status                                   |
| ------- | ------------------------------------------------- |
| 74LS83  | Odd/special handling; full-adder testing deferred |
| 74LS90  | Deferred counter support                          |
| 74LS93  | Non-standard power pins; adapter candidate        |
| 74LS112 | Deferred JK flip-flop support                     |
| 74LS123 | Monostable timing device; deferred                |
| 74LS147 | Pinout/debug pending                              |
| 74LS148 | Test not verified; needs pinout debug             |
| 74LS160 | Suspect/fake batch; abnormal 5V behaviour         |
| 74LS190 | Deferred up/down counter support                  |
| 74LS191 | Loads correctly but does not count; debug pending |
| 74LS192 | Deferred up/down counter support                  |
| 74LS247 | 7-segment decoder/driver; deferred                |
| 74LS48  | 7-segment decoder/driver; deferred                |
| 7445    | BCD decoder/driver; deferred                      |
| 74LS80  | Special function device; deferred                 |
| CD4020  | 4000-series CMOS; Rev-C target                    |

---

## LVC Device Testing

74LVC devices must be tested with the DUT voltage selector set to **3.3V**.

The tester can be used to identify common counterfeit, damaged, or non-functional LVC devices by verifying:

* Logic functionality
* Output enable operation
* Tri-state behaviour
* Bus transceiver direction control
* Input/output operation
* Stuck-high and stuck-low faults

The tester performs functional validation only. It does not verify:

* Propagation delay
* Maximum operating frequency
* Output drive strength
* Leakage current
* Full datasheet compliance

---

## Validation Levels

* **Verified** = Tested on physical hardware and passes Quick, Full, and/or Soak testing.
* **Failed** = Physical device tested and failed; likely faulty IC or faulty batch.
* **Pending Validation** = Firmware support exists but physical validation is not complete.
* **No IC** = Firmware support may exist, but no physical IC was available for validation.
* **Deferred to Rev-C** = Not targeted for Rev-B; planned for future analyzer/adapter support.

---

## Community IC Contributions

Additional IC test contributions are welcome.

Please include:

* IC part number
* Device family
* Test function source code
* Pin mapping used
* Test methodology
* Hardware validation results
* Quick / Full / Soak test results
* Known limitations

Rev-B focuses on standard 74xx logic devices. More specialised devices and advanced diagnostic functions are planned for the Rev-C Logic IC Diagnostic Analyzer.
