##1. Overview
---
Purpose of Rev A
What it was used to validate
Known limitations

##2. Required Parts
---
RP2040 Pico
MCP23017
20-pin ZIF
OLED
Encoder
Buzzer
Buttons
Resistors
Capacitors

##3. Assembly Order
---
1. Resistors
2. Diodes
3. Capacitors
4. MCP23017 socket
5. Headers
6. OLED header
7. Buttons
8. ZIF socket
9. Pico

##4. First Power-Up
---
10. Check 3.3V
Check 5V
Check no shorts

##5. Bring-Up Procedure
---
Flash firmware
Check serial terminal
Verify MCP23017
Verify OLED
Verify buttons
Verify encoder
Verify RGB LED
Verify buzzer

##6. Known Rev A Issues
--
OLED SDA/SCL originally routed incorrectly
BAT54S orientation correction
1k resistor update
74163 test routine issue

##7. Validation Results
---
74HC00 PASS
74HC02 PASS
74HC03 PASS
...
74HC595 PASS

##8. Rev A Lessons Learned
---
Need self-powered operation
Need better front-panel ergonomics
Need modular UI board
Need improved OLED integration
