# Emulator of the seven segment LED display panel

## Description

The purpose of this script is to emulate the seven segment LED display panel.

## Explanation

- The seven segment LED display panel contains eight 4-digit displays.

- Panel displays table example

| source | left col | right col |
|--------|----------|-----------|
| Val1   | Ch1      | Ch2       |
| Val2   | Ch1      | Ch2       |
| Val3   | Ch1      | Ch2       |
| Val4   | Ch1      | Ch2       |

- Data format example

| input | display |
|-------|---------|
| 1     | 1       |
| 0     | 0       |
| 10001 | -1      |
| 10011 | -11     |
| 12000 | Err0    |
| 12001 | Err1    |
| 10000 | StoP    |

### Input

- Each number or text has its unique control character (prefix) which defines the corresponding display.
    - Examples:
        - String '{1234\r' will display number 1234 on the ADC3, CH1 location.
        - String ']10099\r' will display number -99 on the ADC1, CH2 location.
        - String ':10000\r' will display text StoP on the ADC4, CH2 location.
    - Generally:
        - 4-digits => positive numbers.
        - 5-digits => negative numbers and text.

- Control characters table

|      | Ch1 | Ch2 |
|------|-----|-----|
| Val1 | [   | ]   |
| Val2 | (   | )   |
| Val3 | {   | }   |
| Val4 | ;   | :   |

### Output

- Computer monitor.

**Prerequisites**

- Python 3.x - 64bit

**Dependencies**

- Tkinter installed

### Run DEMO

- Run main program: ```python run/sevenseg.py```
    - Demo will start immediately.

### Pylint arguments

```
--msg-template={abspath}:{line}:{column}:{C}:({symbol}){msg} common device graphic run tests setup.py
```