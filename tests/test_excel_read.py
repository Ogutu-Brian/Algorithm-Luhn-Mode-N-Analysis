from luhn.luhn import get_required_data
import unittest


class TestExcelRead(unittest.TestCase):
    """Tests accurate reading of excel file"""

    def test_length_document(self):
        """Tests if the length of pan numbers in file is equal to length of pan numbers read from file
        """
        expected_length = 1013
        actual_length = len(get_required_data(
            "Uday - 1K Sample PAN for Upwork - 24-12-2018.xlsx"))
        message = "Expected {} but returned {}".format(
            expected_length, actual_length)
        self.assertEqual(expected_length, actual_length, message)


if __name__ == "__main__":
    unittest.main(exit=False)
