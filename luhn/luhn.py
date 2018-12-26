import xlrd
from typing import List


def get_required_data(file: str)->List:
    """
    Opens an file and retunrns the data in first column of the sheet
    """
    workbook = xlrd.open_workbook(file)
    sheets = workbook.sheet_names()
    required_data = []
    for sheet_name in sheets:
        sh = workbook.sheet_by_name(sheet_name)
        for rownum in range(sh.nrows):
            row_values = sh.row_values(rownum)
            required_data.append((row_values[0]))
    return required_data


def split_pan(pan: str)->None:
    """converts every pan number into a comma separated list
    >>splitpan('abc')
    >>a,b,c
    """


if __name__ == "__main__":
    dataset = get_required_data(
        "Uday - 1K Sample PAN for Upwork - 24-12-2018.xlsx")
    print("The length of the dataset is {}".format(len(dataset)))
