# Bring-up Checklist

## Before installing socketed devices

- [ ] Inspect PCB for shorts or solder bridges
- [ ] Check 3.3V to GND resistance
- [ ] Check 5V to GND resistance
- [ ] Check V_OUT to GND resistance
- [ ] Confirm Pico orientation
- [ ] Confirm MCP23017 orientation
- [ ] Confirm transistor pinout
- [ ] Confirm ZIF socket orientation
- [ ] Confirm voltage selector switch orientation
- [ ] Confirm package selector switch orientation

## First power-on

- [ ] Power from USB only
- [ ] Confirm Pico boots
- [ ] Confirm 3.3V rail
- [ ] Confirm 5V/VBUS rail
- [ ] Confirm MCP23017 detected
- [ ] Confirm OLED detected if fitted
- [ ] Confirm buttons work
- [ ] Confirm RGB LED works
- [ ] Confirm buzzer works
- [ ] Confirm 5 V power LED
- [ ] Confirm 3.3 V power LED
- [ ] Confirm rotary encoder operation

## Switch tests

- [ ] Package switch reads 14-pin
- [ ] Package switch reads 16-pin
- [ ] Package switch reads 20-pin
- [ ] Voltage switch reads 3.3V
- [ ] Voltage switch reads OFF
- [ ] Voltage switch reads 5V

## Socket power tests

With no IC inserted:

- [ ] 14-pin mode: V_OUT appears on ZIF pin 20
- [ ] 14-pin mode: GND appears on ZIF pin 7
- [ ] 16-pin mode: V_OUT appears on ZIF pin 20
- [ ] 16-pin mode: GND appears on ZIF pin 8
- [ ] 20-pin mode: V_OUT appears on ZIF pin 20
- [ ] 20-pin mode: GND appears on ZIF pin 10

## First IC test

- [ ] Test known-good 74HC00 at 3.3V
- [ ] Test known-good 74HC04 at 3.3V
- [ ] Test known-good 74LS00 at 5V

## Final Verification

- [ ] POST completes with no errors
- [ ] Main menu displayed
- [ ] Known-good IC passes Quick Test
- [ ] Known-good IC passes Full Test
- [ ] Soak Test runs successfully

## Related Documentation

| Document | Description |
|----------|-------------|
| [🏠 Project Home](../../README.md) | Return to the main project page |
| [📖 Documentation Index](../README.md) | Documentation overview |

