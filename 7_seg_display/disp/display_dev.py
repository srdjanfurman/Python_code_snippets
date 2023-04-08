# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman
"""

import sys
import time
import tkinter as tk

from common import const
from common.const import CHs, DISP_SPEED, START, STOP, STEP, TEST_LST
from common.utils import generate_test_data, generate_test_data_dyn


class Display:
    """
    Class Display.

    Order 7 digit clockwise from top left, with crossbar last.
    Coordinates of each digit are (x0, y0, x1, y1)
    given as OFFSETS from top left measured in digit lengths.
    """

    def __init__(self, canvas: tk.Canvas) -> None:
        self.__canvas = canvas

        # Digit is one disp module.
        self.__digit = [[] for _ in range(const.MAX_DIGITS)]

        # Number is 4 digits.
        self.__number = [[] for _ in range(8)]

        self.__create_digits()

        self.data_dyn = iter([item for sublist in generate_test_data_dyn(
            START, STOP, STEP) for item in sublist])

    def __create_digits(self) -> None:
        """
        Create digits.
        """

        def segments(x_0: int, y_0: int, x_1: int, y_1: int) -> None:
            """
            Define segments.
            """

            def max_digits(idx: int) -> None:
                """
                Define maximum digits (4 digit number).
                """

                if idx < const.MAX_DIGITS - 24:  # 0-7
                    self.__digit[idx].append(self.__canvas.create_line(
                        const.POS_FIRST_ROW[idx + 1] + x_0 * const.LENGTH,
                        const.POS_FIRST_ROW[0] + y_0 * const.LENGTH,
                        const.POS_FIRST_ROW[idx + 1] + x_1 * const.LENGTH,
                        const.POS_FIRST_ROW[0] + y_1 * const.LENGTH,
                        fill="red", width=const.WIDTH, state='hidden', arrow=tk.BOTH, arrowshape=(8, 10, 0)))

                elif 7 < idx < const.MAX_DIGITS - 16:  # 8-15
                    self.__digit[idx].append(self.__canvas.create_line(
                        const.POS_SECOND_ROW[idx - 8 + 1] + x_0 * const.LENGTH,
                        const.POS_SECOND_ROW[0] + y_0 * const.LENGTH,
                        const.POS_SECOND_ROW[idx - 8 + 1] + x_1 * const.LENGTH,
                        const.POS_SECOND_ROW[0] + y_1 * const.LENGTH,
                        fill="green", width=const.WIDTH, state='hidden', arrow=tk.BOTH, arrowshape=(8, 10, 0)))

                elif 15 < idx < const.MAX_DIGITS - 8:  # 16-23
                    self.__digit[idx].append(self.__canvas.create_line(
                        const.POS_THIRD_ROW[idx - 16 + 1] + x_0 * const.LENGTH,
                        const.POS_THIRD_ROW[0] + y_0 * const.LENGTH,
                        const.POS_THIRD_ROW[idx - 16 + 1] + x_1 * const.LENGTH,
                        const.POS_THIRD_ROW[0] + y_1 * const.LENGTH,
                        fill="blue", width=const.WIDTH, state='hidden', arrow=tk.BOTH, arrowshape=(8, 10, 0)))

                elif 23 < idx < const.MAX_DIGITS:  # 24-31
                    self.__digit[idx].append(self.__canvas.create_line(
                        const.POS_FOURTH_ROW[idx - 24 + 1] + x_0 * const.LENGTH,
                        const.POS_FOURTH_ROW[0] + y_0 * const.LENGTH,
                        const.POS_FOURTH_ROW[idx - 24 + 1] + x_1 * const.LENGTH,
                        const.POS_FOURTH_ROW[0] + y_1 * const.LENGTH,
                        fill="yellow", width=const.WIDTH, state='hidden', arrow=tk.BOTH, arrowshape=(8, 10, 0)))
                else:
                    pass

            _ = [max_digits(idx) for idx in range(const.MAX_DIGITS)]

        _ = [segments(x0, y0, x1, y1) for x0, y0, x1, y1 in const.SEGMENTS]

        self.__number[0].extend([self.__digit[0]] + [self.__digit[1]] +
                                [self.__digit[2]] + [self.__digit[3]])

        self.__number[1].extend([self.__digit[4]] + [self.__digit[5]] +
                                [self.__digit[6]] + [self.__digit[7]])

        self.__number[2].extend([self.__digit[8]] + [self.__digit[9]] +
                                [self.__digit[10]] + [self.__digit[11]])

        self.__number[3].extend([self.__digit[12]] + [self.__digit[13]] +
                                [self.__digit[14]] + [self.__digit[15]])

        self.__number[4].extend([self.__digit[16]] + [self.__digit[17]] +
                                [self.__digit[18]] + [self.__digit[19]])

        self.__number[5].extend([self.__digit[20]] + [self.__digit[21]] +
                                [self.__digit[22]] + [self.__digit[23]])

        self.__number[6].extend([self.__digit[24]] + [self.__digit[25]] +
                                [self.__digit[26]] + [self.__digit[27]])

        self.__number[7].extend([self.__digit[28]] + [self.__digit[29]] +
                                [self.__digit[30]] + [self.__digit[31]])

    def __create_content(self, result_str: str, digit: list) -> None:
        """
        Create content.
        """

        result_int = int(result_str.rstrip('X'))

        def stop_message() -> None:
            """
            Message "Stop".
            """

            if result_int == 10000:
                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')
                     for iid, on in zip(digit[0], const.DIGITS[5])]  # S
                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')
                     for iid, on in zip(digit[1], const.DIGITS[17])]  # t

                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')
                     for iid, on in zip(digit[2], const.DIGITS[18])]  # o

                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')
                     for iid, on in zip(digit[3], const.DIGITS[19])]  # P

        def err_message() -> None:
            """
            Message "Err", "Err0" or "Err1".
            Message "Err" for values > 10999 is a disp device message, not of a DAS.
            """

            if result_int in (12000, 12001):
                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')  # E
                     for iid, on in zip(digit[0], const.DIGITS[15])]

                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')  # r
                     for iid, on in zip(digit[1], const.DIGITS[20])]

                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')  # r
                     for iid, on in zip(digit[2], const.DIGITS[20])]

                if result_int == 12000:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 0
                         for iid, on in zip(digit[3], const.DIGITS[0])]

                if result_int == 12001:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 1
                         for iid, on in zip(digit[3], const.DIGITS[1])]

        def positive_numbers() -> None:
            """
            Positive numbers 0 ... 9999.

            """

            if result_int < 10000:
                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')
                     for iid, on in zip(digit[0],
                                        const.DIGITS[int(result_str[:1])])]  # 0-9

                if result_int > 9:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')
                         for iid, on in zip(digit[1],
                                            const.DIGITS[int(result_str[1:2])])]  # 10-99
                else:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')
                         for iid, on in zip(digit[1],
                                            const.DIGITS[10])]

                if result_int > 99:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 100-999
                         for iid, on in zip(digit[2],
                                            const.DIGITS[int(result_str[2:3])])]
                else:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')
                         for iid, on in zip(digit[2],
                                            const.DIGITS[10])]

                if result_int > 999:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 1000-9999
                         for iid, on in zip(digit[3],
                                            const.DIGITS[int(result_str[3:4])])]
                else:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')
                         for iid, on in zip(digit[3], const.DIGITS[10])]

        def negative_numbers() -> None:
            """
            Negative numbers -1 ... -999.
            """

            if 10000 < result_int < 11000:
                _ = [self.__canvas.itemconfigure(iid, state='normal'
                if on else 'hidden')  # -
                     for iid, on in zip(digit[0], const.DIGITS[21])]

                if result_int > 10000:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 10001-10009
                         for iid, on in zip(digit[3],
                                            const.DIGITS[int(result_str[4])])]
                # else:
                #     _ = [self.__canvas.itemconfigure(iid, state='normal'
                #     if on else 'hidden')
                #          for iid, on in zip(digit[3], const.DIGITS[10])]

                if result_int > 10009:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 10010-10099
                         for iid, on in zip(digit[2],
                                            const.DIGITS[int(result_str[3])])]
                else:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')
                         for iid, on in zip(digit[2], const.DIGITS[10])]

                if result_int > 10099:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')  # 10100-10999
                         for iid, on in zip(digit[1],
                                            const.DIGITS[int(result_str[2])])]
                else:
                    _ = [self.__canvas.itemconfigure(iid, state='normal'
                    if on else 'hidden')
                         for iid, on in zip(digit[1], const.DIGITS[10])]

        stop_message()
        err_message()
        positive_numbers()
        negative_numbers()

    def display_content(self, ch_val, zero_ch_lst) -> None:
        """
        Display content (messages/number) on eight four number displays.

        Unpack values per each channel, e.g.
        [1111\r\n]2222\r\n(3333\r\n)4444\r\n{5555\r\n}6666\r\n;7777\r\n:8888\r\n
        and assign to corresponding variable.

        ch_value
            b'[2735'
            b']2738'
            b'(11000'
            b')11000'
        """

        def write() -> None:
            """
            Write on disp.
            """

            def channels(idx, chan) -> None:
                """
                Assign channels.
                """

                if chan in ch_val:
                    val = ch_val.lstrip(chan)  # b'10000'
                    # result_str, idx, ch
                    # b'2735' 0 b'['
                    # b'2739' 1 b']'
                    # b'11000' 2 b'('
                    # b'11000' 3 b')'

                    # Remove "Err#" from ADC2_CH1_CH2, write "0" instead.
                    int_val = int(val.rstrip(b'X'))

                    if int_val == 11000:
                        self.__create_content('0', self.__number[idx])
                        return

                    self.__create_content(val.decode('ascii'), self.__number[idx])

                # Remove numbers left behind from ADC3_CH1_CH2 and ADC4_CH1_CH2,
                # write "0" instead.
                elif chan in zero_ch_lst:
                    self.__create_content('0', self.__number[idx])

            _ = [channels(idx, ch) for idx, ch in enumerate(const.CHs)]

        write()

    def update_numbers(self, root, ser_dev, ch_lst) -> None:
        """
        Update numbers.
        """

        # num = 0

        if ser_dev:
            channel_value_row = ser_dev.read_serial_device()

        else:
            # channel_value_row = generate_test_data(bytes(item, 'utf-8')
            #                                   for item in test_lst)
            channel_value_row = generate_test_data(TEST_LST)
            # channel_value_row = generate_test_data(self.data_dyn)

            if channel_value_row:
                # num = channel_value_row.decode('ascii')[1:]
                print(channel_value_row)

            else:
                print('Ending DEMO...')
                sys.exit()

            time.sleep(DISP_SPEED)

        # statement = 0 <= int(num) <= 100
        # statement = int(num) % 10 == 0

        if len(channel_value_row) > 0:  # Skip empty strings, b''.
            # channel_value_row
            # b'[2736'
            # b']2738'
            # b'(11000'
            # b')11000'

            zero_ch_lst = []

            # Create list of all active channel symbols in one sequence.
            if len(ch_lst) < 8:
                ch_lst.append(channel_value_row)
                # [b'[2736', b']2737', b'(11000', b')11000',
                # b'[2736', b']2737', b'(11000', b')11000']
            else:
                # Values for channels which are not in the list will be set to zero.
                chs_decoded = [el.decode('ascii') for el in CHs]
                ch_lst_decoded = list(set(el.decode('ascii')[0] for el in ch_lst))
                zero_ch_lst = [el.encode('ascii') for el in chs_decoded if el not in ch_lst_decoded]
                ch_lst = []

            self.display_content(channel_value_row, zero_ch_lst)

        # For testing purpose only the first parameter should be set to 200.
        root.after(1, self.update_numbers, root, ser_dev, ch_lst)

    def digit_status(self) -> list:
        """digit_status"""

        digits = self.__digit

        return digits

    def number_status(self) -> list:
        """number_status"""

        number = self.__number

        return number
