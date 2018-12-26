import unittest
import sys
sys.path.append('/home/Ogutu/Downloads/LuhnAlgorithm/')
from luhn.luhn import get_required_data


class TestExcelRead(unittest.TestCase):
    """Tests accurate reading of excel file"""

    def test_length_document(self):
        required_length = 1013
        actual_length = len(get_required_data(
            "Uday - 1K Sample PAN for Upwork - 24-12-2018.xlsx"))
        self.assertEqual(required_length, actual_length)


if __name__ == "__main__":
    unittest.main(exit=False)
