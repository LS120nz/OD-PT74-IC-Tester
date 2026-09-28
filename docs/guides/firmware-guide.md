# Firmware Guide

![Thonny Installed](../images/firmware/15-run-main.jpg)

Welcome to the **Firmware Guide** for the **OD-PT74 Pico 74xx IC Tester**.

This guide explains how to prepare a Raspberry Pi Pico (RP2040) by installing MicroPython and loading the OD-PT74 firmware. It provides a step-by-step walkthrough using the Thonny IDE, from connecting the Pico for the first time to running the firmware and verifying that the tester is operating correctly.

The firmware consists of two Python files:

- `main.py` – Main application firmware.
- `ssd1306.py` – OLED display driver.

No previous experience with MicroPython is required. Simply follow each step in order, and your tester will be ready to use in just a few minutes.

---

## Requirements

Before starting you will need:

- Raspberry Pi Pico 2 RP2040
- USB cable
- Computer running Windows, Linux or macOS
- Thonny IDE installed
- `main.py`
- `ssd1306.py`

> [!NOTE]
> This guide assumes the OD-PT74 hardware has already been assembled. 
>
> If you have not yet completed the hardware build, refer to the **Build Guide** before continuing.
>
> The firmware consists of two Python files:
> - `main.py` – Main application firmware.
> - `ssd1306.py` – OLED display driver.

---

## Installing Thonny

If Thonny is not already installed, download and install it before continuing.

Once installed, connect the Raspberry Pi Pico 2 to your computer using a USB cable.

![Thonny Start](../images/firmware/01-thonny-blank.jpg)

Figure 2 - Thonny IDE after starting.

Download and install the supported version of MicroPython as specified in the project README.

---

## Configure Thonny

Open the interpreter configuration.

![Interpreter Menu](../images/firmware/02-thonny-options.jpg)

Figure 3 - open the interpreter configuration.


Then select **Run → Interpreter...**

Select:

- **MicroPython (Raspberry Pi Pico)**

Connection:

- **Try to detect port automatically**

or select the correct COM port manually if required.

---

## Verify USB Connection

If no serial port is shown, open Windows Device Manager.

![Device Manager](../images/firmware/04-device-manager.jpg)

Figure 4 - windows device manager.

Expand:


Ports (COM & LPT)


Verify that the Raspberry Pi Pico 2 serial port is listed.

![USB Port](../images/firmware/05-usb-port.jpg)

Figure 5 - pico USB serial port detected.

Return to Thonny and select this COM port.

---

## Copy main.py

Open the firmware file.


Select **File → Open**.

![Load File](../images/firmware/06-load-file.jpg)

Figure 6 - opening a file.

Choose **This Computer**.

![Select PC](../images/firmware/07-select-main-pc.jpg)

Figure 7 - select "this computer".

Browse to **firmware/main.py**.

![Select main.py](../images/firmware/08-select-main-file.jpg)

Figure 8 - select main.py.

The firmware source should now appear in the editor.

![main.py Loaded](../images/firmware/09-main-loaded.jpg)

Figure 9 - main.py loaded into thonny.

---

## Save main.py

Select **File → Save As...**

Choose **Raspberry Pi Pico 2**.


Do **not** save the file back to your PC.

![Save to Pico](../images/firmware/10-save-to-pico.jpg)

Figure 10 - save main.py to the pico.

---

## Copy ssd1306.py

Repeat the same process for the OLED driver.

Open **ssd1306.py**.


![Open OLED Driver](../images/firmware/11-open-ssd1306.jpg)

Figure 11 - open ssd1306.py.

Select the file.

![Select OLED Driver](../images/firmware/12-select-ssd1306.jpg)

Figure 12 - select ssd1306.py.

Save it to the Raspberry Pi Pico 2.

![Save OLED Driver](../images/firmware/13-save-ssd1306.jpg)

Figure 13 - save ssd1306.py to the Pico 2.

---

## Run the Firmware

Close the OLED driver.

You should see "main.py" and "ssd1306.py" on the left panel under RP2040 device.

A stats.json file will be created automatically after you begin testing ICs. It stores tester statistics and does not need to be copied manually.

Ensure **main.py** is the active editor window.


![Return to main.py](../images/firmware/14-return-main.jpg)

Figure 14 - return to main.py.

Press the **Run** button **(green circle with arrow)** or press **F5**.

![Run Firmware](../images/firmware/15-run-main.jpg)

Figure 15 - running the firmware.

The OD-PT74 should now boot, perform its Power-On Self Test (POST), and display the main menu.

If the OLED display does not initialise, confirm that:

- `main.py` has been copied.
- `ssd1306.py` has been copied.
- The correct interpreter is selected.
- The Pico 2 is connected.

---

## Verifying Operation

If installation was successful, the following screens illustrate the normal operating modes of the OD-PT74.

The following screenshots show normal operation of the firmware.

## Quick Test

![Quick Test](../images/firmware/16-quick-test.jpg)

Figure 16 - Quick test.

## Full Test

![Full Test](../images/firmware/17-full-test.jpg)

Figure 17 - Full test.

## Soak Test

![Soak Test 1](../images/firmware/18-soak-test-1.jpg)

Figure 18 - Soak test.

![Soak Test 2](../images/firmware/19-soak-test-2.jpg)

Figure 19 - Soak test complete.

## Failure Examples

![Failure 1](../images/firmware/20-ic-fail-1.jpg)

Figure 20 - Failed IC example.

![Failure 2](../images/firmware/21-ic-fail-2.jpg)

Figure 21 - Failed IC example.

![Failure 3](../images/firmware/22-ic-fail-3.jpg)

Figure 22 - Failed IC example.

---

---

## Next Steps

Your **OD-PT74 Pico 74xx IC Tester** firmware should now be installed and ready to use.

Continue with the following guides to learn how to operate the tester, explore the supported IC library, and diagnose any hardware or firmware issues.

## Related Documentation

| Document | Description |
|----------|-------------|
| [🏠 Project Home](../../README.md) | Return to the main project page |
| [📖 Documentation Index](../README.md) | Browse all project documentation |
| [🚀 Getting Started](getting-started.md) | First-time setup |
| [🔧 Build Guide](build-guide.md) | Hardware assembly |
| **💾 Firmware Guide** | **You are here** |
| [▶️ Usage Guide](usage-guide.md) | Operating the tester |
| [🧩 Supported ICs](supported-ics.md) | List of supported logic devices |
| [🛠 Troubleshooting Guide](troubleshooting-guide.md) | Diagnose common hardware and firmware issues |

---

| ← Previous | Next → |
|------------|--------|
| [🔧 Build Guide](build-guide.md) | [▶️ Usage Guide](usage-guide.md) |
