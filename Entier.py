from __future__ import annotations

class Entier:
    #constructor
    def __init__(self: Entier,valeur : int):
        #attribut d'instance 
        self.valeur = valeur
    
    def __repr__(self: Entier) -> str:    
        return f'class Entier: valeur : {self.valeur}'    
    
    def setInt (self : Entier, valeur : int):
        self.valeur = valeur
    
    def getInt (self : Entier)->int:
        return self.valeur
#-----------------------------------------
if __name__ == '__main__':
    moi : Entier =Entier(True)
    print(f'{moi}')