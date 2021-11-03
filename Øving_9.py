# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:19:14 2021

@author: Morten
"""
#----- Importerer Øving 8 med klasse -----#
import Øving8_b as Ov8

#----- Lager funksjon åpne/les fil -----#
def Les_Fil():
    
    #----- Åpner fil med kallenavn Spm -----#
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as Spm:
        sporsmal = []
        
    #----- Lager en liste med spørmsmål, svar, og svar_alt -----#    
        for Line in Spm:
            liste = Line.split(":")
            liste[1] = int(liste[1])
            liste[2] = liste[2][liste[2].find("[")+1:liste[2].find("]")].split(", ")
                            
            sporsmal.append(Ov8.Sporsmal(f"{liste[0]} \n", liste[2], liste[1]))

    return sporsmal


if __name__ == "__main__":
    
#----- Leser inn spørsmål -----#    
    sporsmaal_objekter = Les_Fil()
    
#----- Lager variabler med poeng til spillere -----#
    poeng_pl1 = 0
    poeng_pl2 = 0
      
#----- For-loop printer alle spørsmål i listen for tur -----#
    for line in sporsmaal_objekter:
        print(line)
        
#----- Spør brukere om  -----#
        svar_pl1 = int(input("Spiller 1 svar: "))
        svar_pl2 = int(input("Spiller 2 svar: "))
        
  #----- Printer korrekt svar med Sjekk_Svar -----#      
        print("\n--- Korrekt svar er: ", line.Sjekk_Svar(),"--- \n")
  
#----- Sjekker om spiller 1 har rett svar eller ikke, legger til poeng -----#  
        if line.svar == svar_pl1:
            print("Spiller 1: Korrekt!")
            poeng_pl1 += 1
        else:
            print("Spiller 1: Feil")
           
#----- Sjekker om spiller 2 har rett svar eller ikke, legger til poeng -----#              
        if line.svar == svar_pl2:
            print("Spiller 2: Korrekt! \n")
            poeng_pl2 += 1
        else:
            print("Spiller 2: Feil \n")
 
#----- Skriver ut poengsum til spillerene -----# 
    print("Resultat: \nSpiller 1 fikk:", poeng_pl1, "poeng \n"
          "Spiller 2 fikk:", poeng_pl2, "poeng")
