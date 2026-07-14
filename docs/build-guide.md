# Build Guide

## Introduction

This guide describes the assembly of the **Rev-B Pico 74xx IC Tester** hardware.

The Rev-B design consists of two printed circuit boards that together form the complete tester. This guide follows the recommended assembly sequence, including inspection and verification checkpoints, to help ensure a successful build.

> **📷 Photo Placeholder**
>
> *Completed Rev-B Pico 74xx IC Tester*

---

## Before you begin

### Tools required

* Fine-tip soldering iron
* Quality electronic solder
* Side cutters
* Small pliers
* Tweezers
* Digital multimeter
* Magnification (recommended)

### Parts required

Refer to the current Bill of Materials (BOM) for the complete component list.

Before beginning assembly:

* Verify all components are present.
* Check resistor values.
* Identify all polarised components.
* Familiarise yourself with the PCB layout.

> [!TIP]
> Sort resistors and capacitors by value before starting. This makes assembly faster and significantly reduces mistakes.

---

## Assembly

## Stage 1 – Power supply

The Rev-B tester includes an onboard power supply. Assemble and verify this section before installing any other components.

Install:

* BAT54S protection diode(s)
* 3.3 V voltage regulator
* Associated bypass capacitors

<!-- Figure 1 -->
![Power supply assembled](../images/build/01-power-supply.jpg)

*Figure 1. Rev-B power supply assembled.*

### Power supply verification

Connect a regulated 5 V USB supply.

Verify:

* 5 V input present
* Stable 3.3 V regulator output
* No excessive current draw
* No component heating

Disconnect power before continuing.

> [!IMPORTANT]
> Verifying the power supply first makes fault finding much easier than troubleshooting a fully populated board.

---

## Stage 2 – Main board assembly

Populate the main board using the following order:

1. Resistors
2. Ceramic capacitors
3. Diodes
4. IC sockets
5. Headers and connectors

<!-- Figure 2 -->
![Main board after passives](../images/build/02-main-board-after-passives.jpg)

*Figure 2. Main board after passive components installed.*

Continue with:

* Push buttons
* LEDs
* Buzzer
* Remaining connectors

<!-- Figure 3 -->
![Main board complete](../images/build/02-main-board-complete.jpg)

*Figure 3. Completed main board.*

### Checkpoint

Before continuing:

* ✓ No solder bridges
* ✓ Correct resistor values
* ✓ Correct diode orientation
* ✓ All IC sockets aligned
* ✓ Board cleaned and inspected

---

## Stage 3 – Top board assembly

Assemble the top board.

Pay particular attention to:

* OLED header orientation
* Rotary encoder alignment
* Board-to-board connector alignment

<!-- Figure 4 -->
![Top board](../images/build/04-top-board.jpg)

*Figure 4. Top board assembly.*

<!-- Figure 5 -->
![Top board complete](../images/build/05-top-board-complete.jpg)

*Figure 5. Completed top board.*

> [!NOTE]
> **Checkpoint**
>
> Before continuing, confirm:
>
> - No solder bridges
> - Correct resistor values
> - Correct diode orientation
> - All IC sockets aligned
> - Board cleaned and inspected

---

## Stage 4 – Raspberry Pi Pico

Install the Raspberry Pi Pico only after both boards have passed inspection.

Before fitting the Pico:

* Verify there are no shorts between power rails.
* Check connector alignment.
* Confirm correct orientation.

<!-- Figure 6 -->
![Pico installed](../images/build/06-pico-installed.jpg)

*Figure 6. Raspberry Pi Pico installed.*

---

## Stage 5 – Final assembly

Join the main and top boards.

Install:

* OLED module
* Remaining hardware
* Spacers and fasteners (if fitted)

Carry out a final visual inspection.

<!-- Figure 7 -->
![Boards assembled](../images/build/07-boards-assembled.jpg)

*Figure 7. Fully assembled PCB stack.*

---

## Electrical checks

> [!WARNING]
> Never install the Raspberry Pi Pico or any socketed ICs until the power supply has been verified and the board has been inspected for shorts.

Before applying power:

* Check resistance between 5 V and GND.
* Check resistance between 3.3 V and GND.
* Inspect for solder bridges.
* Confirm regulator orientation.
* Confirm BAT54S orientation.
* Ensure no loose solder or debris remains.

> [!TIP]
> Spending a few minutes checking the board before power-up can prevent hours of fault finding later.

---

## First power-up

Connect the tester to a USB power source.

The tester will automatically perform the **Power-On Self Test (POST)**.

Expected sequence:

1. OLED initialises.
2. POST begins.
3. Hardware checks complete.
4. Main menu appears.

<!-- Figure 8 -->
![POST screen](../images/build/08-post-screen.jpg)

*Figure 8. Power-On Self Test (POST).*

If POST reports an error, refer to the **Troubleshooting Guide** before continuing.

---

## Initial functional check

Verify the following operate correctly:

* OLED display
* Rotary encoder
* TEST button
* Package selector
* DUT voltage selector

<!-- Figure 9 -->
![Main menu](../images/build/09-main-menu.jpg)

*Figure 9. Main menu.*

<!-- Figure 10 -->
![PASS result](../images/build/10-pass-result.jpg)

*Figure 10. Successful PASS result.*

The tester is now ready for its first IC.

---

## Next steps

Your hardware assembly is complete.

Continue with the following guides:

1. Read the [Usage Guide](usage-guide.md).
2. Insert a known-good 74LS00 or 74HC00.
3. Perform a Quick Test.
4. Verify the tester reports a successful PASS result.

Congratulations! Your **Rev-B Pico 74xx IC Tester** is now ready for normal operation.
