from luhn.luhn import (split_pan, mapping_to_code_points,
                       double, is_sum_mod_10, decimal_to_base_n, Reduce, is_mod_n)
import unittest


class TestStringManipulation(unittest.TestCase):
    """Tests for data manipulation on the pan numbers"""

    def test_string_split(self):
        """tets if the pan_number is split well into individual alphabets and digits
        """
        expected_list = ['A', 'A', 'D', 'C', 'E', '2', '7', '5', '7', 'L']
        actual_list = "AADCE2757L"
        actual_list = split_pan(actual_list)
        message = "Expected {} but returned {}".format(
            expected_list, actual_list)
        self.assertEqual(actual_list, expected_list, message)

    def test_number_mapping(self):
        """tests if the number is correctly mapped to the correct ascii codes
        """
        expected_list = [10, 10, 13, 12, 14, 2, 7, 5, 7, 21]
        actual_list = mapping_to_code_points(
            ['A', 'A', 'D', 'C', 'E', '2', '7', '5', '7', 'L'])
        message = "Expected {} but returned {}".format(
            expected_list, actual_list)
        self.assertEqual(expected_list, actual_list, message)

    def test_check_sum(self):
        """test if the checksum list is accurate"""
        expected_list = [1, 2, 4, 6, 5, 4, 7, 10, 7, 24]
        actual_list = double([1, 1, 4, 3, 5, 2, 7, 5, 7, 12])
        message = "Expected {} but returned {}".format(
            expected_list, actual_list)
        self.assertEqual(expected_list, actual_list, message)

    def test_mod_10(self):
        """Tests if the sum is in mod 10
        """
        expected_value = True
        actual_value = is_sum_mod_10([1, 2, 4, 6, 5, 4, 7, 10, 7, 24])
        message = "Expected {} but returned {}".format(
            expected_value, actual_value)
        self.assertEqual(expected_value, actual_value, message)

    def test_decimal_to_base_n(self):
        """Tests the conversion of any number into a given base"""
        expected_value = 14
        actual_value = decimal_to_base_n(10, 6)
        message = "Expected {} but returned {}".format(
            expected_value, actual_value)
        self.assertEqual(expected_value, actual_value, message)

        expected_value = 10
        actual_value = decimal_to_base_n(6, 6)
        message = "Expected {} but returned {}".format(
            expected_value, actual_value)
        self.assertEqual(expected_value, actual_value, message)

        expected_value = 2
        actual_value = decimal_to_base_n(2, 6)
        message = "Expected {} but returned {}".format(
            expected_value, actual_value)
        self.assertEqual(expected_value, actual_value, message)

    def test_reduction_of_list(self):
        """Tests if a list has been resuces successfully to the required number"""
        expected_list = [1, 2, 4, 6, 5, 4, 7, 1, 7, 6]
        actual_list = Reduce([1, 2, 4, 6, 5, 4, 7, 10, 7, 24])
        message = "Expected {} but returned {}".format(
            expected_list, actual_list)
        self.assertEqual(expected_list, actual_list, message)

    def test_is_mod_n(self):
        """Checks if a given number is of a given mod using modular arithmetic"""
        expected = True
        actual = is_mod_n(70, 35)
        message = "Expected {} but returned {}".format(expected, actual)
        self.assertEqual(expected, actual, message)

    def test_is_not_mod_n(self):
        """Checks if a given number is not of mod n using modular arithmetic"""
        expected = False
        actual = is_mod_n(71, 35)
        message = "Expected {} but returned {}".format(
            expected, actual)
        self.assertEqual(expected, actual, message)
