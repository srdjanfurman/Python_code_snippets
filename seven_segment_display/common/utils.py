# -*- coding: utf-8 -*-

""" Utils """

from common.const import START, STOP, STEP, DATA


def generate_test_data_fixed() -> bytes:
    """
    Generate test data fixed.
    """

    try:
        return next(DATA)
    except StopIteration:
        pass

    return bytes()


def generate_test_data(lst: iter) -> bytes:
    """
    Generate test data.
    """

    try:
        return next(lst)
    except StopIteration:
        pass

    return bytes()


def generate_test_data_dyn(start=START, stop=STOP, step=STEP) -> list:
    """
    Generate test data dynamically, e.g.
    [b'[1', b']2', b'(3', b')4', b'{5', b'}6', b';7', b':8'
    b'[10000', b']10000', b'(10000', b')10000', b'{10000', b'}10000',
    b';10000', b':10000'...]
    following START, END and STEP constants.
    """

    return [[bytes(item.format(idx), 'utf-8') for item in
             ['[{}', ']{}', '({}', '){}', '{{{}', '}}{}', ';{}', ':{}']]
            for idx in range(start, stop, step)]
