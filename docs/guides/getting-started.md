# Getting Started

![Completed OD-PT74](../images/usage/3c-.jpg)

Welcome to the **OD-PT74 Pico 74xx IC Tester**.

This guide will help you assemble the hardware, install the firmware, and perform your first IC test. This guide assumes you are using the Rev-C hardware PCB and firmware v1.0.0.

For more detailed information, see the additional guides in the documentation.

---

## Before you begin

You will need:

* Rev-C PCB set
* Raspberry Pi Pico (RP2040)
* All components listed in the Bill of Materials (BOM)
* USB cable
* Computer with USB support
* Soldering equipment
* Small hand tools

Basic electronics assembly experience is recommended.

---

## Step 1 – Assemble the hardware

Populate both PCBs according to the Build Guide.

During assembly:

* Install low-profile components first.
* Observe the polarity of all diodes, electrolytic capacitors and LEDs.
* Fit all IC sockets before installing integrated circuits.
* Carefully inspect every solder joint before applying power.

When assembly is complete, perform a visual inspection to check for:

* solder bridges
* dry joints
* incorrect component values
* reversed polarised components
* bent connector pins

Refer to the **Build Guide** for detailed assembly instructions.

---

## Step 2 – Install the firmware

Install the supported version of MicroPython onto the Raspberry Pi Pico, then copy the OD-PT74 firmware files to the board.

Copy the project firmware to the Pico by following the Firmware Guide.

Refer to the firmware installation instructions if you are unfamiliar with installing MicroPython.

---

## Step 3 – Power up

Connect the Pico to your computer using a USB cable.

On first power-up the tester automatically performs a **Power-On Self Test (POST)**.

During POST the tester verifies:

* OLED display
* MCP23017 communication
* I²C bus
* Package selector
* DUT voltage selector
* TEST button

If all checks pass, the main menu is displayed.

If a fault is detected, the tester displays an error message describing the failed test.

---

## Step 4 – Configure the tester

Before testing an IC:

1. Select the correct package size.
2. Select the required DUT supply voltage.
3. Confirm the ZIF socket is empty.

The tester is now ready for use.

---

## Step 5 – Perform your first test

A 74LS00 or 74HC00 quad NAND gate is recommended for your first test because these devices are widely available and easy to verify.

1. Set the DUT voltage selector to OFF.
2. Open the ZIF socket.
3. Insert the IC with Pin 1 correctly oriented.
4. Close the ZIF socket.
5. Select the package size (14, 16 or 20 pins).
6. Select the DUT voltage (3.3 V or 5 V).
7. Select the device family and IC from the menu.
8. Press **TEST**.
9. Review the test results displayed on the OLED.

If the device passes, your tester is operating correctly.

---

## Safety notes

> [!IMPORTANT]
>
> Always move the DUT voltage selector to OFF before inserting or removing an IC.

> [!IMPORTANT]
>
> Never insert or remove an IC while a test is in progress.

> [!WARNING]
>
> Verify the orientation of every device before closing the ZIF socket.

> [!WARNING]
>
> The tester is designed for supported 74xx-series logic devices only. Do not connect external circuitry to the DUT socket while testing.

---

Congratulations! Your **OD-PT74 Pico 74xx IC Tester** is now ready to test supported 74xx-series logic ICs.

We hope you enjoy using it, and we welcome bug reports, hardware feedback, and contributions to expand the supported IC library.

---

---

## Next Steps

Now that your OD-PT74 is assembled and running, continue with the Build Guide for detailed assembly information and optional enhancements.

## Related Documentation

| Document | Description |
|----------|-------------|
| [🏠 Project Home](../../README.md) | Return to the main project page |
| [📖 Documentation Index](../README.md) | Browse all project documentation |
| **🚀 Getting Started** | **You are here** |
| [🔧 Build Guide](build-guide.md) | Complete hardware assembly instructions |
| [💾 Firmware Guide](firmware-guide.md) | Installing and updating the firmware |
| [▶️ Usage Guide](usage-guide.md) | Operating the tester |
| [🧩 Supported ICs](supported-ics.md) | List of supported logic devices |
| [🛠 Troubleshooting Guide](troubleshooting-guide.md) | Diagnose common hardware and firmware issues |

---

| ← Previous | Next → |
|------------|--------|
| [🏠 Project Home](../../README.md) | [🔧 Build Guide](build-guide.md) |