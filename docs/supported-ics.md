# Supported ICs

## Introduction

This document lists the logic ICs currently supported by the **Rev-B Pico 74xx IC Tester**.

Each device listed has either been validated on physical Rev-B hardware or is included in the firmware awaiting hardware verification.

The Rev-B platform focuses on standard **74xx-series logic ICs** in **14-pin, 16-pin, and 20-pin DIP packages** using conventional power pin arrangements.

---

## Validation summary

**Current Release:** Rev-B v1.0.0

> [!NOTE]
> **Validation Summary**
>
> - Supported packages: **14-, 16- and 20-pin DIP**
> - Supported families: **74LS, 74HC, 74HCT and selected 74LVC**
> - Verified devices: **48**
> - Pending validation: **10**

### Supported package sizes

* 14-pin DIP
* 16-pin DIP
* 20-pin DIP

### Supported logic families

* 74LS
* 74HC
* 74HCT
* Selected 74LVC devices operating at 3.3 V

### Validation status

- ✅ Physical hardware validation
- 🧪 Firmware implementation awaiting validation
- 📋 Outside the scope of Rev-B

---

## Validation levels

| Status                    | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| ✅ **Verified**           | Successfully tested on physical Rev-B hardware.                                             |
| ⚠ **Failed**              | Physical device tested but failed functional verification.                                  |
| 🧪 **Pending Validation** | Firmware support exists but physical validation has not yet been completed.                 |
| 📦 **No IC Available**    | Firmware support exists but a suitable device was not available for testing.                |
| 🚫 Not Supported          | Outside the design scope of the Rev-B Pico 74xx IC Tester.                                  |

A device is considered **Verified** only after successful testing on physical Rev-B hardware using one or more of the available test modes (Quick, Full, and Soak, where appropriate).

---

## Verified Devices

The following devices have been successfully validated on physical Rev-B hardware.

## 14-pin Devices

| IC      | Function                 | Status   | 
| ------- | ------------------------ | -------- | 
| 74HC00  | Quad 2-input NAND        | Verified | 
| 74LS00  | Quad 2-input NAND        | Verified | 
| 74HC02  | Quad 2-input NOR         | Verified | 
| 74LS02  | Quad 2-input NOR         | Verified | 
| 74HC03  | Quad 2-input NAND OC     | Verified | 
| 74LS04  | Hex inverter             | Verified | 
| 74HC05  | Hex inverter OC          | Verified | 
| 74HC06  | Hex inverter / driver OC | Verified | 
| 74LS06  | Hex inverter / driver OC | Verified | 
| 74HC07  | Hex buffer / driver OC   | Verified | 
| 74LS07  | Hex buffer / driver OC   | Verified | 
| 74HC08  | Quad 2-input AND         | Verified | 
| 74HC10  | Triple 3-input NAND      | Verified | 
| 74LS11  | Triple 3-input AND       | Verified | 
| 74HC14  | Hex Schmitt inverter     | Verified | 
| 74HC21  | Dual 4-input AND         | Verified | 
| 74LS27  | Triple 3-input NOR       | Verified | 
| 74HC30  | 8-input NAND             | Verified | 
| 74HC32  | Quad 2-input OR          | Verified | 
| 74LS32  | Quad 2-input OR          | Verified | 
| 74LS74  | Dual D flip-flop         | Verified | 
| 74LS86  | Quad 2-input XOR         | Verified | 
| 74HC125 | Quad tri-state buffer    | Verified | 
| 74HC126 | Quad tri-state buffer    | Verified | 
| 74HC132 | Quad Schmitt NAND        | Verified | 
| 74HC164 | 8-bit shift register     | Verified | 
| 74HC393 | Dual binary counter      | Verified | 

---

## 16-pin Devices

| IC      | Function                              | Status   |
| ------- | ------------------------------------- | -------- |
| 74LS85  | 4-bit magnitude comparator            | Verified | 
| 74HC138 | 3-to-8 decoder                        | Verified | 
| 74HC139 | Dual 2-to-4 decoder                   | Verified | 
| 74LS139 | Dual 2-to-4 decoder                   | Verified | 
| 74LS151 | 8-input digital multiplexer           | Verified | 
| 74LS153 | Dual 4-input multiplexer              | Verified | 
| 74LS157 | Quad 2:1 multiplexer                  | Verified | 
| 74LS161 | 4-bit synchronous binary counter      | Verified | 
| 74HC163 | 4-bit counter                         | Verified | 
| 74HC165 | 8-bit PISO shift register             | Verified | 
| 74HC174 | Hex D flip-flop                       | Verified | 
| 74LS194 | 4-bit bidirectional shift register    | Verified | 
| 74HC595 | Serial-in parallel-out shift register | Verified | 


---

## 20-pin Devices

| IC      | Function              | Status   | 
| ------- | --------------------- | -------- | 
| 74HC244 | Octal buffer          | Verified | 
| 74HC245 | Octal bus transceiver | Verified | 
| 74HC273 | Octal D flip-flop     | Verified | 
| 74HC373 | Octal latch           | Verified | 
| 74HC374 | Octal D flip-flop     | Verified | 
| 74HC573 | Octal latch           | Verified | 
| 74HC574 | Octal D flip-flop     | Verified | 


---

## 74LVC Devices

> [!IMPORTANT]
> All **74LVC** devices must be tested with the DUT voltage selector set to **3.3 V**.

| IC       | Function              | Status             | Notes             |
| -------- | --------------------- | ------------------ | ----------------- |
| 74LVC245 | Octal bus transceiver | Verified at 3.3V | Clean legs required |


---

# Pending Validation

The following devices are implemented in firmware but have not yet been validated on physical hardware.

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

# Notes on 74LVC devices

74LVC devices operate at **3.3 V** and require the tester's DUT voltage selector to be set accordingly.

Because of their lower operating voltage, poor socket contact or tarnished IC pins may cause intermittent failures during extended testing.

The tester can verify:

* Logic functionality
* Output enable operation
* Tri-state behaviour
* Bus transceiver direction control
* Input and output operation
* Stuck-high and stuck-low faults

The tester performs **functional verification only**.

It does **not** measure:

* Propagation delay
* Maximum operating frequency
* Output drive capability
* Leakage current
* Full datasheet compliance

---

# How devices are verified

Before an IC is added to the **Verified** list, it is tested on physical Rev-B hardware.

Validation normally includes:

* Correct device identification
* Quick Test
* Full Functional Test
* Soak Test (where applicable)
* Verification using known-good devices
* Confirmation that the observed behaviour matches the expected logic function

Firmware implementation alone does not qualify a device as **Verified**.

---

# Community contributions

Additional IC definitions and validation results are always welcome.

When submitting a new device, please include:

* IC part number
* Logic family
* Package type
* Test definition source code
* Pin mapping
* Hardware revision used
* Quick Test results
* Full Test results
* Soak Test results (if performed)
* Any known limitations or observations

Community contributions help expand the supported IC library and increase confidence in the validation process.

---

# Project scope

The Rev-B Pico 74xx IC Tester is designed to test the most commonly encountered 74xx-series logic ICs using standard 14-pin, 16-pin and 20-pin DIP packages.

Devices requiring non-standard power connections, adapter boards, specialised timing analysis, analogue measurements or additional hardware are outside the design scope of this project.