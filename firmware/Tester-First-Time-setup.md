# Installing MicroPython and the OD-PT74 Pico 74xx Logic IC Tester Firmware

If this is your first time using a Raspberry Pi Pico, don't worry—this guide walks you through every step.
Difficulty: Beginner
Estimated time: 10–15 minutes

This guide was validated using MicroPython v1.28.0 and Thonny 4.x. Newer versions should also work, but the screenshots may differ slightly.

## OD-PT74 First-Time Setup

## Requirements

You'll need:
- Raspberry Pi Pico or Pico W
- USB cable
- Windows / Linux / macOS
- Internet connection

## Step 1 - Install Thonny
➡️ **Download Thonny**
https://thonny.org
Download and install Thonny from the official website before continuing with this guide.
- Install and Start Thonny.

## Step 2 - Install MicroPython

- Hold BOOTSEL.
- Plug the Pico into USB.
- Release BOOTSEL.
- A new drive appears.
* In Thonny:
	Run
	   Select Interpreter
		Raspberry Pi Pico
		     Install MicroPython

## Step 3 - Download the Project

Clone the GitHub repository or download the ZIP archive, then open the firmware folder.

## Step 4 - Copy the Firmware

Copy the following file to the Raspberry Pi Pico:

- main.py

(Save the files to the Raspberry Pi Pico in Thonny, not to "This Computer".)

Saving main.py causes the Pico to restart automatically. This is normal.

![Installing main.py](../images/firmware/23-save-to-pico.jpg)

*Figure 1. Saving main.py to RP2040.*

## Step 5 - Install Required Libraries

Make sure you Copy this file to the Pico:

ssd1306.py

ssd1306.py is the display driver used by the tester. 

MicroPython does not include this library by default, 

ssd1306.py is included in the project's firmware folder and it must be copied to the Pico before the OLED will work.

(Save the files to the Raspberry Pi Pico in Thonny, not to "This Computer".)

![Installing ssd1306.py](../images/firmware/23-save-to-pico.jpg)

*Figure 2. Saving ssd1306.py to RP2040.*

## Step 6 - Verify the Files

The Pico should contain:

| File         | Purpose               |
| ------------ | --------------------- |
| `main.py`    | Main OD-PT74 firmware |
| `ssd1306.py` | OLED display driver   |

![verify files](../images/firmware/24-files on PR2040.jpg)

*Figure 3. files installed on PR2040.*

## Step 7 - Reset the Pico

Press Reset or unplug/replug USB.

Expected terminal output:

Booting OD-PT74...
POST...
MCP23017 PASS
OLED PASS
...
If the terminal window is not visible in Thonny, open View → Shell to see the POST messages.

![verify files](../images/firmware/25-main boot.jpg)

*Figure 4. the boot screen from Thonny.*

## Step 8 - First Boot

When the Pico restarts you should see:

==============================
OD-PT74
Pico 74xx Logic IC Tester
Firmware v1.0.0
==============================
POST...
MCP23017 PASS
OLED PASS

If you see this, your firmware has been installed successfully.

Congratulations!

Your OD-PT74 Pico 74xx Logic IC Tester firmware is now installed.

Continue with the Bring-Up Guide to verify the hardware.

## Next Step;

Continue with the **[Bring-up Checklist](...)**

## Common Mistakes & Troubleshooting

OLED not detected ?

Before checking the wiring:

• Forgot to copy ssd1306.py to the Pico.
• Saved main.py onto the PC instead of the Pico.
• Selected the wrong interpreter in Thonny.
• OLED connected to the wrong I²C address (0x3C/0x3D).
• USB cable is charge-only and cannot transfer data.
• Does i2c.scan() show the OLED?
• Forgot to install MicroPython before copying main.py.
