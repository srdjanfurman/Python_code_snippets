"""
Created on Sep 15, 2014

@author: sfurman
"""


class Color(object):
    def __init__(self):
        pass

    TEXT_RESET_ALL = '\033[0m'
    TEXT_RESET = '\033[39m'  # '\033[49m'
    TEXT_BLACK = '\033[30m'
    TEXT_RED = '\033[31m'
    TEXT_GREEN = '\033[32m'
    TEXT_YELLOW = '\033[33m'
    TEXT_BLUE = '\033[34m'
    TEXT_MAGENTA = '\033[35m'
    TEXT_CYAN = '\033[36m'
    TEXT_WHITE = '\033[37m'
    TEXT_BRIGHT = '\033[1m'
    TEXT_NORMAL = '\033[22m'
    BACKGROUND_BLACK = '\033[40m'
    BACKGROUND_RED = '\033[41m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_YELLOW = '\033[43m'  # olive
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_MAGENTA = '\033[45m'  # purple
    BACKGROUND_CYAN = '\033[46m'  # light blue
    BACKGROUND_WHITE = '\033[47m'  # grey

# The only ANSI sequences that colorama converts into win32 calls are:
#
# # TEXT:
# ESC [ 0 m       # reset all (colors and brightness)
# ESC [ 1 m       # bright
# ESC [ 2 m       # dim (looks same as normal brightness)
# ESC [ 22 m      # normal brightness
#
# # FOREGROUND:
# ESC [ 30 m      # black
# ESC [ 31 m      # red
# ESC [ 32 m      # green
# ESC [ 33 m      # yellow
# ESC [ 34 m      # blue
# ESC [ 35 m      # magenta
# ESC [ 36 m      # cyan
# ESC [ 37 m      # white
# ESC [ 39 m      # reset
#
# # BACKGROUND:
# ESC [ 40 m      # black
# ESC [ 41 m      # red
# ESC [ 42 m      # green
# ESC [ 43 m      # yellow
# ESC [ 44 m      # blue
# ESC [ 45 m      # magenta
# ESC [ 46 m      # cyan
# ESC [ 47 m      # white
# ESC [ 49 m      # reset
#
# # cursor positioning
# ESC [ y;x H     # position cursor at x across, y down
#
# # clear the screen
# ESC [ mode J    # clear the screen. Only mode 2 (clear entire screen)
#                 # is supported. It should be easy to add other modes,
#                 # let me know if that would be useful.
