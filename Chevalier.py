from __future__ import annotations
from Arme import Arme
import pygame as pg


class Chevalier:
    #attribut statique
    allChevaliers : list [Chevalier] = []
    
    # methode statique
    @staticmethod
    def getInfo()->list[Chevalier]:
        return Chevalier.allChevaliers
    
    #constructor
    def __init__(self: Chevalier, type : str,ar : Arme):
        #attribut d'instance 
        self.type : str = type
        self.arme : Arme = ar
        self.vitalité : int = 14
        self.endurance : int = 10
        self.dextérité : int = 11
        self.intelligence : int = 9
        self.force : int = 11
        self.resistance : int = 10
        self.image = "Images/Knight.png"
        Chevalier.allChevaliers.append(self)
    
    def __repr__(self: Chevalier) -> str:    
        return f'class Chevalier: nom : "{self.type}" et a comme {self.arme}'
    
    
    def setType(self : Chevalier , type: str):
        self.type = type

    def setArme(self : Chevalier, arme : str):
        self.arme = arme
    
    def setImage(self : Chevalier, img:str):
        self.image = img
    
    def getType(self:Chevalier)->str:
        return self.type
        
    def getArme(self : Chevalier)->Arme:
        return self.arme
    
    def getImage(self : Chevalier)->str:
        return self.image
    
    def getVitalité(self : Chevalier)->int:
        return self.vitalité
    
    def getEndurance(self : Chevalier)->int:
        return self.endurance
    
    def getDextérité(self : Chevalier)->int:
        return self.dextérité
    
    def getIntelligence(self : Chevalier)->int:
        return self.intelligence
    
    def getForce(self : Chevalier)->int:
        return self.force
    
    def getResistance(self : Chevalier)->int:
        return self.resistance
    
    def setVitalité(self : Chevalier, vitalité : int):
        self.vitalité = vitalité

    def setEndurance(self : Chevalier, endurance : int):
        self.endurance = endurance
        
    def setDextérité(self : Chevalier, dextérité : int):
        self.dextérité = dextérité
        
    def setIntelligence(self : Chevalier, intelligence : int):
        self.intelligence = intelligence
        
    def setForce(self : Chevalier, force : int):
        self.force = force
        
    def setResistance(self : Chevalier, resistance : int):
        self.resistance = resistance
        
    def attaquer(self : Chevalier, cible : Chevalier):
        cible.setVitalité(cible.getVitalité()-self.arme.getDPS())
        
    
        
#-----------------------------------------
if __name__ == '__main__':
    Epee : Arme = Arme(30,"Epée")
    moi : Chevalier =Chevalier('Chevalier renforcée',Epee)
    print(f'{moi}')