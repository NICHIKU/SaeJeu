from __future__ import annotations
import pygame as pg 
import sys
from Joueur import Joueur
from Arme import Arme 
from Boolean import Boolean
from Entier import Entier
from Texte import Texte

def clic_Joueur(ListeJoueur : list[Joueur],x:int,y:int):
        print("clic sur le joueur")
        verif = getJoueur(x,y)
        selection_en_cours.setBool(True)
        for i in range(len(ListeJoueur)):
            if verif.gettype() == ListeJoueur[i].gettype():
                print(ListeJoueur[i].getMouvement())
                if tour.getInt()%2 == 0 or verif.getMouvement() == True:
                    print("mauvais tour")
                    selection_en_cours.setBool(False)
                    clic_actif.setBool(False)
           
def deplacement_possible(x,y,indice_ligne,indice_colonne,plateau) -> bool:
    result = False
    
    if isinstance(plateau[indice_ligne][indice_colonne],Joueur) == False :
        print("pas de joueur")
        if (indice_ligne<x+3 and indice_ligne>x-3) and (indice_colonne<y+3 and indice_colonne>y-3):
            print("Déplacement possible")
            result= True
    else:
        print("Déplacement impossible")
        result = False
    
    print("resultat : ",result)
    return result
    


def deplacement(ListeJoueur : list[Joueur],x:int,y:int,verif:Joueur):
        print("Joueur récupéré")
        déplace = getJoueur(verif.getX(), verif.getY())
        plateau[déplace.getX()][déplace.getY()] = None
        for i in range(len(ListeJoueur)):
            if déplace.gettype() == ListeJoueur[i].gettype():
                ListeJoueur[i].setX(x)
                ListeJoueur[i].setY(y)
                ListeJoueur[i].setMouvement(True)
        plateau[x][y] = déplace
        nbdéplacement = 0
        #trouver comment ajuster le nb de joueurs à modifier en fonction du typebre de Joueur sur le plateau
        for i in range(len(ListeJoueur)):
            if ListeJoueur[i].getMouvement() == True:
                nbdéplacement +=1
        
        if nbdéplacement == (len(ListeJoueur)+1):
            for i in range (len(ListeJoueur)):
                ListeJoueur[i].setMouvement(False)
            tour.setInt(tour.getInt()+1)

def getObjet(x,y):
    if plateau[x][y] == None:
        return None
    else:
        return plateau[x][y]

def verif_Joueur(x,y) -> bool:
    if isinstance(plateau[x][y],Joueur):
        return True
    else:
        return False

def getJoueur(x,y)-> Joueur:
    return plateau[x][y]

def creaJoueur(type : str,arme : Arme ,x: int,y : int):
        type = input("type du joueur : ")
        arme = input("Arme du joueur : ")
        x = int(input("x : "))
        y = int(input("y : "))
        ListeJoueur.append(Joueur(type,arme,x,y))

def creaTexte(texte : str,font : str, taille : int, couleur : tuple,center : bool,First : bool,y_rect : float = 2,x : int = None,y : int = None):
    font = pg.font.Font(font, taille)
    texte = font.render(texte, True, couleur)
    if center == True:
        texteRect = texte.get_rect()
        if First == True:
            texteRect.center = (screen_width // 2, screen_height // 2)
        else : 
            texteRect.center = (screen_width // 2, screen_height // y_rect)
        screen.blit(texte, texteRect)
    else:

        if x>screen_width or x<0 or y<0 or y>screen_height:
            while x>screen_width or x<0 or y<0 or y>screen_height:
                print("erreur, veuillez réessayer")
                x = int(input("x : "))
                y = int(input("y : "))
                screen.blit(texte, (x,y))
        else:
            screen.blit(texte, (x,y))


    
if __name__ == "__main__":
    pg.init()
    # Création de la fenêtre
    nb_lig = 8
    nb_col = 12
    Taille_case = 64
    couleur_gril=(133,192,0)
    
    decalj2_g = 8
    decalj2_h = 10

   

    screen_color = (100,100,100)
    screen_width = nb_col*Taille_case
    screen_height = nb_lig*Taille_case

    Epee : Arme = Arme(30,"Epée")
    j1 : Joueur =Joueur('j1',Epee,1,2)
    j2 : Joueur =Joueur("j2",Epee,2,2)
    j2.setImage("Images/Solaire.png")
    
    ListeJoueur : list[Joueur] = []
    ListeJoueur.append(j1)
    ListeJoueur.append(j2)
    
    plateau = [[None] * nb_col for _ in range(nb_lig)]    
    plateau[j1.getX()][j1.getY()] = j1
    plateau[j2.getX()][j2.getY()] = j2

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Dark info")

    clic_actif:Boolean = Boolean(False) 
    selection_en_cours : Boolean = Boolean(False)
    tour:Entier = Entier(1)
    menu : Boolean = Boolean(True)
    jeu : Boolean = Boolean(False)
    param : Boolean = Boolean(False)
    param_actif : Boolean = Boolean(False)
    while True:
        while menu.getBool()==True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
                screen.fill(screen_color)
                #affichage du texte jouer en majuscule en noir et en font 50 sur le centre haut de la fenêtre
                Jouer : Texte = Texte("Jouer",None,50,(0,0,0),True,True,screen_width,screen_height,screen) 
                #affichage du texte quitter en majuscule en noir et en font 50 sur le centre bas de la fenêtre
                Param : Texte = Texte("Parametres",None,50,(0,0,0),True,None,screen_width,screen_height,screen) 
                
                x, y = pg.mouse.get_pos()
                
                if Jouer.getRect().collidepoint(x,y) == True:
                            #le texte jouer devient rouge
                            Jouer.setColor((255,0,0),screen)
                if Param.getRect().collidepoint(x,y) == True:
                            #le texte quitter devient rouge
                            Param.setColor((255,0,0),screen)
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pg.mouse.get_pos()
                        if x > 200 and x < 400 and y > 200 and y < 250:
                            menu.setBool(False)
                            jeu.setBool(True)
                        elif x > 200 and x < 400 and y > 300 and y < 350:
                            menu.setBool(False)
                            param.setBool(True)
            
            
            pg.display.update()


        while param.getBool()==True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
                screen.fill(screen_color)
                #affichage du texte jouer en majuscule en noir et en font 50 sur le centre haut de la fenêtre
                creaTexte("nbJoueur",None,50,(0,0,0),True,True)
                #affichage du texte quitter en majuscule en noir et en font 50 sur le centre bas de la fenêtre
                creaTexte("Retour",None,50,(0,0,0),True,False,1.5)
                
                x, y = pg.mouse.get_pos()
                if x > 200 and x < 400 and y > 300 and y < 350:
                            creaTexte("Retour",None,50,(255,0,0),True,False,1.5)
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pg.mouse.get_pos()
                        if x > 200 and x < 400 and y > 300 and y < 350:
                            param.setBool(False)
                            menu.setBool(True)
            
            
            pg.display.update()
        

        while jeu.getBool()==True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            screen.fill(screen_color)
            
            for ligne in range(nb_lig):
                for colonne in range(nb_col):
                
                    pg.draw.rect(screen, couleur_gril, (colonne * Taille_case, ligne * Taille_case, Taille_case, Taille_case), 1)
                    for i in range(len(ListeJoueur)):
                        if plateau[ligne][colonne] == ListeJoueur[i]:
                            screen.blit(pg.image.load(ListeJoueur[i].getImage()), (colonne * Taille_case-decalj2_g, ligne * Taille_case-decalj2_h ))
                
            
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if clic_actif.getBool() == False:    
                        x, y = pg.mouse.get_pos()
                        indice_colonne = x // Taille_case
                        indice_ligne = y // Taille_case

                        if selection_en_cours.getBool() == False:
                            
                            if verif_Joueur(indice_ligne, indice_colonne):
                                verif = getJoueur(indice_ligne, indice_colonne)
                                selection_en_cours.setBool(True)
                                clic_Joueur(ListeJoueur,indice_ligne,indice_colonne)
                            clic_actif.setBool(True)
                                                                
                        else:
                            print ("selection en cours")
                            if deplacement_possible(verif.getX(), verif.getY(), indice_ligne, indice_colonne, plateau) == True:
                                print("rangé")
                                deplacement(ListeJoueur,indice_ligne,indice_colonne,verif)
                            print("deplacement effectué")
                            selection_en_cours.setBool(False)
                            clic_actif.setBool(True)   
        
                            
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    clic_actif.setBool(False)

            pg.display.update()
