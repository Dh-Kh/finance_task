import openpyxl
from database import retrieve_fromDb

def createExcel() -> str:
    data = retrieve_fromDb()
    if not data:
        return "data.xlsx"
    else:
        workbook = openpyxl.Workbook()
        sheet = workbook.active 
        sheet.append(["datetime", "exchange_rate"])
        for row in data:
            formatted_datetime = row[0].strftime("%d.%m.%Y %H:%M:%S")
            sheet.append([formatted_datetime, float(row[1])])
        workbook.save("data.xlsx")
        return "data.xlsx"
    