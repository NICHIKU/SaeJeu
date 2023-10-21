from __future__ import annotations
import pygame as pg

class Texte:
    #constructor
    def __init__(self: Texte,texte : str,font : str, taille : int, couleur : tuple,center : bool,First : bool,y_rect : float = 0.5,x : int = None,y : int = None, screen_width : int = 800, screen_height : int = 600, screen: pg.display = pg.display.set_mode((800,600))):
        #attribut d'instance 
        self.couleur : tuple = couleur
        self.taille : int = taille
        self.valeur : str = texte
        self.font = pg.font.Font(font, self.taille)
        self.texte = self.font.render(self.valeur, True, self.couleur)
        self.center : bool = center
        self.First : bool = First
        self.y_rect : float = y_rect
        self.x : int = x
        self.y : int = y
        self.screen_width : int = screen_width
        self.screen_height : int = screen_height
        self.screen : pg.display.set_mode = screen
        self.rect: pg.Rect = pg.Rect((screen_width - taille) // 2.1, (screen_height-taille)//2.5, taille, taille)
        if self.center == True:
            texteRect = self.texte.get_rect()
            if self.First == True:
                texteRect.center = self.rect.center
            else : 
                self.rect= pg.Rect((screen_width - taille) // 2.1, (screen_height-taille)//y_rect, taille, taille)
                texteRect.center = self.rect.center
            self.screen.blit(self.texte, texteRect)
        else:

            if self.x>self.screen_width or self.x<0 or self.y<0 or self.y>self.screen_height:
                while x>screen_width or x<0 or y<0 or y>screen_height:
                    print("erreur, veuillez réessayer")
                    self.x = int(input("x : "))
                    self.y = int(input("y : "))
                    self.screen.blit(self.texte, (self.x,self.y))
            else:
                self.screen.blit(self.texte, (self.x,self.y))
        
    
    def __repr__(self: Texte) -> str:    
        return f'class Texte: valeur : {self.texte}'    
    
    def setTexte (self : Texte, valeur : str):
        self.texte = self.font.render(valeur, True, self.couleur)
        if self.center == True:
            texteRect = self.texte.get_rect()
            if self.First == True:
                texteRect.center = self.rect.center
            else : 
                self.rect= pg.Rect((self.screen_width - self.taille) // 2.1, (self.screen_height-self.taille)//self.y_rect, self.taille, self.taille)
                texteRect.center = self.rect.center
                self.screen.blit(self.texte, texteRect)    
        else:
            self.screen.blit(self.texte, (self.x,self.y))
        
    def setFont (self : Texte, font : str):
        self.font = pg.font.Font(font, self.taille)
        self.texte = self.font.render(self.valeur, True, self.couleur)
        if self.center == True:
            texteRect = self.texte.get_rect()
            if self.First == True:
                texteRect.center = self.rect.center
            else : 
                self.rect= pg.Rect((self.screen_width - self.taille) // 2.1, (self.screen_height-self.taille)//self.y_rect, self.taille, self.taille)
                texteRect.center = self.rect.center
                self.screen.blit(self.texte, texteRect)    
        else:
            self.screen.blit(self.texte, (self.x,self.y))
            
            
    def setColor (self : Texte, couleur : tuple, screen : pg.display = pg.display.set_mode((800,600))):
        self.texte = self.font.render(self.valeur, True, couleur)
        if self.center == True:
            texteRect = self.texte.get_rect()
            if self.First == True:
                texteRect.center = self.rect.center
                self.screen.blit(self.texte, texteRect)
            else : 
                self.rect= pg.Rect((self.screen_width - self.taille) // 2.1, (self.screen_height-self.taille)//self.y_rect, self.taille, self.taille)
                texteRect.center = self.rect.center
                self.screen.blit(self.texte, texteRect)    
        else:
            self.screen.blit(self.texte, (self.x,self.y))
    
        
    def setX (self : Texte, x : int):
        self.x = x
        self.screen.blit(self.texte, (self.x,self.y))
        
    def setY (self : Texte, y : int):
        self.y = y
        self.screen.blit(self.texte, (self.x,self.y))
        
    def getTexte (self : Texte)->str:
        return self.texte
    
    def getFont (self : Texte)->str:
        return self.font
    
    def getColor (self : Texte)->tuple:
        return self.couleur
    
    def getTaille (self : Texte)->int:
        return self.taille
    
    def getCenter (self : Texte)->bool:
        return self.center
    
    def getFirst (self : Texte)->bool:
        return self.First
    
    def getY_rect (self : Texte)->float:
        return self.y_rect
    
    def getX (self : Texte)->int:
        return self.x   

    
    def getText (self : Texte)->str:
        return self.valeur
    
    def getRect(self : Texte)->pg.Rect:
        return self.rect
#-----------------------------------------
if __name__ == '__main__':
    moi : Texte =Texte(True)
    print(f'{moi}')