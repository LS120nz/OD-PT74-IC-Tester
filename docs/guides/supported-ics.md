# Supported ICs

## Introduction

This document lists the logic ICs currently supported by the **OD-PT74 Pico 74xx Logic IC Tester**.

Each device listed has either been validated on physical Rev-C hardware or is included in the firmware awaiting hardware verification.

The Rev-C hardware platform focuses on standard **74xx-series logic ICs** in **14-pin, 16-pin, and 20-pin DIP packages** using conventional power pin arrangements.

---

## Validation summary

**Current Release

Firmware: v1.0.0
Hardware: Rev-C

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
- 📋 Outside the scope of the OD-PT74

---

## Validation levels

| Status                    | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| ✅ **Verified**           | Successfully tested on physical Rev-C hardware.                                             |
| ⚠ **Failed**              | Physical device tested but failed functional verification.                                  |
| 🧪 **Pending Validation** | Firmware support exists but physical validation has not yet been completed.                 |
| 📦 Not Yet Tested (No Sample Available)| Firmware support exists but a suitable device was not available for testing.                |
| 🚫 Not Supported          | Outside the design scope of the OD-PT74.                                  |

A device is considered **Verified** only after successful testing on physical Rev-C hardware PCB using one or more of the available test modes (Quick, Full, and Soak, where appropriate).

---

## Verified Devices

The following devices have been successfully validated on physical Rev-C hardware PCB.

## 14-pin Devices

| IC      | Function                 | Status   | 
| ------- | ------------------------ | -------- | 
| 74HC00  | Quad 2-input NAND        |    ✅   | 
| 74LS00  | Quad 2-input NAND        |    ✅   | 
| 74HC02  | Quad 2-input NOR         |    ✅   | 
| 74LS02  | Quad 2-input NOR         |    ✅   | 
| 74HC03  | Quad 2-input NAND OC     |    ✅   | 
| 74LS04  | Hex inverter             |    ✅   | 
| 74HC05  | Hex inverter OC          |    ✅   |
| 74HC06  | Hex inverter / driver OC |    ✅   | 
| 74LS06  | Hex inverter / driver OC |    ✅   | 
| 74HC07  | Hex buffer / driver OC   |    ✅   | 
| 74LS07  | Hex buffer / driver OC   |    ✅   | 
| 74HC08  | Quad 2-input AND         |    ✅   | 
| 74HC10  | Triple 3-input NAND      |    ✅   | 
| 74LS11  | Triple 3-input AND       |    ✅   | 
| 74HC14  | Hex Schmitt inverter     |    ✅   | 
| 74HC21  | Dual 4-input AND         |    ✅   | 
| 74LS27  | Triple 3-input NOR       |    ✅   | 
| 74HC30  | 8-input NAND             |    ✅   | 
| 74HC32  | Quad 2-input OR          |    ✅   | 
| 74LS32  | Quad 2-input OR          |    ✅   | 
| 74LS74  | Dual D flip-flop         |    ✅   | 
| 74LS86  | Quad 2-input XOR         |    ✅   | 
| 74HC125 | Quad tri-state buffer    |    ✅   | 
| 74HC126 | Quad tri-state buffer    |    ✅   | 
| 74HC132 | Quad Schmitt NAND        |    ✅   | 
| 74HC164 | 8-bit shift register     |    ✅   | 
| 74HC393 | Dual binary counter      |    ✅   | 

---

## 16-pin Devices

| IC      | Function                              | Status   |
| ------- | ------------------------------------- | -------- |
| 74LS85  | 4-bit magnitude comparator            |    ✅   | 
| 74HC138 | 3-to-8 decoder                        |    ✅   | 
| 74HC139 | Dual 2-to-4 decoder                   |    ✅   | 
| 74LS139 | Dual 2-to-4 decoder                   |    ✅   | 
| 74LS151 | 8-input digital multiplexer           |    ✅   |
| 74LS153 | Dual 4-input multiplexer              |    ✅   | 
| 74LS157 | Quad 2:1 multiplexer                  |    ✅   |
| 74LS161 | 4-bit synchronous binary counter      |    ✅   | 
| 74HC163 | 4-bit counter                         |    ✅   | 
| 74HC165 | 8-bit PISO shift register             |    ✅   | 
| 74HC174 | Hex D flip-flop                       |    ✅   | 
| 74LS194 | 4-bit bidirectional shift register    |    ✅   | 
| 74HC595 | Serial-in parallel-out shift register |    ✅   | 


---

## 20-pin Devices

| IC      | Function              | Status   | 
| ------- | --------------------- | -------- | 
| 74HC244 | Octal buffer          |    ✅   | 
| 74HC245 | Octal bus transceiver |    ✅   | 
| 74HC273 | Octal D flip-flop     |    ✅   | 
| 74HC373 | Octal latch           |    ✅   | 
| 74HC374 | Octal D flip-flop     |    ✅   | 
| 74HC573 | Octal latch           |    ✅   |
| 74HC574 | Octal D flip-flop     |    ✅   | 


---

## 74LVC Devices

> [!IMPORTANT]
> All **74LVC** devices must be tested with the DUT voltage selector set to **3.3 V**.

| IC       | Function              | Status             | Notes             |
| -------- | --------------------- | ------------------ | ----------------- |
| 74LVC245 | Octal bus transceiver |         ✅        | Clean legs required |


---

# Pending Validation

The following devices are implemented in firmware but have not yet been validated on physical hardware.

| IC      | Function             | Status |
| ------- | -------------------- | ------ |
| 74HC04  | Hex inverter         | 📦 Not tested |
| 74HC11  | Triple 3-input AND   | 📦 Not tested |
| 74HC27  | Triple 3-input NOR   | 📦 Not tested |
| 74HC74  | Dual D flip-flop     | 📦 Not tested |
| 74HC86  | Quad 2-input XOR     | 📦 Not tested |
| 74HC151 | 8-input multiplexer  | 📦 Not tested |
| 74HC153 | Dual 4-input mux     | 📦 Not tested |
| 74HC157 | Quad 2:1 multiplexer | 📦 Not tested |
| 74HC161 | 4-bit counter        | 📦 Not tested |
| 74HC194 | Shift register       | 📦 Not tested |


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

Before an IC is added to the **Verified** list, it is tested on physical Rev-C hardware PCB.

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

The OD-PT74 Pico 74xx Logic IC Tester is designed to test the most commonly encountered 74xx-series logic ICs using standard 14-pin, 16-pin and 20-pin DIP packages.

Devices requiring non-standard power connections, adapter boards, specialised timing analysis, analogue measurements or additional hardware are outside the design scope of this project.

As additional IC definitions are developed and verified, this guide will continue to expand with future firmware releases.

---

## Next Steps

You now have an overview of the logic devices currently supported by the **OD-PT74 Pico 74xx Logic IC Tester**.

As additional IC definitions are developed and verified, this guide will continue to expand with future firmware releases.

If you encounter unexpected behaviour while testing a supported device, refer to the **Troubleshooting Guide** for diagnostic procedures and common solutions.

## Related Documentation

| Document | Description |
|----------|-------------|
| [🏠 Project Home](../../README.md) | Return to the main project page |
| [📖 Documentation Index](../README.md) | Browse all project documentation |
| [🚀 Getting Started](getting-started.md) | First-time setup |
| [🔧 Build Guide](build-guide.md) | Hardware assembly |
| [💾 Firmware Guide](firmware-guide.md) | Installing and updating the firmware |
| [▶️ Usage Guide](usage-guide.md) | Operating the tester |
| **🧩 Supported ICs** | **You are here** |
| [🛠 Troubleshooting Guide](troubleshooting-guide.md) | Diagnose common hardware and firmware issues |

---

| ← Previous | Next → |
|------------|--------|
| [▶️ Usage Guide](usage-guide.md) | [🛠 Troubleshooting Guide](troubleshooting-guide.md) |