from __future__ import annotations
from Arme import Arme
from Ennemie import Ennemie


class Joueur:
    #attribut statique
    allJoueurs : list [Joueur] = []
    
    # methode statique
    @staticmethod
    def getInfo()->list[Joueur]:
        return Joueur.allJoueurs
    
    #constructor
    def __init__(self: Joueur, type : str,ar : Arme, x : int, y : int):
        #attribut d'instance 
        self.type : str = type
        self.arme : Arme = ar
        self.x : int = x
        self.y : int = y
        self.mouvement : bool = False
        self.vitalité : int = 14
        self.endurance : int = 10
        self.dextérité : int = 11
        self.intelligence : int = 9
        self.force : int = 11
        self.resistance : int = 10
        self.image = "Images/Knight.png"
        Joueur.allJoueurs.append(self)
    
    def __repr__(self: Joueur) -> str:    
        return f'class Joueur: type : "{self.type}" et a comme {self.arme}'
    
    
    def settype(self : Joueur , type: str):
        self.type = type

    def setArme(self : Joueur, arme : str):
        self.arme = arme
    
    def setImage(self : Joueur, img:str):
        self.image = img
    
    def gettype(self:Joueur)->str:
        return self.type
        
    def getArme(self : Joueur)->Arme:
        return self.arme
    
    def getX(self : Joueur)->int:
        return self.x
    
    def getY(self : Joueur)->int:
        return self.y
    
    def getMouvement(self : Joueur)->bool:
        return self.mouvement
    
    def getImage(self : Joueur)->str:
        return self.image
    
    def getVitalité(self : Joueur)->int:
        return self.vitalité
    
    def getEndurance(self : Joueur)->int:
        return self.endurance
    
    def getDextérité(self : Joueur)->int:
        return self.dextérité
    
    def getIntelligence(self : Joueur)->int:
        return self.intelligence
    
    def getForce(self : Joueur)->int:
        return self.force
    
    def getResistance(self : Joueur)->int:
        return self.resistance
    
    def setX(self : Joueur, x : int):
        self.x = x
        
    def setY(self : Joueur, y : int):
        self.y = y
        
    def setMouvement(self : Joueur, mouvement : bool):
        self.mouvement = mouvement
    
    def setVitalité(self : Joueur, vitalité : int):
        self.vitalité = vitalité

    def setEndurance(self : Joueur, endurance : int):
        self.endurance = endurance
        
    def setDextérité(self : Joueur, dextérité : int):
        self.dextérité = dextérité
        
    def setIntelligence(self : Joueur, intelligence : int):
        self.intelligence = intelligence
        
    def setForce(self : Joueur, force : int):
        self.force = force
        
    def setResistance(self : Joueur, resistance : int):
        self.resistance = resistance
        
    def attaquer(self : Joueur, cible : Ennemie):
        cible.setVitalité(cible.getVitalité()-self.arme.getDPS())
        
    
        
#-----------------------------------------
if __name__ == '__main__':
    Epee : Arme = Arme(30,"Epée")
    moi : Joueur =Joueur('Joueur renforcée',Epee)
    print(f'{moi}')