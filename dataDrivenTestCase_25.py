'''
Agenda
   Excel operations:
   2.)Writing data in Excel file
'''
import openpyxl
path="C:\\Users\\Dell\\PycharmProjects\\selenium\\data\\empWrite.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.active
# workbook.get_sheet_by_name("Sheet1")











