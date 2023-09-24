from __future__ import annotations
from Arme import Arme

class Carcasse:
    #attribut statique
    allCarcasses : list [Carcasse] = []
    
    # methode statique
    @staticmethod
    def getInfo()->list[Carcasse]:
        return Carcasse.allCarcasses
    
    #constructor
    def __init__(self: Carcasse, type : str,ar : Arme):
        #attribut d'instance 
        self.type : str = type
        self.arme : Arme = ar
        Carcasse.allCarcasses.append(self)
    
    def __repr__(self: Carcasse) -> str:    
        return f'class Carcasse: nom : "{self.type}" et a comme {self.arme}'
    
    
    def setType(self : Carcasse , type: str):
        self.type = type

    def setArme(self : Carcasse, arme : str):
        self.arme = arme
    
    def getType(self:Carcasse)->str:
        return self.type
        
    def getArme(self : Carcasse)->Arme:
        return self.arme
        
#-----------------------------------------
if __name__ == '__main__':
    Epee : Arme = Arme(40,"Moonlight Great Sword")
    moi : Carcasse =Carcasse('Carcasse renforcée',Epee)
    print(f'{moi}')