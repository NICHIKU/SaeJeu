from __future__ import annotations
from Arme import Arme


class Ennemie:
    #attribut statique
    allEnnemies : list [Ennemie] = []
    
    # methode statique
    @staticmethod
    def getInfo()->list[Ennemie]:
        return Ennemie.allEnnemies
    
    #constructor
    def __init__(self: Ennemie, type : str,ar : Arme, x : int, y : int):
        #attribut d'instance 
        self.type : str = type
        self.arme : Arme = ar
        self.x : int = x
        self.y : int = y
        self.mouvement : bool = False
        self.vitalité : int = 100
        self.endurance : int = 10
        self.image = "Images/hollow_sword.png"
        Ennemie.allEnnemies.append(self)
    
    def __repr__(self: Ennemie) -> str:    
        return f'class Ennemie: type : "{self.type}" et a comme {self.arme}'
    
    
    def settype(self : Ennemie , type: str):
        self.type = type

    def setArme(self : Ennemie, arme : str):
        self.arme = arme
    
    def setImage(self : Ennemie, img:str):
        self.image = img
    
    def gettype(self:Ennemie)->str:
        return self.type
        
    def getArme(self : Ennemie)->Arme:
        return self.arme
    
    def getX(self : Ennemie)->int:
        return self.x
    
    def getY(self : Ennemie)->int:
        return self.y
    
    def getMouvement(self : Ennemie)->bool:
        return self.mouvement
    
    def getImage(self : Ennemie)->str:
        return self.image
    
    def getVitalité(self : Ennemie)->int:
        return self.vitalité
    
    def getEndurance(self : Ennemie)->int:
        return self.endurance
    
    
    def setX(self : Ennemie, x : int):
        self.x = x
        
    def setY(self : Ennemie, y : int):
        self.y = y
        
    def setMouvement(self : Ennemie, mouvement : bool):
        self.mouvement = mouvement
    
    def setVitalité(self : Ennemie, vitalité : int):
        self.vitalité = vitalité

    def setEndurance(self : Ennemie, endurance : int):
        self.endurance = endurance
        
   
        
        
    
        
#-----------------------------------------
if __name__ == '__main__':
    Epee : Arme = Arme(30,"Epée")
    moi : Ennemie =Ennemie('Ennemie renforcée',Epee)
    print(f'{moi}')