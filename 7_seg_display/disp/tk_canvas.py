# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman
"""

import tkinter as tk

from common.const import FONT


class TkCanvas:
    """TkCanvas class"""

    # No need for public methods.
    # pylint: disable=too-few-public-methods
    def __init__(self, root: tk.Tk) -> None:
        self.canvas = tk.Canvas(root, width=1110, height=980, bg='black')
        self.canvas.create_text(80, 200, text='ADC1:', fill='white', font=FONT)
        self.canvas.create_text(80, 400, text='ADC2:', fill='white', font=FONT)
        self.canvas.create_text(80, 600, text='ADC3:', fill='white', font=FONT)
        self.canvas.create_text(80, 800, text='ADC4:', fill='white', font=FONT)
        self.canvas.create_text(400, 40, text='CH1:', fill='white', font=FONT)
        self.canvas.create_text(900, 40, text='CH2:', fill='white', font=FONT)
        self.canvas.pack()
