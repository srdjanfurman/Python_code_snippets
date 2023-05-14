# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman

Emulator of the 7 segment LED disp.
"""

from device.display import Display
from serial.serialutil import SerialException

from const.consts import DEV
from ser.serial_dev import SerialDevice

if __name__ == '__main__':
    try:
        SD = SerialDevice(DEV)
        SD.open_serial_device()

        display_title = 'Data Status'

        # The first four elements are the y-axis titles.
        # The last elements two are the x-axis titles.
        display_axis_titles = ['ADC1:', 'ADC2:', 'ADC3:', 'ADC4:',
                               'Ch1:', 'Ch2:']

        # Display colors per row.
        display_colors = ['red', 'green', 'blue', 'yellow']

        # Display setting altogether.
        display_setting = (display_title, display_axis_titles, display_colors)

        # Function generate_test_data is provided for the testing purpose.
        data_generator_callable = SD.read_serial_device

        display = Display(*display_setting, data_generator_callable)

        display.run(1)

    except SerialException as e:
        print(e.strerror)
        SD = None

    if SD:
        SD.close_serial_device()
