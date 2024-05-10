import openpyxl
from database import retrieve_fromDb
from psycopg2 import Error

def createExcel() -> str:
    workbook = openpyxl.Workbook()
    sheet = workbook.active 
    sheet.append(["datetime", "exchange_rate"])
    
    try:
        data = retrieve_fromDb()
        if not data:
            workbook.save("data.xlsx")
            return "data.xlsx"
        else:
            for row in data:
                formatted_datetime = row[0].strftime("%d.%m.%Y %H:%M:%S")
                sheet.append([formatted_datetime, float(row[1])])
            workbook.save("data.xlsx")
            return "data.xlsx"
    except Error:
        workbook.save("data.xlsx")
        return "data.xlsx"
    
    