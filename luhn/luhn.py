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


def mapping_to_code_points(pan_list: List)->List:
    """Maps non digit characters into equivalent ascii numbers
    >>>mapping_to_number(['A', 'A', 'D', 'C', 'E', '2', '7', '5', '7', 'L'])
    >>>[1, 1, 4, 3, 5, 2, 7, 5, 7, 12]
    """
    new_pan_list = []
    for character in pan_list:
        if character.isdigit():
            new_pan_list.append(int(character))
        else:
            new_pan_list.append(int(ord(character.lower()) - 96)+9)
    return new_pan_list


def double(pan_list: List)->List:
    """doubles the digits in accordance with luhn algorithm
    >>>checksum([1, 1, 4, 3, 5, 2, 7, 5, 7, 12])
    >>>[1, 2, 4, 6, 5, 4, 7, 10, 7, 24]
    """
    index = len(pan_list) - 1
    while index > 0:
        pan_list[index] += pan_list[index]
        pan_list[index] = decimal_to_base_n(pan_list[index], 35)
        index -= 2
    return pan_list


def is_sum_mod_10(pan_list: List)->bool:
    """Checks if the sum mode 10 is 0 or not
    >>>sum_mod_10([1, 2, 4, 6, 5, 4, 7, 10, 7, 24])
    >>>True
    """
    return sum(pan_list) % 10 == 0


def decimal_to_base_n(number: int, base: int)->int:
    """Converts a decimal number into a given base
    >>>decimal_to_base_n(10,6)
    >>>14
    """
    m = []
    while number != 0:
        d = int(number/base)
        r = number % base
        m.insert(0, r)
        number = d
    index = len(m) - 1
    multiplier = 1
    values = []
    while index >= 0:
        values.append(m[index]*multiplier)
        multiplier *= 10
        index -= 1
    return sum(values)


def Reduce(pan_list: List)->List:
    """Reduces multiple digit numbers into single digits depending on the base
    >>>Reduce([1, 2, 4, 6, 5, 4, 7, 10, 7, 24])
    >>>[1, 2, 4, 6, 5, 4, 7, 1, 7, 6]
    """
    reduced_list = []
    for item in pan_list:
        if item >= 10:
            reduced_list.append(sum([int(digit) for digit in str(item)]))
        else:
            reduced_list.append(item)
    return reduced_list


def is_mod_n(number: int, base: int)->bool:
    """Checks if number is of a given mode or not"
    >>>is_mod_n(70,35)
    >>>True
    >>>is_mod_n(36,35)
    >>>False
    """
    return number % base == 0


if __name__ == "__main__":
    dataset = get_required_data(
        "Uday - 1K Sample PAN for Upwork - 24-12-2018.xlsx")
    split_data = split_pan(dataset)
    mapped_data = [mapping_to_code_points(item) for item in split_data]
    # reduced_data = [Reduce(item) for item in base_35_data]
    doubled_data = []
    reduced_data = []
    valid_pans = []
    invalid_pans = []
    for item in mapped_data:
        doubled_list = double(item[0:9])
        doubled_list.append(item[9])
        doubled_data.append(doubled_list)
    for item in mapped_data:
        reduced_list = Reduce(item)
        reduced_list.append(item[9])
        reduced_data.append(reduced_list)
    for item in reduced_data:
        if is_mod_n(sum(item), 35):
            valid_pans.append(item)
        else:
            invalid_pans.append(item)
    print("The number of valid PAN numbers is {}".format(len(valid_pans)))
    print("The number of valid PAN numbers is {}".format(len(invalid_pans)))
