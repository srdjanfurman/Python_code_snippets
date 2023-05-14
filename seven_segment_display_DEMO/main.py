# -*- coding: utf-8 -*-

""" Main """

from device.display import Display
from serial.serialutil import SerialException

from const.consts import DEV
from ser.serial_dev import SerialDevice

if __name__ == '__main__':
    try:
        SD = SerialDevice(DEV)
        SD.open_serial_device()

        DISPLAY_TITLE = 'Data Status'

        # The first four elements are the y-axis titles.
        # The last elements two are the x-axis titles.
        display_axis_titles = ['ADC1:', 'ADC2:', 'ADC3:', 'ADC4:',
                               'Ch1:', 'Ch2:']

        # Display colors per row.
        display_colors = ['red', 'green', 'blue', 'yellow']

        # Function generate_test_data is provided for the testing purpose.
        data_generator_callable = SD.read_serial_device

        # Display setting altogether.
        display_setting = (DISPLAY_TITLE, display_axis_titles, display_colors,
                           data_generator_callable)

        display = Display(*display_setting)

        display.run(1)

    except SerialException as e:
        print(e.strerror)
        SD = None

    if SD:
        SD.close_serial_device()
