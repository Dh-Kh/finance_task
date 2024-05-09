import openpyxl
from .database import retrieve_fromDb

def createExcel() -> None:
    data = retrieve_fromDb()
    workbook = openpyxl.Workbook()
    sheet = workbook.active 
    sheet.append(["datetime", "exchange_rate"])
    for row in data:
        sheet.append([row[0], float(row[1])])
    workbook.save("data.xlsx")
    