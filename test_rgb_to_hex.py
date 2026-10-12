
import unittest
from rgb_to_hex import rgb_to_hex


class TestRGBToHex(unittest.TestCase):

    def test_basic_conversion(self):
        self.assertEqual(rgb_to_hex(119, 119, 199), "#7777C7")

    def test_black(self):
        self.assertEqual(rgb_to_hex(0, 0, 0), "#000000")

    def test_white(self):
        self.assertEqual(rgb_to_hex(255, 255, 255), "#FFFFFF")

    def test_red(self):
        self.assertEqual(rgb_to_hex(255, 0, 0), "#FF0000")

    def test_green(self):
        self.assertEqual(rgb_to_hex(0, 255, 0), "#00FF00")

    def test_blue(self):
        self.assertEqual(rgb_to_hex(0, 0, 255), "#0000FF")

    def test_hexadecimal_letters(self):
        self.assertEqual(rgb_to_hex(10, 11, 12), "#0A0B0C")

    def test_all_hexadecimal_letters(self):
        self.assertEqual(rgb_to_hex(171, 205, 239), "#ABCDEF")

    def test_leading_zeroes(self):
        self.assertEqual(rgb_to_hex(1, 2, 3), "#010203")

    def test_values_at_15(self):
        self.assertEqual(rgb_to_hex(15, 15, 15), "#0F0F0F")

    def test_values_at_16(self):
        self.assertEqual(rgb_to_hex(16, 16, 16), "#101010")

    def test_values_at_254(self):
        self.assertEqual(rgb_to_hex(254, 254, 254), "#FEFEFE")

    def test_negative_red(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(-1, 0, 0)

    def test_negative_green(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, -1, 0)

    def test_negative_blue(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 0, -1)

    def test_red_above_255(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(256, 0, 0)

    def test_green_above_255(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 256, 0)

    def test_blue_above_255(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 0, 256)

    def test_float_red(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(12.5, 0, 0)

    def test_float_green(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 12.5, 0)

    def test_float_blue(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 0, 12.5)

    def test_string_red(self):
        with self.assertRaises(ValueError):
            rgb_to_hex("10", 0, 0)

    def test_string_green(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, "10", 0)

    def test_string_blue(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 0, "10")

    def test_boolean_red(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(True, 0, 0)

    def test_boolean_green(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, True, 0)

    def test_boolean_blue(self):
        with self.assertRaises(ValueError):
            rgb_to_hex(0, 0, True)


if __name__ == "__main__":
    unittest.main()