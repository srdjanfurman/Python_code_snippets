# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman
"""

# Testing ranges (from - to). See "Data format example" table in README.md file.
START = 0
STOP = 11
STEP = 1

# Counter speed.
DISP_SPEED = 0.1

TEST_LST = iter([
    b'[1', b']2', b'(3', b')4', b'{5', b'}6', b';7', b':8',
    b'[991', b']992', b'(993', b')994', b'{995', b'}996', b';997', b':998',
    b'[999', b']1000', b'(1001', b')1002', b'{1003', b'}1004', b';1005', b':9999',
    b'[10001', b']10002', b'(10003', b')10004', b'{10005', b'}10006', b';10007', b':10008',
    b'[10991', b']10992', b'(10993', b')10994', b'{10995', b'}10996', b';10997', b':10998',
    b'[12000', b']12000', b'(12000', b')12000', b'{12000', b'}12000', b';12000', b':12000',
    b'[12001', b']12001', b'(12001', b')12001', b'{12001', b'}12001', b';12001', b':12001',
    b'[10000', b']10000', b'(10000', b')10000', b'{10000', b'}10000', b';10000', b':10000'])

# DEV = '/dev/ttyUSB1'
DEV = '/dev/pts/1'

FONT = 'Helvetica 35 bold'

SEGMENTS = (
    (0, 0, 1, 0),  # top
    (1, 0, 1, 1),  # upper right
    (1, 1, 1, 2),  # lower right
    (0, 2, 1, 2),  # bottom
    (0, 1, 0, 2),  # lower left
    (0, 0, 0, 1),  # upper left
    (0, 1, 1, 1),  # middle
)

# Segments used for each digit; 0, 1 = off, on.
DIGITS = (
    # Digits.
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
    (0, 0, 0, 0, 0, 0, 0),  #
    # Letters.
    (1, 1, 1, 0, 1, 1, 1),  # A
    (0, 0, 1, 1, 1, 1, 1),  # b
    (1, 0, 0, 1, 1, 1, 0),  # C
    (0, 1, 1, 1, 1, 0, 1),  # d
    (1, 0, 0, 1, 1, 1, 1),  # E
    (1, 0, 0, 0, 1, 1, 1),  # F
    (0, 0, 0, 1, 1, 1, 1),  # t
    (0, 0, 1, 1, 1, 0, 1),  # o
    (1, 1, 0, 0, 1, 1, 1),  # p
    (0, 0, 0, 0, 1, 0, 1),  # r
    # Symbols.
    (0, 0, 0, 0, 0, 0, 1)  # -
)

#        mask           digit
# (1, 0, 0, 0, 0, 0, 0)    a
# (0, 1, 0, 0, 0, 0, 0)    b
# (0, 0, 1, 0, 0, 0, 0)    c
# (0, 0, 0, 1, 0, 0, 0)    d
# (0, 0, 0, 0, 1, 0, 0)    e
# (0, 0, 0, 0, 0, 1, 0)    f
# (0, 0, 0, 0, 0, 0, 1)    g


# A zero-indexed element is unique on Y position on the canvas.
# Others are on X positions.
# POS_FIRST_ROW = [20, 20, 120, 220, 320, 520, 620, 720, 820]
# POS_SECOND_ROW = [220, 20, 120, 220, 320, 520, 620, 720, 820]
# POS_THIRD_ROW = [420, 20, 120, 220, 320, 520, 620, 720, 820]
# POS_FOURTH_ROW = [620, 20, 120, 220, 320, 520, 620, 720, 820]

POS_FIRST_ROW = [100, 200, 320, 420, 520, 720, 820, 920, 1020]
POS_SECOND_ROW = [300, 200, 320, 420, 520, 720, 820, 920, 1020]
POS_THIRD_ROW = [500, 200, 320, 420, 520, 720, 820, 920, 1020]
POS_FOURTH_ROW = [700, 200, 320, 420, 520, 720, 820, 920, 1020]

# CHs = [b'[', b']', b'(', b')', b'{', b'}', b';', b':', b'%']
CHs = [b'[', b']', b'(', b')', b'{', b'}', b';', b':']

LENGTH = 70  # Digit length.
WIDTH = 15  # Digit width.
MAX_DIGITS = 32  # 1 number = 4 DIGITS max.
