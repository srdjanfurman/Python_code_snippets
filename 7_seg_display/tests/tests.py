# -*- coding: utf-8 -*-

"""
Created on Dec 12, 2021

@author: furman

Run unittests and check unittest coverage
    7_seg_display$ coverage run -m unittest discover && coverage report -m

"""

import io
import unittest
from contextlib import redirect_stdout

from common.utils import generate_test_data, generate_test_data_dyn
from data.data_set import digits_data, numbers_data
from disp.display_dev import Display
from disp.tk_canvas import TkCanvas
from disp.tk_root import TkRoot


class TestTkRoot(unittest.TestCase):
    """TestTkRoot class"""

    def setUp(self) -> None:
        self.root = TkRoot()

    def tearDown(self) -> None:
        pass

    def test_tk_root(self):
        """test_tk_root"""

        self.assertIsInstance(self.root, TkRoot)


class TestTkCanvas(unittest.TestCase):
    """TestTkCanvas class"""

    def setUp(self) -> None:
        self.root = TkRoot()
        self.canvas = TkCanvas(self.root.root)

    def tearDown(self) -> None:
        pass

    def test_tk_canvas(self):
        """test_tk_canvas"""

        self.assertIsInstance(self.canvas, TkCanvas)


class TestDisplayClass(unittest.TestCase):
    """TestDisplayClass class"""

    def setUp(self) -> None:
        self.root = TkRoot()
        self.canvas = TkCanvas(self.root.root)
        self.display = Display(self.canvas.canvas)

    def tearDown(self) -> None:
        pass

    def test_update_numbers(self) -> None:
        """test_update_numbers"""

        with redirect_stdout(io.StringIO()) as ctx:
            self.root.root.after(1, self.display.update_numbers(self.root.root, None, []))

        print_message = ctx.getvalue().rstrip('\n')

        self.assertEqual("b'[1'", print_message)

    def test_display_content(self) -> None:
        """test_display_content"""

        digits = self.display.digit_status()
        self.assertListEqual(digits, digits_data)

        numbers = self.display.number_status()
        self.assertListEqual(numbers, numbers_data)

        try:
            self.display.display_content(b'[}1', [])
        except ValueError as val_err:
            self.assertIsInstance(val_err, ValueError)

        self.display.display_content(b'[99', [])
        self.display.display_content(b'[100', [])
        self.display.display_content(b'[1000', [])
        self.display.display_content(b'[10000', [])
        self.display.display_content(b'[10009', [])
        self.display.display_content(b'[10999', [])
        self.display.display_content(b'[11000', [])
        self.display.display_content(b'[12000', [])
        self.display.display_content(b'[12001', [])

        try:
            self.display.display_content('[1', [])
        except TypeError as typ_err:
            self.assertIsInstance(typ_err, TypeError)


class TestGeneric(unittest.TestCase):
    """TestGeneric class"""

    def setUp(self) -> None:
        self.data = iter([b'[1', b']2', b'(3', b')4', b'{5', b'}6', b';7'])

    def tearDown(self) -> None:
        pass

    def test_generate_data(self) -> None:
        """test_generate_data"""

        self.assertEqual(generate_test_data(self.data), b'[1')
        self.assertEqual(generate_test_data(self.data), b']2')
        self.assertEqual(generate_test_data(self.data), b'(3')
        self.assertEqual(generate_test_data(self.data), b')4')
        self.assertEqual(generate_test_data(self.data), b'{5')
        self.assertEqual(generate_test_data(self.data), b'}6')
        self.assertEqual(generate_test_data(self.data), b';7')
        self.assertEqual(generate_test_data(self.data), b'')
        self.assertEqual(generate_test_data(self.data), b'')

    def test_generate_data_dyn(self) -> None:
        """test_generate_data_dyn"""

        data_dyn = generate_test_data_dyn(0, 5, 1)  # 8 * 5 = 40 elements.
        data_dyn_flat = [item for sublist in data_dyn for item in sublist]
        # print(len(data_dyn_flat))
        data_dyn_flat = iter(data_dyn_flat)

        # Check the 1st and the 2nd value.
        self.assertEqual(next(data_dyn_flat), b'[0')
        self.assertEqual(next(data_dyn_flat), b']0')

        # Evaluate the next 24 values.
        _ = [next(data_dyn_flat) for _ in range(24)]

        # Check values.
        self.assertEqual(next(data_dyn_flat), b'(3')
        self.assertEqual(next(data_dyn_flat), b')3')

        # Evaluate the next 20 values.
        _ = [next(data_dyn_flat) for _ in range(10)]

        # Check values.
        self.assertEqual(next(data_dyn_flat), b';4')
        self.assertEqual(next(data_dyn_flat), b':4')


class TestSerial(unittest.TestCase):
    """TestSerial class"""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_serial(self) -> None:
        """test_serial"""
