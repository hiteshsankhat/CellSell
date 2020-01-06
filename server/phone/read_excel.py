import xlrd
from django.db import connection

from . import models


def sqlDeleteAllFromTable(tableName):
    with connection.cursor() as coursor:
        sql = "Delete From {0}".format(tableName)
        coursor.execute(sql)
        sql = "DELETE FROM sqlite_sequence WHERE name='{0}'".format(tableName)
        coursor.execute(sql)



def sqlInsertIntoBrandName(name, icon):
    with connection.cursor() as cursor:
        sql = "INSERT INTO BrandName (name, brandIcon) VALUES('{0}', '{1}')".format(
            name, icon)
        cursor.execute(sql)

def sqlInsertIntoModelNumber(data):
    with connection.cursor() as cursor:
        sql = "SELECT id FROM BrandName WHERE name='{0}'".format(data[1])
        cursor.execute(sql)
        row = cursor.fetchall()

        sql = "INSERT INTO ModelNumber (brandID_id, name, modelImage)VALUES('{0}', '{1}', '{2}')".format(row[0][0], data[2], data[3])
        cursor.execute(sql)

def sqlInsertIntoVarient(data):
    with connection.cursor() as cursor:
        sql = "SELECT id FROM ModelNumber WHERE name='{0}'".format(data[1])
        cursor.execute(sql)
        row = cursor.fetchall()

        if row:
            sql = '''
            INSERT INTO Varient 
            (ram, storage, modelNumberId_id, price, billAboveThreeMonth
            , billBelowThreeMonth, hasBox, hasCharger, hasHeadPhone,
            isExcellent, isNew, isFair)
            VALUES(
                '{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}'
            )
            '''.format(data[2], data[3], row[0][0], data[4], data[7], data[6], data[10], data[8], data[9], data[12], data[11], data[13])
            cursor.execute(sql)
        else:
            print(data[1])


def insertALLData(loc):
    wb = xlrd.open_workbook(loc)
    sheet1 = wb.sheet_by_index(0)
    sheet2 = wb.sheet_by_index(1)
    sheet3 = wb.sheet_by_index(2)

    sqlDeleteAllFromTable('Varient')
    sqlDeleteAllFromTable('ModelNumber')
    sqlDeleteAllFromTable('BrandName')

    for i in range(1, sheet1.nrows):
        data = sheet1.row_values(i)
        sqlInsertIntoBrandName(data[0], data[1])
    
    for i in range(1, sheet2.nrows):
        data = sheet2.row_values(i)
        sqlInsertIntoModelNumber(data)

    for i in range(1, sheet3.nrows):
        data = sheet3.row_values(i)
        sqlInsertIntoVarient(data)