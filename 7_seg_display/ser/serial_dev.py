# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman
"""

import sys

from serial import Serial
from serial.serialutil import SerialException

from common import const


class SerialDevice:
    """SerialDevice class"""

    def __init__(self, serial_device: str) -> None:
        self.serial_device = Serial(serial_device, 57600)

    def open_serial_device(self) -> Serial:
        """
        Open serial device.
        """

        try:
            if not self.serial_device.isOpen():
                self.serial_device.open()
            print(f'\nDevice {self.serial_device.portstr} selected.\n')
        except SerialException as exc:
            print(f'\nError opening serial port: {exc}\n')

            sys.exit(1)

        try:
            self.serial_device.reset_input_buffer()
            self.serial_device.reset_output_buffer()

        except SerialException as exc:
            print(f'\nError communicating on serial port: {exc}\n')

            self.serial_device.close()

            sys.exit(1)

        return self.serial_device

    def close_serial_device(self) -> None:
        """
        Close serial device.
        """

        if self.serial_device.isOpen():
            self.serial_device.close()

            print(f'Device {self.serial_device.port} closed.\n')

    def read_serial_device(self) -> bytes:
        """
        Read from the serial device.

        Example out (terminal):
            [10000
            ]10000
            %00000
            (00000
            )00000
        """

        # NOTE: It's hard to make it more pythonic...
        #       Procedural 'how to' approach is needed.

        out = b''

        while self.serial_device.in_waiting > 0:  # Do not block.
            char = self.serial_device.read()

            if char in const.CHs:  # Wait for the control character (start reception).

                ctrl_char = char
                out += ctrl_char

                while True:
                    char = self.serial_device.read()

                    if char != b'\r':
                        out += char

                    else:
                        break
                break

        return out
