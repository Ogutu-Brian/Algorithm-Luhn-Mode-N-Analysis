from luhn.luhn import (split_pan, mapping_to_number, checksum)
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
        expected_list = [1, 1, 4, 3, 5, 2, 7, 5, 7, 12]
        actual_list = mapping_to_number(
            ['A', 'A', 'D', 'C', 'E', '2', '7', '5', '7', 'L'])
        message = "Expected {} but returned {}".format(
            expected_list, actual_list)
        self.assertEqual(expected_list, actual_list, message)

    def test_check_sum(self):
        """test if the checksum list is accurate"""
        expected_list = [1, 2, 4, 6, 5, 4, 7, 10, 7, 24]
        actual_list = checksum([1, 1, 4, 3, 5, 2, 7, 5, 7, 12])
        message = "Expected {} nut returned {}".format(
            expected_list, actual_list)
        self.assertEqual(expected_list, actual_list, message)
