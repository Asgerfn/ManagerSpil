
from tokenize import Ignore
from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
import openpyxl
import numpy as np
from openpyxl import Workbook, load_workbook
from ExcelFormator import *
from HelpFunctions import *
from WipeExcel import *



HjemmmeBaneLink = ["https://www.badmintonplayer.dk/DBF/HoldTurnering/Stilling/#5,2022,14816,1,1,,425312,1148,","https://www.badmintonplayer.dk/DBF/HoldTurnering/Stilling/#5,2022,14829,1,1,,425535,1148,"]
UdebaneLink = ["https://www.badmintonplayer.dk/DBF/HoldTurnering/Stilling/#5,2022,14849,1,10,,425869,1148,","https://www.badmintonplayer.dk/DBF/HoldTurnering/Stilling/#5,2022,14849,1,10,,425869,1148,"]


def udebane(x): 
    wb = load_workbook("kamp.xlsx")
    ws = wb.active
    Liste = listOfPeople()
    NavneLængdeListe = (NavneLængde(Liste))
    brugteNavne = []
    for i in range(500,len(x)-13): 
        for j in range(1,len(Liste)): 
            if (x[i:i+NavneLængdeListe[j]] == Liste[j]) and (Liste[j] not in brugteNavne):
                excelNummer = people(Liste[j],Liste)+1 
                brugteNavne.append(Liste[j])
                ws['B'+str(excelNummer)].value = ws['B'+str(excelNummer)].value+float(helpUdebane(x,Liste[j],excelNummer))
                break
    wb.save("kamp.xlsx")   
    newExcel(længdeexcel)
    return()
#print(udebane(finalTekst))

def Hjemmebane(x): 
    wb = load_workbook("kamp.xlsx")
    ws = wb.active
    Liste = listOfPeople()
    NavneLængdeListe = (NavneLængde(Liste))
    brugteNavne = []

    for i in range(500,len(x)-13): 
        for j in range(1,len(Liste)): 
            
            if (x[i:i+NavneLængdeListe[j]] == Liste[j]) and (Liste[j] not in brugteNavne):
                excelNummer = people(Liste[j],Liste)+1 
                point = float(helpHjemmebane(x,Liste[j],excelNummer))
                
                ws['B'+str(excelNummer)].value = ws['B'+str(excelNummer)].value+point
                #ws['E'+str(excelNummer)].value = ws['E'+str(excelNummer)].value+sæt
                brugteNavne.append(Liste[j])
                break
    wb.save("kamp.xlsx")  
    newExcel(længdeexcel) 
    return()
#print(Hjemmebane(finalTekst))

 
Hjemmelinjer = []
Hjemmefil = open("Hjemmebane.txt", "r")
Hjemmelinjer = Hjemmefil.readlines()
gentagHjemmeliste = []
for line in Hjemmelinjer:
    gentagHjemmeliste.append((line.strip()))
    
    
with open("Hjemmebane.txt", "a") as Hjemmebanen: 
    for i in range(len(HjemmmeBaneLink)): 
        if HjemmmeBaneLink[i] not in gentagHjemmeliste:
            Hjemmebanen.write(HjemmmeBaneLink[i] +"\n") 

  

Udelinjer = []
udefil = open("Udebane.txt", "r")
Udelinjer = udefil.readlines()
gentagUdeliste = []
for line in Udelinjer:
    gentagUdeliste.append((line.strip()))

with open("Udebane.txt", "a") as Udebanen: 
    for i in range(len(UdebaneLink)): 
        if UdebaneLink[i] not in gentagUdeliste:
            Udebanen.write(UdebaneLink[i] +"\n")


brugtelinks = open("BrugteLinks.txt","a")
linjebrugt = open("BrugteLinks.txt","r")
Brugtelinjer = linjebrugt.readlines()



def kørSpil(x,y,link,brugtLinks): 
    for i in range(len(x)): 
        if x[i] not in brugtLinks: 
            
            print("Hjemmebane holdkamp kører... \n")
            PATH = "C:\webdrivers\chromedriver.exe" 
            driver = webdriver.Chrome(PATH)
            driver.get(x[i])
            main = driver.find_element_by_id("aspnetForm")
            tekst = str(main.text)
            finalTekst = (fjernNavne(tekst))
            Hjemmebane(finalTekst)
            print("Hejmmebane holdkamp opdateret nummer",i, "\n")
            if x[i] not in brugtLinks: 
                link.write(x[i])
    for j in range(len(y)): 
        if y[j] not in brugtLinks: 
        
            print("Udebane holdkamp kører... \n")
            PATH = "C:\webdrivers\chromedriver.exe" 
            driver = webdriver.Chrome(PATH)
            driver.get(y[j])
            main = driver.find_element_by_id("aspnetForm")
            tekst = str(main.text)
            finalTekst = (fjernNavne(tekst))
            udebane(finalTekst)
            print("Udebane holdkamp opdateret \n")
            if y[j] not in brugtLinks:
                link.write(y[j])
    return("så er spillet klar!")
print(kørSpil(Hjemmelinjer,Udelinjer,brugtelinks,Brugtelinjer))

