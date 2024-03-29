# -*- coding: utf-8 -*-

""" Seven segment test run """

import signal
import sys

from common.utils import generate_test_data_fixed
from ssd_device.display import SSDisplay


def handler(signum, frame):
    """Signal handler"""

    print(f'\nExiting on signal: {signum}, frame: {frame}')
    sys.exit(0)


def main() -> None:
    """Main function"""

    display_title = 'ADC Status'

    # The first four elements are the y-axis titles.
    # The last elements two are the x-axis titles.
    display_axis_titles = ['Val1:', 'Val2:', 'Val3:', 'Val4:', 'Ch1:', 'Ch2:']

    # SSDisplay colors per row.
    display_colors = ['red', 'green', 'blue', 'yellow']

    # Function generate_test_data is provided for the testing purpose.
    data_generator_callable = generate_test_data_fixed

    # SSDisplay setting altogether.
    display_setting = (display_title, display_axis_titles, display_colors,
                       data_generator_callable)

    # NOTE: SSDisplay setting can be a JSON file, e.g. config.json.

    display = SSDisplay(*display_setting)

    display.run(100)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    main()
