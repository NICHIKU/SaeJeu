from __future__ import annotations
import pygame as pg 
import sys
from Joueur import Joueur
from Ennemie import Ennemie
from Arme import Arme 
from Boolean import Boolean
from Entier import Entier
from Texte import Texte
import random as rd


def clic_Joueur(ListeJoueur : list[Joueur],x:int,y:int):
        print("clic sur le joueur")
        verif = getJoueur(x,y)
        selection_en_cours.setBool(True)
        for i in range(len(ListeJoueur)):
            if verif.gettype() == ListeJoueur[i].gettype():
                print(ListeJoueur[i].getMouvement())
                if tour.getInt()%2 == 1 or verif.getMouvement() == True:
                    print("mauvais tour")
                    selection_en_cours.setBool(False)
                    clic_actif.setBool(False)
              
                           
                            
                            
def deplacement_possible(x,y,indice_ligne,indice_colonne,plateau) -> bool:
    result = False
    
    if isinstance(plateau[indice_ligne][indice_colonne],Joueur) == False :
        if (indice_ligne<x+3 and indice_ligne>x-3) and (indice_colonne<y+3 and indice_colonne>y-3):
            result= True
    elif isinstance(plateau[indice_ligne][indice_colonne],Ennemie) == True:
        if (indice_ligne<x+3 and indice_ligne>x-3) and (indice_colonne<y+3 and indice_colonne>y-3):
            attaquerEnnemi(ListeJoueur,ListeEnnemi,indice_ligne,indice_colonne)
            result= True
    else:
        print("Déplacement impossible")
        result = False
    
    print("resultat : ",result)
    return result


def attaquerJoueur(ListeJoueur : list[Joueur],x : int,y : int,e1 : Ennemie):
            for j in range(len(ListeJoueur)):
                if plateau[x][y] == ListeJoueur[j]:
                    ListeJoueur[j].setVitalité(ListeJoueur[j].getVitalité()-e1.getArme().getDPS())
                    attack_zombie_sound.play(-1)
                    print("vie du joueur : ",ListeJoueur[j].getVitalité())
                    if ListeJoueur[j].getVitalité() <= 0:
                        plateau[x][y] = None
                        ListeJoueur.pop(j)
                        plateau[x][y] = None
                 
                        death_sound.play(-1)
                        if len(ListeJoueur) == 0:
                            lose_sound.play(-1)
                            print("fin de partie")
                            jeu.setBool(False)
                            Lose.setBool(True)
                    else:
                        print("joueur touché")
                    break

def deplacementEnnemi(ListeEnnemi : list[Ennemie]):
    for i in range(len(ListeEnnemi)):
        x_Temp = ListeEnnemi[i].getX()-rd.randint(1,2)
        y_Temp = ListeEnnemi[i].getY()-rd.randint(1,2)
        while x_Temp >7 or x_Temp <0 or y_Temp >11 or y_Temp <0:
            x_Temp = ListeEnnemi[i].getX()+rd.randint(1,2)
            y_Temp = ListeEnnemi[i].getY()+rd.randint(1,2)
        if isinstance(plateau[x_Temp][y_Temp],Joueur) == False and isinstance(plateau[x_Temp][y_Temp],Ennemie) == False:
            plateau[ListeEnnemi[i].getX()][ListeEnnemi[i].getY()] = None
            plateau[x_Temp][y_Temp] = ListeEnnemi[i]
            ListeEnnemi[i].setX(x_Temp)
            ListeEnnemi[i].setY(y_Temp)
        elif isinstance(plateau[x_Temp][y_Temp],Joueur) == True:
            ennemie_temp = getEnnemi(ListeEnnemi[i].getX(),ListeEnnemi[i].getY())
            attaquerJoueur(ListeJoueur,x_Temp,y_Temp,ennemie_temp)
            print("joueur touché")
        else:
            print("Ennemi bloqué")
    print("Ennemi déplacé")

        


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
        
        if nbdéplacement == (len(ListeJoueur)):
            for i in range (len(ListeJoueur)):
                ListeJoueur[i].setMouvement(False)
            tour.setInt(tour.getInt()+1)
            print("tour : ",tour.getInt())


def verif_Joueur(x,y) -> bool:
    if isinstance(plateau[x][y],Joueur):
        return True
    else:
        return False

def getJoueur(x,y)-> Joueur:
    return plateau[x][y]

def getEnnemi(x,y)-> Ennemie:
    return plateau[x][y]

            
def attaquerEnnemi(ListeEnnemi : list[Ennemie],x : int,y : int,j_temp : Joueur):
    #Récupère la liste des ennemis présents sur le plateau
    num_ennemi = len(ListeEnnemi)
    for j in range(num_ennemi):
        if plateau[x][y] == ListeEnnemi[j]:
            #Récupère l'ennemi touché et lui retire des points de vie en fonction des dégats de l'arme du joueur
            ListeEnnemi[j].setVitalité(ListeEnnemi[j].getVitalité()-j_temp.getArme().getDPS())
            attack_sound.play(-1)
            print("vie de l'ennemi : ",ListeEnnemi[j].getVitalité())
            if ListeEnnemi[j].getVitalité() <= 0:
                #Si l'ennemi n'a plus de vie, il est retiré de la liste et du plateau
                plateau[x][y] = None
                ListeEnnemi.pop(j)
                print("ennemi mort")
                if len(ListeEnnemi) == 0:
                    if cpt_ennemi.getInt() == 0:
                        #Si il n'y a plus d'ennemi, on passe au niveau suivant
                        round_sound.play(-1)
                        cpt_ennemi.setInt(cpt_ennemi.getInt()+1)
                        e4 : Ennemie = Ennemie("e4",Epee_Enemmie,2,6)
                        e5 : Ennemie = Ennemie("e5",Epee_Enemmie,3,6)
                        e6 : Ennemie = Ennemie("e6",Epee_Enemmie,4,6)
                        e7 : Ennemie = Ennemie("e7",Epee_Enemmie,5,6)
                        e4.setImage("Images/hollow_soldier.png")
                        e5.setImage("Images/hollow_soldier.png")
                        e6.setImage("Images/hollow_soldier.png")
                        e7.setImage("Images/hollow_soldier.png")
                        b : Ennemie = Ennemie("boss",Massue,3,7)
                        b.setImage("Images/boss.png")
                        b.setVitalité(200)
                        ListeEnnemi.append(b)
                        ListeEnnemi.append(e4)
                        ListeEnnemi.append(e5)
                        ListeEnnemi.append(e6)
                        ListeEnnemi.append(e7)
                        pg.display.update()
                    else:
                        print("fin de partie")
                        jeu.setBool(False)
                        Win.setBool(True)
                break
                
            else:
                print("ennemi touché")
            tour.setInt(tour.getInt()+1)
                       


    
if __name__ == "__main__":
    pg.init()
    # Nb de fois où tout les ennemis sont morts
    cpt_ennemi : Entier = Entier(0)
    
    # Paramètres du jeu
    nb_lig = 8
    nb_col = 12
    Taille_case = 64
    couleur_gril=(133,192,0)
    
    #variables pour le décalage des images
    decalj2_g = 8
    decalj2_h = 10

    #taill et couleur de la fenêtre
    screen_color = (100,100,100)
    screen_width = nb_col*Taille_case
    screen_height = nb_lig*Taille_case

    #Création des armes
    Epee : Arme = Arme(30,"Epée")
    Epee_Enemmie : Arme = Arme(10,"Epée Enemmie")
    Massue : Arme = Arme(50,"Massue")
    
    #Création des joueurs
    j1 : Joueur =Joueur('j1',Epee,1,2)
    j2 : Joueur =Joueur("j2",Epee,2,2)
    j2.setImage("Images/Solaire.png")
    
    #instanciation de la liste et ajout des joueurs
    ListeJoueur : list[Joueur] = []
    ListeJoueur.append(j1)
    ListeJoueur.append(j2)
    
    #Création des ennemis
    e0 : Ennemie = Ennemie("e0",Epee_Enemmie,4,5)
    e1 : Ennemie = Ennemie("e1",Epee_Enemmie,5,5)
    e2 : Ennemie = Ennemie("e2",Epee_Enemmie,6,5)
    e3 : Ennemie = Ennemie("e3",Epee_Enemmie,7,5)
    
    #instanciation de la liste et ajout des ennemis
    ListeEnnemi : list[Ennemie] = []
    
    ListeEnnemi.append(e0)
    ListeEnnemi.append(e1)
    ListeEnnemi.append(e2)
    ListeEnnemi.append(e3)
    
    
    #Instanciation des effets sonores
    attack_sound = pg.mixer.Sound("Sons/joueur_attack.wav")
    attack_zombie_sound = pg.mixer.Sound("Sons/ennemie_attack.wav")
    zombie_sound = pg.mixer.Sound("Sons/zombie_death.wav")
    round_sound = pg.mixer.Sound("Sons/round2.wav")
    death_sound = pg.mixer.Sound("Sons/player_death.wav")
    lose_sound = pg.mixer.Sound("Sons/player_lose.wav")

    
    #Création du plateau et ajout des joueurs et ennemis automatiquement en fonction de leurs coordonnées
    plateau = [[None] * nb_col for _ in range(nb_lig)]    
    for i in range(len(ListeJoueur)):
        plateau[ListeJoueur[i].getX()][ListeJoueur[i].getY()] = ListeJoueur[i]
    for i in range(len(ListeEnnemi)):
        plateau[ListeEnnemi[i].getX()][ListeEnnemi[i].getY()] = ListeEnnemi[i]    

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Dark info")

    #variables pour les clics
    clic_actif:Boolean = Boolean(False) 
    selection_en_cours : Boolean = Boolean(False)
    
    #variable pour le tour (voir Entier.py)
    tour:Entier = Entier(2)

    #variables pour les menus (voir Boolean.py)
    menu : Boolean = Boolean(True)
    jeu : Boolean = Boolean(False)
    Win : Boolean = Boolean(False)
    Lose : Boolean = Boolean(False)

    #Boucle principale
    while True:
        
        #Création des menus et du son
        if menu.getBool() == True:
            menu_sound = pg.mixer.Sound("Sons/Menu.wav")
            menu_sound.play(-1)
        while menu.getBool()==True:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                #affichage du menu en fond
                screen.blit(pg.image.load("Images/Menu.png"), (0,0))
                
                #Création du texte (voir Texte.py)
                Jouer : Texte = Texte("Jouer",None,100,(250,250,250),True,True,screen_width,screen_height,screen) 

                #récupération de la position de la souris
                x, y = pg.mouse.get_pos()
             
                #si la souris est sur le texte jouer   
                if Jouer.getRect().collidepoint(x,y) == True:
                            #le texte jouer devient rouge
                            Jouer.setColor((255,0,0),screen)
                
                #si on clique sur le texte jouer
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pg.mouse.get_pos()
                        if Jouer.getRect().collidepoint(x,y) == True:
                            menu.setBool(False)
                            jeu.setBool(True)
                            Jouer.setColor((100,100,100),screen)
                            
                      
                    
            pg.display.update()

        if jeu.getBool() == True:
            menu_sound.stop()
            jeu_sound = pg.mixer.Sound("Sons/Background.wav")
            jeu_sound.play(-1)


        #Boucle du jeu
        while jeu.getBool()==True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                screen.blit(pg.image.load("Images/Background.png"), (0,0))

            
            for ligne in range(nb_lig):
                for colonne in range(nb_col):
                    pg.draw.rect(screen, couleur_gril, (colonne * Taille_case, ligne * Taille_case, Taille_case, Taille_case), 1)
                    
                    #Va chercher l'image des joueurs et ennemis dans la liste et les affichent à leur position respective
                    for i in range(len(ListeJoueur)):
                        if plateau[ligne][colonne] == ListeJoueur[i]:
                            screen.blit(pg.image.load(ListeJoueur[i].getImage()), (colonne * Taille_case-decalj2_g, ligne * Taille_case-decalj2_h ))
                    for i in range(len(ListeEnnemi)):
                        if plateau[ligne][colonne] == ListeEnnemi[i]:
                            screen.blit(pg.image.load(ListeEnnemi[i].getImage()), (colonne * Taille_case-decalj2_g, ligne * Taille_case-decalj2_h ))
                
            
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
                                if isinstance(plateau[indice_ligne][indice_colonne],Ennemie) == True:
                                    attaquerEnnemi(ListeEnnemi,indice_ligne,indice_colonne,verif)
                                else:
                                    deplacement(ListeJoueur,indice_ligne,indice_colonne,verif)
                            
                            selection_en_cours.setBool(False)
                            clic_actif.setBool(True)   
            
        
                
            if tour.getInt()%2 == 1:
                deplacementEnnemi(ListeEnnemi)
                tour.setInt(tour.getInt()+1)
                
        
                            
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    clic_actif.setBool(False)

            pg.display.update()
         

        if Lose.getBool() == True:
            jeu_sound.stop()
            lose_sound = pg.mixer.Sound("Sons/Lose.wav")
            lose_sound.play(-1)
            
        while Lose.getBool()==True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
                screen.blit(pg.image.load("Images/Lose.png"), (0,0))
                #affichage du texte jouer en majuscule en noir et en font 50 sur le centre haut de la fenêtre
                retry : Texte = Texte("Quitter",None,100,(250,250,250),True,True,screen_width,screen_height,screen) 

                
                x, y = pg.mouse.get_pos()
                
                if retry.getRect().collidepoint(x,y) == True:
                            #le texte jouer devient rouge
                            retry.setColor((255,0,0),screen)
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pg.mouse.get_pos()
                        if retry.getRect().collidepoint(x,y) == True:
                            sys.exit()
                            
                      
                    
            pg.display.update()
        
        if Win.getBool() == True:
            jeu_sound.stop()
            win_sound = pg.mixer.Sound("Sons/Win.wav")
            win_sound.play(-1)
    
        while Win.getBool()==True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                
                    screen.blit(pg.image.load("Images/Win.png"), (0,0))
                    #affichage du texte jouer en majuscule en noir et en font 50 sur le centre haut de la fenêtre
                    quit : Texte = Texte("Quitter",None,100,(250,250,250),True,True,screen_width,screen_height,screen) 

                    
                    x, y = pg.mouse.get_pos()
                    
                    if quit.getRect().collidepoint(x,y) == True:
                                #le texte jouer devient rouge
                                retry.setColor((0,0,255),screen)
                    
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            x, y = pg.mouse.get_pos()
                            if quit.getRect().collidepoint(x,y) == True:
                                sys.exit()
                                
                        
                        
                pg.display.update()