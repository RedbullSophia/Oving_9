# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:15:02 2021

@author: Morten
"""
#------Definerer klasse------#
class Sporsmal:
     def __init__(self, spor, svar_alt, svar):
        self.spor = spor
        self.svar = svar
        self.svar_alt = svar_alt

     def Sjekk_Svar(self, svaret):
        return self.svar == svaret  
    
     def __str__(self):
        prnt = self.spor + self.svar_alt
        return prnt

#------Spørsmål------#
spørsmål = [
        "Hvilket årstall sank ‘Titanic’?",
        "Hva er det tyske ordet for ‘motorvei’?",
        "Hva slags gjenstand var ‘Mjølner’?",
        "Under hvilken internasjonal filmfestival deles prisen ‘Gullbjørnen’ ut?",
        "Hvem var statsminister i Norge i perioden 1981 til -86?",
        "Hvem anses for å være skaperen av den digitale pengeenheten Bitcoin?",
            ]
       
svar_alt = [
    "\n 1: 1934 \n 2: 1909 \n 3: 1912",
    "\n 1: Straße \n 2: Seiteneingang \n 3: Autobahn",
    "\n 1: Siloslegge \n 2: En hammer (Tors hammer) \n 3: Kniv",
    "\n 1: Filmfestivalen i Berlin \n 2: Filmfestivalen i Paris"
    "\n 3: Filmfestivalen i Stockholm",
    "\n 1: Erna Solberg  \n 2: Kåre Willoch \n 3: Gro Harlem Brundtland",
    "\n 1: Chŭng Eogeum \n 2: Seonu Heung \n 3: Satoshi Nakamoto",
    ]

#------Svar til spørsmålet------#
spor_svar = [
        Sporsmal(spørsmål[0], svar_alt[0], "3"),
        Sporsmal(spørsmål[1], svar_alt[1], "3"),    
        Sporsmal(spørsmål[2], svar_alt[2], "2"),   
        Sporsmal(spørsmål[3], svar_alt[3], "1"),   
        Sporsmal(spørsmål[4], svar_alt[4], "2"),   
        Sporsmal(spørsmål[5], svar_alt[5], "3"),   
            ] 
        
#------Funksjon for å kjøre spill med funksjoner------#
def Run_Game(spor_svar):
    resultat = 0
    for sporsmal in spor_svar:
        print(sporsmal)
        svar_in = input("Svar: ")
        if sporsmal.Sjekk_Svar(svar_in):
            resultat +=1
    print("Gratulerer, du fikk", resultat, "av", len(spor_svar), "poeng!")

Run_Game(spor_svar)