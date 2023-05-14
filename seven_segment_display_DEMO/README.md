# Emulator of the seven segment LED display panel DEMO

## Description

The purpose of this script is to emulate the seven segment LED display panel.

## Explanation

- The seven segment LED display panel contains eight 4-digit displays.

- Panel displays table

| source | left col | right col |
|--------|----------|-----------|
| ADC1   | Ch1      | Ch2       |
| ADC2   | Ch1      | Ch2       |
| ADC3   | Ch1      | Ch2       |
| ADC4   | Ch1      | Ch2       |

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
    - Set value for 'DEV' constant in a seven_segment_display_DEMO/const/consts.py file.

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
| ADC1 | [   | ]   |
| ADC2 | (   | )   |
| ADC3 | {   | }   |
| ADC4 | ;   | :   |

### Output

- Computer monitor.

**Prerequisites**

- Python 3.x - 64bit

**Dependencies**

- Install requirements
    - `pip install -r requirements.txt`

**Usage**

- Run the script
    - `python main.py`

### Run DEMO

- Open virtual serial ports:
  ```
  python virtual_serial.py
  ```
    - The log message should look like:
      ```
      /dev/pts/1
      /dev/pts/2
      ```

- Copy one serial device into const/consts.py file:
  ```
  DEV = '/dev/pts/1'
  ```

- Copy the other one serial device into run_data_dyn.sh file:
  ```
  echo -ne "${CTRL_CHRS[RND_NUM_LST]}${RND_NUM}\r\n" > /dev/pts/2
  ```

- Open Terminal and run: ```./run_data_dyn.sh```
- Run main program: ```python main.py```
