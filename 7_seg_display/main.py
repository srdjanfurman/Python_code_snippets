# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman

Emulator of the 7 segment LED disp.
"""

from serial.serialutil import SerialException

from common.const import DEV
from disp.display_dev import Display
from disp.tk_canvas import TkCanvas
from disp.tk_root import TkRoot
from ser.serial_dev import SerialDevice

if __name__ == '__main__':
    root_obj = TkRoot()
    canvas_obj = TkCanvas(root_obj.root)

    try:
        SD = SerialDevice(DEV)
        SD.open_serial_device()
    except SerialException as e:
        print(e.strerror)
        print('Starting DEMO...')
        SD = None

    d = Display(canvas_obj.canvas)
    root_obj.root.after(1, d.update_numbers(root_obj.root, SD, []))
    root_obj.root.mainloop()

    if SD:
        SD.close_serial_device()
