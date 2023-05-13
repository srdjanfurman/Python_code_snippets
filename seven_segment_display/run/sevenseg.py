# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman

Emulator of the 7 segment LED display.
"""

import signal
import sys

from common.utils import generate_test_data_fixed
from device.display import Display


def handler(signum, frame):
    """Signal handler"""

    print(f'\nExiting on signal: {signum}, frame: {frame}')
    sys.exit(0)


def main():
    """Main function"""

    display_title = 'ADC Status'

    # The first four elements are the y-axis titles.
    # The last elements two are the x-axis titles.
    display_axis_titles = ['ADC1:', 'ADC2:', 'ADC3:', 'ADC4:', 'CH1:', 'CH2:']

    # Display colors per row.
    display_colors = ['red', 'green', 'blue', 'yellow']

    # Display setting altogether.
    display_setting = (display_title, display_axis_titles, display_colors)

    # Function generate_test_data is provided for the testing purpose.
    data_generator_callable = generate_test_data_fixed

    # NOTE: Display setting can be a JSON file, e.g. config.json.

    display = Display(*display_setting, data_generator_callable)

    display.run(100)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    main()
