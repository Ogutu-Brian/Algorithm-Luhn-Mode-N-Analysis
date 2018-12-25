import xlrd
from

def get_required_data()->list:
    workbook = xlrd.open_workbook(
        "Uday - 1K Sample PAN for Upwork - 24-12-2018.xlsx")
    sheets = workbook.sheet_names()
    required_data = []
    for sheet_name in sheets:
        sh = workbook.sheet_by_name(sheet_name)
        for rownum in range(sh.nrows):
            row_values = sh.row_values(rownum)
            required_data.append((row_values[0]))
    return required_data
