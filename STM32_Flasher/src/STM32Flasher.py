#!/usr/bin/env python

"""
Created on Dec 23, 2015

@author: sfurman


GUI application for programming the STM32 MCUs.

Prerequisites:
  st-flash - Flash binary files to the STM32 device.
"""

from subprocess import Popen, PIPE

import wx
from wx.lib.filebrowsebutton import FileBrowseButton


class MyFrame(wx.Frame):
    def __init__(self, parent, app_title, app_size):
        wx.Frame.__init__(self, parent, wx.ID_ANY, app_title, size=app_size)

        panel = wx.Panel(self)

        # Mask file browser to look for .bin files.
        # Explain browse_button.
        self.browse_button = FileBrowseButton(panel,
                                              labelText="Select a BIN file:",
                                              fileMask="*.bin")
        # Explain flash_button.
        self.flash_button = wx.Button(panel, wx.ID_ANY, "Flash")
        self.flash_button.Bind(wx.EVT_BUTTON, self.on_flash)

        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        output_txt = "st-flash says:\n"
        self.text_ctrl.AppendText(output_txt)

        # Setup the layout with sizers.
        # Create a horizontal_sizer space.
        horiz_sizer = wx.BoxSizer(wx.HORIZONTAL)
        horiz_sizer.Add(self.browse_button, 1, wx.ALIGN_CENTER_VERTICAL)
        horiz_sizer.Add(self.flash_button, 0, wx.ALIGN_CENTER_VERTICAL)

        # Create a vertical_sizer space.
        vertical_sizer = wx.BoxSizer(wx.VERTICAL)
        vertical_sizer.Add(horiz_sizer, 0, wx.EXPAND | wx.ALL, 10)
        vertical_sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 10)

        # Vertical sizer space contains horizontal sizer space, so set them.
        panel.SetSizer(vertical_sizer)

    def on_flash(self, evt):
        filename = self.browse_button.GetValue()
        if filename:
            p = Popen(
                ['st-flash', 'write', filename, '0x8000000'],
                stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output = p.communicate(
                b"input data that is passed to subprocess' stdin")
            self.text_ctrl.AppendText(output[0])
            self.text_ctrl.AppendText(output[1])
        else:
            wx.MessageBox("Missing or invalid BIN file", "Error")


app = wx.App(0)
# Create a MyFrame instance and show the frame.
appTitle = "STM32Flasher"
width = 1000
height = 400
MyFrame(None, appTitle, (width, height)).Show()
app.MainLoop()
