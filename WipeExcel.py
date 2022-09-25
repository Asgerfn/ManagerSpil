import pandas as pd
import os
import openpyxl
from openpyxl import Workbook, load_workbook


def LengthOfExcel():
    wb = load_workbook("kamp.xlsx")
    ws = wb.active 
    AntalSpillere = 0
    for i in range(2,500): 
        val = ws['A'+str(i)].value
        if val is not None:
            AntalSpillere += 1
    return(AntalSpillere)

AntalSpillere = (LengthOfExcel())+1

def slette(x):
    wb = load_workbook("kamp.xlsx")
    ws = wb.active 
    for i in range(2,AntalSpillere+2): 
        ws['B'+str(i)].value = 0
    open("BrugteLinks.txt", 'w').close()
    
    print("slet")
    wb.save("kamp.xlsx")



#print(slette(1))