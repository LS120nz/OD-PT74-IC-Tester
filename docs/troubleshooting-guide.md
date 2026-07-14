# Troubleshooting Guide

## Introduction

This guide provides practical troubleshooting information for the **Rev-B Pico 74xx IC Tester**.

Most problems can be resolved by following the recommended diagnostic steps in this guide. Work through each section in order, beginning with the power supply and progressing through the hardware and firmware checks.

> [!TIP]
> Do not assume the IC under test is faulty. Always verify the tester is operating correctly before diagnosing the device.

---

## Before you begin

Before troubleshooting, ensure:

* The hardware has been assembled according to the **Build Guide**.
* The latest Rev-B firmware is installed.
* The Raspberry Pi Pico is correctly seated.
* The tester is powered from a stable 5 V USB supply.

Have the following available:

* Digital multimeter
* Known-good 74LS00 or 74HC00
* USB cable
* Magnifying glass or inspection lamp

---

## Power problems

### Symptom

The tester does not power on.

### Possible causes

* No USB power
* Incorrectly fitted voltage regulator
* Incorrect BAT54S orientation
* Short circuit on the PCB
* Faulty USB cable

### Checks

* Verify 5 V at the USB input.
* Verify 3.3 V regulator output.
* Inspect for solder bridges.
* Check regulator orientation.
* Confirm BAT54S orientation.

> [!IMPORTANT]
> Do not continue until both the 5 V and 3.3 V rails are correct.

---

## POST failures

During startup the tester performs a **Power-On Self Test (POST)**.

If POST reports an error, identify the failed subsystem before continuing.

### OLED failure

Possible causes:

* OLED module not connected
* Incorrect header soldering
* I²C communication fault

Checks:

* Inspect the OLED header.
* Verify SDA and SCL continuity.
* Confirm the OLED module is correctly fitted.

---

### MCP23017 failure

Possible causes:

* MCP23017 incorrectly installed
* Poor solder joints
* I²C bus fault

Checks:

* Verify 3.3 V supply.
* Inspect SDA and SCL.
* Check device orientation.
* Reflow suspect solder joints.

---

### Button test failure

Possible causes:

* Incorrect switch orientation
* Poor solder joints
* Mechanical obstruction

Checks:

* Press each button several times.
* Inspect solder joints.
* Verify switch operation using a multimeter if necessary.

---

## OLED display problems

### Symptom

Display remains blank.

Possible causes:

* No power
* Incorrect OLED orientation
* Faulty OLED module
* I²C communication failure

Checks:

* Verify the 3.3 V rail.
* Confirm OLED orientation.
* Inspect the OLED connector.
* Check I²C continuity.

---

## Rotary encoder problems

### Symptom

Menu navigation is unreliable.

Possible causes:

* Poor solder joints
* Incorrect encoder alignment
* Mechanical damage

Checks:

* Inspect solder joints.
* Confirm encoder alignment.
* Rotate the encoder slowly while observing the menu.

---

## TEST button problems

### Symptom

Pressing **TEST** has no effect.

Possible causes:

* Faulty switch
* Poor solder joint
* Firmware configuration issue

Checks:

* Inspect switch soldering.
* Verify switch operation.
* Repeat the POST.

---

## IC testing problems

### Symptom

Every IC reports **FAIL**.

Possible causes:

* Incorrect IC selected
* Wrong package size
* Wrong DUT supply voltage
* Poor IC socket contact

Checks:

* Verify the selected IC.
* Verify package selection.
* Confirm the DUT voltage.
* Reinsert the IC.
* Test using a known-good device.

---

### Symptom

Only one IC fails.

Possible causes:

* Faulty IC
* Dirty or oxidised pins
* Bent pins
* Counterfeit device

Checks:

* Clean the IC pins.
* Straighten bent pins.
* Test another known-good device of the same type.
* Repeat the test.

---

## Intermittent failures

Intermittent failures are often caused by:

* Dirty IC pins
* Worn ZIF socket contacts
* Poor solder joints
* Marginal ICs
* Incorrect supply voltage

Use **Soak Test** mode to help identify intermittent faults.

---

## 74LVC device problems

> [!IMPORTANT]
> All 74LVC devices must be tested with the DUT voltage selector set to **3.3 V**.

Common causes of failure include:

* Incorrect supply voltage
* Dirty IC pins
* Poor socket contact

---

## Before reporting a problem

Please gather the following information:

* Hardware revision
* Firmware version
* IC part number
* Logic family
* Package size
* DUT voltage
* Test mode
* POST results
* Error messages
* USB serial output (if available)

Providing this information will help diagnose the problem more quickly.

---

## Quick reference

| Symptom                    | Possible cause           | Recommended action                       |
| -------------------------- | ------------------------ | ---------------------------------------- |
| No power                   | USB or regulator problem | Verify 5 V and 3.3 V rails               |
| Blank OLED                 | Display or I²C fault     | Check OLED installation                  |
| POST failure               | Hardware fault           | Identify failed subsystem                |
| TEST button not responding | Switch or solder fault   | Inspect button and solder joints         |
| All ICs fail               | Configuration error      | Verify IC selection, package and voltage |
| One IC fails               | Faulty IC                | Test another known-good device           |
| Intermittent failures      | Poor contact             | Clean IC pins and run Soak Test          |

---

## Still having problems?

If the fault cannot be resolved:

1. Repeat the POST.
2. Verify the power rails.
3. Test with a known-good IC.
4. Review the **Build Guide**.
5. Review the **Usage Guide**.

If you believe you have found a firmware defect or hardware issue, please include the information listed above when opening a GitHub issue.

Most problems are resolved by careful inspection of the power supply, solder joints, connector alignment, or IC orientation before more complex troubleshooting is required.
