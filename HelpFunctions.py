import re 
def helpUdebane(x:str,navn:str,nummer:int):
    pattern = "[0-9]+"
    point = 0
    HD = 0
    MD = 0
    DD = 0
    for j in range(len(x)-10):
        if x[j:j+8] == "Resultat": 
            Holdkampsresultat = (re.findall(pattern,x[j+9:j+14]))
            if int(Holdkampsresultat[-1]) == 0: 
                point = point-5
            elif int(Holdkampsresultat[-1]) > 6: 
                point = point+5
            else: 
                point = point+2
    for i in range(len(x)-20):  
        if x[i:i+len(navn)] == navn: 
            for k in range(80):
                if "HS" in x[i-k-2:i-k]: 
                    HSPoint = (re.findall(pattern,x[i:i+40+len(navn)]))
                    if len(HSPoint)%2 == 1: 
                        del HSPoint[-1]
                    if len(HSPoint) < 1: 
                        break
                    HSHerlevListe = []
                    HSModstanderListe = []
                    
                    for r in range(len(HSPoint)):
                        if r%2 == 0 : 
                            HSModstanderListe.append(HSPoint[r])
                        else: 
                            HSHerlevListe.append(HSPoint[r])
                    if int(HSHerlevListe[-1]) < 21 and int(HSModstanderListe[-1]) < 21: 
                        point=point+0
                    elif int(HSHerlevListe[-1]) > int(HSModstanderListe[-1]) : 
                        if len(HSHerlevListe) == 3: 
                                point=point+4 
                        else : 
                                point=point+5
                    else: 
                        if len(HSHerlevListe) == 3:
                                point=point+2
                        else: 
                                point=point+1
                    for j in range(len(HSHerlevListe)): 
                        if int(HSHerlevListe[j]) < 6: 
                            point = point-5
                        elif int(HSHerlevListe[j]) < 11: 
                            point = point-3
                        if int(HSModstanderListe[j]) < 6:
                            point = point+5
                        elif int(HSModstanderListe[j]) <11:
                            point = point +3 
                    break
                elif "HD" in x[i-k-2:i-k]: 
                    
                    if HD < 1: 
                        HD = 2
                        HDPoint = (re.findall(pattern,x[i:i+60+len(navn)]))
                        if (len(HDPoint))%2 == 1: 
                            del HDPoint[-1]
                        if len(HDPoint) < 1: 
                            break
                        HDHerlevListe = []
                        HDModstanderListe = []
                        for r in range(len(HDPoint)):
                            if r%2 == 0 : 
                                HDModstanderListe.append(HDPoint[r])
                            else: 
                                HDHerlevListe.append(HDPoint[r])
                        if int(HDHerlevListe[-1]) < 21 and int(HDModstanderListe[-1]) < 21: 
                            point=point+0
                        elif int(HDHerlevListe[-1]) > int(HDModstanderListe[-1]) : 
                            if len(HDHerlevListe) == 3: 
                                    point=point+4 
                            else : 
                                    point=point+5
                        else: 
                            if len(HDHerlevListe) == 3:
                                    point=point+2
                            else: 
                                    point=point+1
                        for j in range(len(HDHerlevListe)): 
                            if int(HDHerlevListe[j]) < 6: 
                                point = point-5
                            elif int(HDHerlevListe[j]) < 11: 
                                point = point-3
                            if int(HDModstanderListe[j]) < 6:
                                point = point+5
                            elif int(HDModstanderListe[j]) <11:
                                point = point +3 
                    break
                elif "MD" in x[i-k-2:i-k]: 
                    
                    if MD < 1: 
                        MD = 2
                        MDPoint = (re.findall(pattern,x[i:i+50+len(navn)]))
                        if (len(MDPoint))%2 == 1: 
                            del MDPoint[-1]
                        if len(MDPoint) < 1: 
                            break
                        MDHerlevListe = []
                        MDModstanderListe = []
                        for r in range(len(MDPoint)):
                            if r%2 == 0 : 
                                MDModstanderListe.append(MDPoint[r])
                            else: 
                                MDHerlevListe.append(MDPoint[r])
                        if int(MDHerlevListe[-1]) < 21 and int(MDModstanderListe[-1]) < 21: 
                            point=point+0
                        elif int(MDHerlevListe[-1]) > int(MDModstanderListe[-1]) : 
                            if len(MDHerlevListe) == 3: 
                                    point=point+4 
                            else : 
                                    point=point+5
                        else: 
                            if len(MDHerlevListe) == 3:
                                    point=point+2
                            else: 
                                    point=point+1
                        for j in range(len(MDHerlevListe)): 
                            if int(MDHerlevListe[j]) < 6: 
                                point = point-5
                            elif int(MDHerlevListe[j]) < 11: 
                                point = point-3
                            if int(MDModstanderListe[j]) < 6:
                                point = point+5
                            elif int(MDModstanderListe[j]) <11:
                                point = point +3 
                    break
                elif "DS" in x[i-k-2:i-k]: 
                    DSPoint = (re.findall(pattern,x[i:i+40+len(navn)]))
                    if len(DSPoint)%2 == 1: 
                        del DSPoint[-1]
                    if len(DSPoint) < 1: 
                        break
                    DSHerlevListe = []
                    DSModstanderListe = []
                    for r in range(len(DSPoint)):
                        if r%2 == 0 : 
                            DSModstanderListe.append(DSPoint[r])
                        else: 
                            DSHerlevListe.append(DSPoint[r])
                    if int(DSHerlevListe[-1]) < 21 and int(DSModstanderListe[-1]) < 21: 
                        point=point+0
                    elif int(DSHerlevListe[-1]) > int(DSModstanderListe[-1]) :
                     
                        if len(DSHerlevListe) == 3: 
                                point=point+4 
                        else : 
                                point=point+5
                    else: 
                        if len(DSHerlevListe) == 3:
                                point=point+2
                        else: 
                                point=point+1
                    for j in range(len(DSHerlevListe)): 
                        if int(DSHerlevListe[j]) < 6: 
                            point = point-5
                        elif int(DSHerlevListe[j]) < 11: 
                            point = point-3
                        if int(DSModstanderListe[j]) < 6:
                            point = point+5
                        elif int(DSModstanderListe[j]) <11:
                            point = point +3
                    break
                elif "DD" in x[i-k-2:i-k]: 
                    
                    if DD < 1: 
                        DD = 2
                        DDPoint = (re.findall(pattern,x[i:i+50+len(navn)]))
                        if len(DDPoint) < 2: 
                            break
                        if (len(DDPoint))%2 == 1: 
                            del DDPoint[-1]
                        if len(DDPoint) < 1 : 
                            break
                        DDHerlevListe = []
                        DDModstanderListe = []
                        for r in range(len(DDPoint)):
                            if r%2 == 0 : 
                                DDModstanderListe.append(DDPoint[r])
                            else: 
                                DDHerlevListe.append(DDPoint[r])
                        if int(DDHerlevListe[-1]) < 21 and int(DDModstanderListe[-1]) < 21: 
                            point=point+0
                        elif int(DDHerlevListe[-1]) > int(DDModstanderListe[-1]) : 
                            if len(DDHerlevListe) == 3: 
                                    point=point+4 
                            else : 
                                    point=point+5
                        else: 
                            if len(DDHerlevListe) == 3:
                                    point=point+2
                            else: 
                                    point=point+1
                        for j in range(len(DDHerlevListe)): 
                            if int(DDHerlevListe[j]) < 6: 
                                point = point-5
                            elif int(DDHerlevListe[j]) < 11: 
                                point = point-3
                            if int(DDModstanderListe[j]) < 6:
                                point = point+5
                            elif int(DDModstanderListe[j]) <11:
                                point = point +3
                    break
    return(point)

def helpHjemmebane(x:str,navn:str,nummer:int):
    pattern = "[0-9]+"
    point = 0
    HD = 0
    MD = 0
    DD = 0
    sæt = 0
    for j in range(len(x)-10):
        if x[j:j+8] == "Resultat": 
            Holdkampsresultat = (re.findall(pattern,x[j+9:j+14]))
            if int(Holdkampsresultat[0]) == 0: 
                point = point-5
            elif int(Holdkampsresultat[0]) > 6: 
                point = point+5
            else: 
                point = point+2
    for i in range(len(x)-20): 
        if x[i:i+len(navn)] == navn: 
            for k in range(45):
                if "HS" in x[i-3:i-1]: 
                    HSPoint = (re.findall(pattern,x[i:i+55+len(navn)]))
                    if len(HSPoint)%2 == 1: 
                        del HSPoint[-1]
                    if len(HSPoint) < 1: 
                        break
                    HSHerlevListe = []
                    HSModstanderListe = []
                    for r in range(len(HSPoint)):
                        if r%2 == 1 : 
                            HSModstanderListe.append(HSPoint[r])
                        else: 
                            HSHerlevListe.append(HSPoint[r])
                    
                    if int(HSHerlevListe[-1]) < 21 and int(HSModstanderListe[-1]) < 21: 
                        point=point+0
                        
                    
                    elif int(HSHerlevListe[-1]) > int(HSModstanderListe[-1]) : 
                        if len(HSHerlevListe) == 3: 
                                sæt = sæt+3
                                point=point+4 
                        else : 
                                point=point+5
                                sæt = sæt+2
                    else: 
                        if len(HSHerlevListe) == 3:
                                point=point+2
                                sæt = sæt+3
                        else: 
                                point=point+1
                                sæt = sæt+2
                    Gennemsnitpoint = sum(map(int, HSHerlevListe))
                    ModstanderGennemsnitspoint = sum(map(int, HSModstanderListe))
                    
                    for j in range(len(HSHerlevListe)): 
                        if int(HSHerlevListe[j]) < 6: 
                            point = point-5
                        elif int(HSHerlevListe[j]) < 11: 
                            point = point-3
                        if int(HSModstanderListe[j]) < 6:
                            point = point+5
                        elif int(HSModstanderListe[j]) <11:
                            point = point +3 
                    break
                elif "HD" in x[i-k-2:i-k]: 
                    if HD < 1: 
                        HD = 2
                        HDPoint = (re.findall(pattern,x[i:i+100+len(navn)]))
                        if (len(HDPoint))%2 == 1: 
                            del HDPoint[-1]
                        if len(HDPoint) < 1: 
                            break
                        HDHerlevListe = []
                        HDModstanderListe = []
                        for r in range(len(HDPoint)):
                            if r%2 == 1 : 
                                HDModstanderListe.append(HDPoint[r])
                            else: 
                                HDHerlevListe.append(HDPoint[r])
                        if int(HDHerlevListe[-1]) < 21 and int(HDModstanderListe[-1]) < 21: 
                            point=point+0
                        elif int(HDHerlevListe[-1]) > int(HDModstanderListe[-1]) : 
                            if len(HDHerlevListe) == 3: 
                                    point=point+4 
                                    sæt = sæt+3
                            else : 
                                    point=point+5
                                    sæt = sæt+2
                        else: 
                            if len(HDHerlevListe) == 3:
                                    point=point+2
                                    sæt = sæt+3
                            else: 
                                    point=point+1
                                    sæt=sæt+2
                        for j in range(len(HDHerlevListe)): 
                            if int(HDHerlevListe[j]) < 6: 
                                point = point-5
                            elif int(HDHerlevListe[j]) < 11: 
                                point = point-3
                            if int(HDModstanderListe[j]) < 6:
                                point = point+5
                            elif int(HDModstanderListe[j]) <11:
                                point = point +3 
                    break
                elif "MD" in x[i-k-2:i-k]: 
                    if MD < 1: 
                        MD = 2
                        MDPoint = (re.findall(pattern,x[i:i+75+len(navn)]))
                        if (len(MDPoint))%2 == 1: 
                            del MDPoint[-1]
                        if len(MDPoint) < 1: 
                            break
                        MDHerlevListe = []
                        MDModstanderListe = []
                        for r in range(len(MDPoint)):
                            if r%2 == 1 : 
                                MDModstanderListe.append(MDPoint[r])
                            else: 
                                MDHerlevListe.append(MDPoint[r])
                        if int(MDHerlevListe[-1]) < 21 and int(MDModstanderListe[-1]) < 21: 
                            point=point+0
                        elif int(MDHerlevListe[-1]) > int(MDModstanderListe[-1]) : 
                            if len(MDHerlevListe) == 3: 
                                    point=point+4 
                                    sæt = sæt+3
                            else : 
                                    point=point+5
                                    sæt = sæt+2
                        else: 
                            if len(MDHerlevListe) == 3:
                                    point=point+2
                                    sæt = sæt+2
                            else: 
                                    point=point+1
                                    sæt = sæt+3
                        for j in range(len(MDHerlevListe)): 
                            if int(MDHerlevListe[j]) < 6: 
                                point = point-5
                            elif int(MDHerlevListe[j]) < 11: 
                                point = point-3
                            if int(MDModstanderListe[j]) < 6:
                                point = point+5
                            elif int(MDModstanderListe[j]) <11:
                                point = point +3 
                    break
                elif "DS" in x[i-3:i-1]: 
                    DSPoint = (re.findall(pattern,x[i:i+55+len(navn)]))
                    if len(DSPoint)%2 == 1: 
                        del DSPoint[-1]
                    if len(DSPoint) < 1: 
                        break
                    DSHerlevListe = []
                    DSModstanderListe = []
                    for r in range(len(DSPoint)):
                        if r%2 == 1 : 
                            DSModstanderListe.append(DSPoint[r])
                        else: 
                            DSHerlevListe.append(DSPoint[r])
                    if int(DSHerlevListe[-1]) < 21 and int(DSModstanderListe[-1]) < 21: 
                        point=point+0
                    elif int(DSHerlevListe[-1]) > int(DSModstanderListe[-1]) : 
                        if len(DSHerlevListe) == 3: 
                                point=point+4 
                                sæt = sæt+3
                        else : 
                                point=point+5
                                sæt = sæt+2
                    else: 
                        if len(DSHerlevListe) == 3:
                                point=point+2
                                sæt = sæt+3
                        else: 
                                point=point+1
                                sæt = sæt+2
                    for j in range(len(DSHerlevListe)): 
                        if int(DSHerlevListe[j]) < 6: 
                            point = point-5
                        elif int(DSHerlevListe[j]) < 11: 
                            point = point-3
                        if int(DSModstanderListe[j]) < 6:
                            point = point+5
                        elif int(DSModstanderListe[j]) <11:
                            point = point +3
                    break
                elif "DD" in x[i-k-2:i-k]: 
                    if DD < 1: 
                        DD = 2
                        DDPoint = (re.findall(pattern,x[i:i+75+len(navn)]))
                        if len(DDPoint) < 2: 
                            break
                        if (len(DDPoint))%2 == 1: 
                            del DDPoint[-1]
                        if len(DDPoint) < 1 : 
                            break
                        DDHerlevListe = []
                        DDModstanderListe = []
                        for r in range(len(DDPoint)):
                            if r%2 == 1 : 
                                DDModstanderListe.append(DDPoint[r])
                            else: 
                                DDHerlevListe.append(DDPoint[r])
                        if int(DDHerlevListe[-1]) < 21 and int(DDModstanderListe[-1]) < 21: 
                            point=point+0
                        elif int(DDHerlevListe[-1]) > int(DDModstanderListe[-1]) : 
                            if len(DDHerlevListe) == 3: 
                                    point=point+4 
                                    sæt = sæt+3
                            else : 
                                    point=point+5
                                    sæt = sæt+2
                        else: 
                            if len(DDHerlevListe) == 3:
                                    point=point+2
                                    sæt = sæt+3
                            else: 
                                    point=point+1
                                    sæt = sæt+2
                        for j in range(len(DDHerlevListe)): 
                            if int(DDHerlevListe[j]) < 6: 
                                point = point-5
                            elif int(DDHerlevListe[j]) < 11: 
                                point = point-3
                            if int(DDModstanderListe[j]) < 6:
                                point = point+5
                            elif int(DDModstanderListe[j]) <11:
                                point = point +3
                    break
    return(point)

def fjernNavne(x): 
    for i in range(len(x)): 
        if x[i:i+8] == "Resultat": 
            return(x[i:-1])

