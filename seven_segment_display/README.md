# Emulator of the 7 segment LED display

## Description

The purpose of this script is to emulate the 7 segment LED display panel.

## Explanation

- The 7 segment LED display panel contains eight 4-digit displays.

- Panel displays table

| source | left col | right col |
|--------|----------|-----------|
| ADC1   | CH1      | CH2       |
| ADC2   | CH1      | CH2       |
| ADC3   | CH1      | CH2       |
| ADC4   | CH1      | CH2       |

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

- Serial device
    - Set value for 'dev' constant in a 7_seg_display/const.py file.

- Each number or text has its unique control character (prefix) which defines the corresponding display.
    - Examples:
        - String '{1234\r' will display number 1234 on the ADC3, CH1 location.
        - String ']10099\r' will display number -99 on the ADC1, CH2 location.
        - String ':10000\r' will display text StoP on the ADC4, CH2 location.
    - Generally:
        - 4-digits => positive numbers.
        - 5-digits => negative numbers and text.

- Control characters table

|      | CH1 | CH2 |
|------|-----|-----|
| ADC1 | [   | ]   |
| ADC2 | (   | )   |
| ADC3 | {   | }   |
| ADC4 | ;   | :   |

### Output

- Computer monitor.

**Prerequisites**

- Python 3.x - 64bit

**Dependencies**

- Tkinter installed

### Run DEMO

- Run main program: ```python run/sevenseg.py```
    - Demo will start immediately.
