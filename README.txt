Goddag! 
Dette er hvordan man skal tilgå min fil.
Først og fremmest er det et krav at have python3 installeret, og et program som hedder Visual Studio Code. Der ligger links til dem i bunden af filen. 
Derudover er der en masse tilføjelser til python som skal installeres. Dette gøres ved at tilgå sin kommandocentral og skrive:

pip install openpyxl
pip install csv
pip install sys
pip install selenium
pip install numpy
pip install regex

Dette kræver også at man har downloadet chrome, da det er en anelse anderledes for hver browser, og dette er kodet til chrome. 
Nu skal man finde sin chromedriver, dette kan findes ved at gå ind på chrome, derefter "hjælp" og til sidst "om google". 
Her kan det ses hvilken version af chrome man har. Dertil skal man så downloade en passende chromedriver på nettet. 
Denne fil skal ligge i en mappe ved navn "webdrivers", som skal ligge på fil placeringen "Windows-SSD". Hvis programmet har kørt fint -
i en længere periode, men der opstår problemer, så er det højst sandsynligt at man skal opdaterer sin chromedriver, da der kan være kommet en ny version. 
Man skal herefter oprette 3 txt filer. Dette gøres ved at åbne "Wordpad", og lave en fil der hedder henholdsvis: "Hjemmebane.txt", "Udebane.txt" og "BrugteLinks.txt". 
Disse 3 filer skal ligge inde i ens personlige "sti". Altså for mig skal de ligge herinde "C:\Users\Asger Nielsen". Se video hvis i tvivl. 

Herefter burde det hele virke! Det er vigtigt at det hele ligger i samme mappe, og ligger et sted der er en del af din "path", altså en del af "C:\Users\Asger Nielsen", bare med jeres eget navn. 
I det dokument som hedder uptimized, skal du opdatere din værdi PATH (linje 100 og linje 114), til den sti hvorpå din chromedriver nu ligger. 
I mit tilfælde ligger den ved "C:\webdrivers". 
Nu skal du tilføje de holdkampslinks fra badmintonplayer, som jeres klub har spillet. Hvis jeres hold har spillet hjemmebane, skal linket tilføjes på linje 15. 
Det skal indsættes inden i [] og med "" rundt om sig. Hvis du skal indsætte mere end et link, skal du have komma i mellem. Det ser cirka sådan her ud: 
["link1","link2","link3"]. Det samme gælder for udebane links i linjen nedenunder. 
Herefter skal du lave et exel dokument som hedder "kamp" (dette har jeg i hvertfald kaldt min, så medmindre du vil ændre mere vil jeg
foreslå du bruger samme navn), hvori du skriver alle navnene på spillerne i din klub. Dette er meget vigtigt at de er stavet præcis
som de er på badmintonplayer! Ellers vil koden ikke kunne genkende navnene. 
Der skal også laves en excel fil som holder styr på hver persons hold, og giver de point som man skal have. Derfor skal man oprette en excelfil som hedder:
"managerspil". Her skal man lave hold, og personernes navne (Ligesom før, de korrekt stavede navne) skal stå i kollenne A, og man skal sætte et 0 ud for dem i kollenne B.
Se de filer jeg har lagt med hvis i tvivl. 

Herefter kan du køre filen, og se at dit exelark nu er blevet opdateret med de nye værdier. Note, dit exelark må ikke være åbent 
mens koden kører, ellers får du en fejlkode. 
Hvis man har brug for at slette alle sine værdier i exelarket, så kør filen WipeExcel, den stiller alle værdier i anden celle til 0. 
Dette gøres ved at fjerne # på linje 31, og køre den. 
Hvis du er kommet til at indsætte et hjemmebaneholdkamp link til udebane ved en fejl, skal du gå ind og slette det link i din txt fil "Udebane", køre filen 
WipeExcel, og derefter køre filen "uptimized" igen. 

Ideen med hele dette managerspil er at dem der deltager vælger fx 6 spillere i klubben som de tror kommer til at klare sig godt i løbet 
af årets holdkampe, og sætter dem på sit hold. 
Jeg vedlægger et excelark af Herlevs samlede holdstilling(ManagerGame), hvor i kan se hvordan jeg har sat det op. 
Hvis du synes det ser fint ud, kan du kopiere måden jeg har sat det op på. Hvis dette er tilfældet kan du selv lave et excel ark stillet op
på samme måde som jeg gjorde, med de forskellige deltageres hold. Herefter kør filen ExcelFormator, og så vil den opdatere dette excelark med
de værdier som der nu står kamp-filen. 

Dette burde kunne spare meget tid i længden! 

Jeg vil meget meget gerne svare på spørgsmål hvis man har svært ved at få det hele til at køre, da det selvfølgelig kan være man ikke selv koder. 
Jeg er også åbent for at lave ændringer hvis du har noget som skal tilføjes, eller noget du vil have fjernet. 
mail: asger.feldbaek@gmail.com
tlf: 51202519 



links: 
https://www.python.org/downloads/
https://code.visualstudio.com/download
https://chromedriver.chromium.org/downloads
