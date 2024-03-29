# -*- coding: utf-8 -*-

""" Tk root """

import tkinter as tk


class TkRoot:
    """TkRoot class"""

    # No need for public methods.
    # pylint: disable=too-few-public-methods
    def __init__(self, title: str) -> None:
        self.__title = title
        self.root = tk.Tk()
        self.root.title(self.__title)
