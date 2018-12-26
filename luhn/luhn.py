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


def split_pan(pan: str)->List:
    """converts every pan number into a comma separated list and returns the list
    >>splitpan('abc')
    >>>[a,b,c]
    """
    pan = list(pan)
    return pan


def mapping_to_number(pan_list: List)->List:
    """Maps non digit characters into equivalent ascii numbers
    >>>mapping_to_number(['A', 'A', 'D', 'C', 'E', '2', '7', '5', '7', 'L'])
    >>>[1, 1, 4, 3, 5, 2, 7, 5, 7, 12]
    """
    new_pan_list = []
    for character in pan_list:
        if character.isdigit():
            new_pan_list.append(int(character))
        else:
            new_pan_list.append(int(ord(character.lower()) - 96))
    return new_pan_list


def checksum(pan_list: List)->List:
    """does the summation of numbers in the list in accordance with luhn algorithm
    >>>checksum([1, 1, 4, 3, 5, 2, 7, 5, 7, 12])
    >>>[1, 2, 4, 6, 5, 4, 7, 10, 7, 24]
    """
    index = len(pan_list) - 1
    while index > 0:
        pan_list[index] += pan_list[index]
        index -= 2
    return pan_list


def is_sum_mod_10(pan_list: List)->bool:
    """Checks if the sum mode 10 is 0 or not
    >>>sum_mod_10([1, 2, 4, 6, 5, 4, 7, 10, 7, 24])
    >>>True
    """
    return sum(pan_list) % 10 == 0


if __name__ == "__main__":
    dataset = get_required_data(
        "Uday - 1K Sample PAN for Upwork - 24-12-2018.xlsx")
    split_data = split_pan(dataset)
    mapped_data = [mapping_to_number(item) for item in split_data]
    summed_data = [checksum(item) for item in mapped_data]
    for item in summed_data:
        if not is_sum_mod_10(item):
            print(item)
            print("The sum is {}".format(sum(item)))
            print("There was a glitch in the algorithm")
            break