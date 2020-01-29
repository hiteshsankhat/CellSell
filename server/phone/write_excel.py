import xlwt
from xlwt import Workbook
from django.db import connection


def sqlReadData(table):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM {0} ".format(table)
        cursor.execute(sql)
        row = cursor.fetchall()
    return row 

def addDataInSheet(sheet, data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i+1, j, data[i][j])
    return sheet

def addSheetOneData(wb) :
    sheet1 = wb.add_sheet("Brand")

    sheet1.write(0, 0, "Name")
    sheet1.write(0, 1, "Name")
    sheet1.write(0, 2, "Image Path")

    data = sqlReadData("BrandName")
    sheet1 = addDataInSheet(sheet1, data)
    return sheet1
    

def addSheetTwoData(wb):
    sheet2 = wb.add_sheet("ModelNumber")

    sheet2.write(0, 0, "BrandId")
    sheet2.write(0, 1, "BrandName")
    sheet2.write(0, 2, "Name")
    sheet2.write(0, 3, "Image Path")

    data = sqlReadData("ModelNumber")
    sheet2 = addDataInSheet(sheet2, data)
    return sheet2
    

def addSheetThreeData(wb):
    sheet3 = wb.add_sheet("Varient")
    
    sheet3.write(0, 0, "Model ID")
    sheet3.write(0, 1, "Model Name")
    sheet3.write(0, 2, "RAM")
    sheet3.write(0, 3, "Storage")
    sheet3.write(0, 4, "Price")
    sheet3.write(0, 5, "No Issue")
    sheet3.write(0, 6, "Below 11 month")
    sheet3.write(0, 7, "Aelow 11 month")
    sheet3.write(0, 8, "Charger")
    sheet3.write(0, 9, "earphone")
    sheet3.write(0, 10, "Box")
    sheet3.write(0, 11, "New")
    sheet3.write(0, 12, "Excellent")
    sheet3.write(0, 13, "Fair")

    data = sqlReadData("Varient")
    sheet3 = addDataInSheet(sheet3, data)
    return sheet3

def export(response):
    wb = Workbook(encoding='utf-8')
    sheet1 = addSheetOneData(wb)
    sheet2 = addSheetTwoData(wb)
    sheet3 = addSheetThreeData(wb)
    wb.save(response)
    return response