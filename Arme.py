from __future__ import annotations
class Arme:
    #attribut statique
    allArmes : list [Arme] = []
    
    # methode statique
    @staticmethod
    def getInfo()->list[Arme]:
        return Arme.allArmes
    
    #constructor
    def __init__(self: Arme,DPS : int,nom : str):
        #attribut d'instance
        self.DPS : int  = DPS    
        self.nom : str = nom
        Arme.allArmes.append(self)
    
    def __repr__(self: Arme) -> str:    
        return f'Arme: "{self.nom}" et fait "{self.DPS}" de dégats >'
    

    def setNom(self : Arme , nom: str):
        self.nom = nom

    def setDPS(self : Arme, DPS : int):
        self.DPS = DPS
    
    
    def getNom(self:Arme)->str:
        return self.nom
    
    def getDPS(self : Arme)->int:
        return self.DPS
        
#-----------------------------------------
if __name__ == '__main__':
    moi : Arme =Arme(10,'Epee')
    print(f' Cette arme est : {moi}')