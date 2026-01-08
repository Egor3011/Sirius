from openpyxl import load_workbook
from config import exel_file


def append_ex(info):
    wb = load_workbook(exel_file)
    ws = wb['data']
    ws.append(info)
    wb.save(exel_file)
    wb.close()