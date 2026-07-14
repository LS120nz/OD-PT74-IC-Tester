# Getting Started

Welcome to the **Pico 74xx IC Tester** project.

This guide will help you assemble the hardware, install the firmware, and perform your first IC test. It assumes you are using the **Rev-B** hardware and the **Rev-B v1.0.0** firmware release.

If you are looking for more detailed technical information, refer to the other guides in the `docs/` directory.

---

# Before you begin

You will need:

* Rev-B PCB set
* Raspberry Pi Pico (RP2040)
* All components listed in the Bill of Materials (BOM)
* USB cable
* Computer with USB support
* Soldering equipment
* Small hand tools

Basic electronics assembly experience is recommended.

---

# Step 1 – Assemble the hardware

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

# Step 2 – Install the firmware

Install the latest release of MicroPython onto the Raspberry Pi Pico.

Copy the project firmware to the Pico using your preferred MicroPython development environment.

Refer to the firmware installation instructions if you are unfamiliar with installing MicroPython.

---

# Step 3 – Power up

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

# Step 4 – Configure the tester

Before testing an IC:

1. Select the correct package size.
2. Select the required DUT supply voltage.
3. Confirm the ZIF socket is empty.

The tester is now ready for use.

---

# Step 5 – Perform your first test

A 74LS00 or 74HC00 quad NAND gate is recommended for your first test because these devices are widely available and easy to verify.

1. Open the ZIF socket.
2. Insert the IC with Pin 1 correctly oriented.
3. Close the ZIF socket.
4. Select the device from the menu.
5. Press **TEST**.
6. Review the test results displayed on the OLED.

If the device passes, your tester is operating correctly.

---

# Safety notes

> **Important**
>
> Always select the correct DUT supply voltage before inserting an IC.

> **Important**
>
> Never insert or remove an IC while a test is in progress.

> **Warning**
>
> Verify the orientation of every device before closing the ZIF socket.

> **Warning**
>
> The tester is designed for supported 74xx-series logic devices only. Do not connect external circuitry to the DUT socket while testing.

---

# Next steps

Once your tester is operating correctly, the following guides provide more detailed information:

* **Project Overview** — design philosophy and architecture
* **Build Guide** — complete hardware assembly instructions
* **Usage Guide** — operating the tester
* **Supported ICs** — verified device list
* **Troubleshooting** — diagnosing common problems

---

Congratulations! Your Pico 74xx IC Tester is now ready to begin testing supported 74xx-series logic ICs.

We hope you enjoy using it, and we welcome bug reports, hardware feedback, and contributions to expand the supported IC library.
