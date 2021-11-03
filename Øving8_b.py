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

     def Sjekk_Svar(self):
        return self.svar_alt[self.svar] 
    
     def __str__(self):
        prnt = self.spor
        for i, alt in enumerate(self.svar_alt):
                prnt += f"{i}. {alt} \n"
        return prnt
