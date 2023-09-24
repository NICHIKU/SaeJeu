from __future__ import annotations
import pygame as pg 
import sys
from Chevalier import Chevalier
from Arme import Arme 

if __name__ == "__main__":
    pg.init()
    # Création de la fenêtre
    nb_lig = 8
    nb_col = 12
    Taille_case = 64
    couleur_gril=(133,192,0)
    
    decalsolaire_g = 8
    decalsolaire_h = 10

    decalknight_g=10
    decalknight_h=25

    screen_color = (100,100,100)
    screen_width = nb_col*Taille_case
    screen_height = nb_lig*Taille_case

    Epee : Arme = Arme(30,"Epée")
    moi : Chevalier =Chevalier('Chevalier renforcée',Epee)
    Solaire : Chevalier = Chevalier ('Solaire',Epee)
    Solaire.setImage("Images/solaire.png")

    plateau = [[None] * nb_col for _ in range(nb_lig)]    
    plateau[1][2] = moi
    plateau[2][2] = Solaire

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Dark info")


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        screen.fill(screen_color)
        
        for ligne in range(nb_lig):
         for colonne in range(nb_col):
            pg.draw.rect(screen, couleur_gril, (colonne * Taille_case, ligne * Taille_case, Taille_case, Taille_case), 1)
            if plateau[ligne][colonne] ==moi:
                    screen.blit(pg.image.load(moi.getImage()), (colonne * Taille_case-decalknight_g, ligne * Taille_case-decalknight_h ))
                    x_moi = ligne
                    y_moi = colonne
            elif plateau[ligne][colonne] ==Solaire:
                    screen.blit(pg.image.load(Solaire.getImage()), (colonne * Taille_case-decalsolaire_g, ligne * Taille_case-decalsolaire_h ))
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Vérifie le bouton gauche de la souris
                x, y = pg.mouse.get_pos()
                indice_colonne = x // Taille_case
                indice_ligne = y // Taille_case

                # Vérifiez que les indices sont dans les limites de la grille
                if 0 <= indice_colonne < nb_col and 0 <= indice_ligne < nb_lig:
                    # Utilisez les indices pour accéder à la cellule de la grille
                    plateau[x_moi][y_moi]=None
                    plateau[indice_ligne][indice_colonne] = moi
                    


        pg.display.update()
