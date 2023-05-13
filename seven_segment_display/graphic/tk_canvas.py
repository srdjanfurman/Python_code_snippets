# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman
"""

import tkinter as tk

from more_itertools import nth

from common.const import FONT


class TkCanvas:
    """TkCanvas class"""

    # No need for public methods.
    # pylint: disable=too-few-public-methods
    def __init__(self, root: tk.Tk, axis_titles) -> None:
        self.__axis_titles = axis_titles

        self.canvas = tk.Canvas(root, width=1110, height=980, bg='black')

        self.canvas.create_text(
            80, 200, text=nth(self.__axis_titles, 0), fill='white', font=FONT)
        self.canvas.create_text(
            80, 400, text=nth(self.__axis_titles, 1), fill='white', font=FONT)
        self.canvas.create_text(
            80, 600, text=nth(self.__axis_titles, 2), fill='white', font=FONT)
        self.canvas.create_text(
            80, 800, text=nth(self.__axis_titles, 3), fill='white', font=FONT)
        self.canvas.create_text(
            400, 40, text=nth(self.__axis_titles, 4), fill='white', font=FONT)
        self.canvas.create_text(
            900, 40, text=nth(self.__axis_titles, 5), fill='white', font=FONT)

        self.canvas.pack()
