from __future__ import annotations

class Boolean:
    #constructor
    def __init__(self: Boolean,valeur : bool):
        #attribut d'instance 
        self.valeur = valeur
    
    def __repr__(self: Boolean) -> str:    
        return f'class Boolean: valeur : {self.valeur}'    
    
    def setBool (self : Boolean, valeur : bool):
        self.valeur = valeur
    
    def getBool (self : Boolean)->bool:
        return self.valeur
#-----------------------------------------
if __name__ == '__main__':
    moi : Boolean =Boolean(True)
    print(f'{moi}')