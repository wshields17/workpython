import numpy as np 
import openpyxl
xlname = "spdata.xlsx"
wb = openpyxl.load_workbook(xlname)
print (wb.get_sheet_names())