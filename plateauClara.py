from upemtk import image
from upemtk import cercle
from upemtk import donne_ev
from upemtk import type_ev
from upemtk import touche
from upemtk import efface

from math import sqrt
from random import randint
from chess import *


"""
Retournement TPN°6.

Code testé sur pyvala
(TD6_Liste) TD6_Liste clara$ pylava retournement.py
(TD6_Liste) TD6_Liste clara$

Usage:
======
    python retournement.py
    nécésssité de la librairie upemtk.py
"""

__authors__ = "Clara Correia"
__contact__ = "clara.correia.sne@gmail.com"
__version__ = "1.0.0"
__date__ = "14/12/2020"

from upemtk import rectangle
from upemtk import mise_a_jour
from upemtk import cree_fenetre
from upemtk import abscisse_souris
from upemtk import ordonnee_souris
from upemtk import attend_clic_gauche
from upemtk import efface_tout
from upemtk import texte
from upemtk import ferme_fenetre
from time import sleep  # librairie pour ralentir le temps d'affichage


def affiche_ouverture(taille_ecran, picture):
    """
    Permet d'afficher une image dans la fenetre

    :param taille_ecran:
    :param picture: int
    :return: str
            nom de l'image gif passe a afficher.

    """
    image(taille_ecran // 2, taille_ecran // 2, picture, tag='image')
    mise_a_jour()
    attend_clic_gauche()
    efface_tout()


def distance(xa, ya, xb, yb):
    """
        Permet de savoir une distance entre 2 points

            Parameters
            ----------
            xa  : int
                abscisse x d'un point A
            ya  : int
                ordonnee y d'un point A
            xb  : int
                abscisse x d'un point B
            yb  : int
                ordonne y d'un point B

            Returns
             -------
            int
                Le resultat du calcul.

            """
    return sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


def affiche_menu(ecran, rayon):
    """

    :param ecran:
    :param rayon:
    :return:
    """
    menu = True
    action_menu = 0
    decallage = ecran // 6
    while menu:
        init_x = ecran // 3
        init_y = ecran // 2
        texte(init_x - decallage - 30, init_y - 5, 'PARAMS', 'black', 'nw',
              'Helvetica', 15)
        cercle(init_x - decallage, init_y, rayon)
        texte(2 * init_x - decallage - 25, init_y - 5, 'JOUER', 'black', 'nw',
              'Helvetica', 15)
        cercle(2 * init_x - decallage, init_y, rayon)
        texte(3 * init_x - decallage - 33, init_y - 5, 'QUITTER', 'black',
              'nw', 'Helvetica', 15)
        cercle(3 * init_x - decallage, init_y, rayon)
        attend_clic_gauche()  # attente d'un choix parmi les trois propositions
        # verifie les coo du clic de la souris
        action_menu = click_cercle_accueil(ecran, rayon, abscisse_souris(),
                                           ordonnee_souris())
        mise_a_jour()
        if action_menu > 0:
            menu = False
    return action_menu


def click_cercle_accueil(ecran, rayon, coo_x, coo_y):
    """

    :param ecran:
    :param rayon:
    :param coo_x:
    :param coo_y:
    :return:
    """
    decallage = ecran // 6
    init_x = ecran // 3
    init_y = ecran // 2
    # param action==1
    if distance(coo_x, coo_y, init_x - decallage, init_y) < rayon:
        return 1
    # rejouer action==2
    elif distance(coo_x, coo_y, 2 * init_x - decallage, init_y) < rayon:
        return 2
    # quitte action==3
    elif distance(coo_x, coo_y, 3 * init_x - decallage, init_y) < rayon:
        return 3
    else:
        return 0


def affiche_param(ecran, rayon):
    menu = True
    action_param = 0
    decallage = ecran // 8
    while menu:
        init_x = ecran // 4
        init_y = ecran // 2
        texte(init_x - decallage - 30, init_y - 5, 'JOUEUR', 'black', 'nw',
              'Helvetica', 15)
        cercle(init_x - decallage, init_y, rayon)
        texte(2 * init_x - decallage - 25, init_y - 5, 'REPLAY', 'black', 'nw',
              'Helvetica', 15)
        cercle(2 * init_x - decallage, init_y, rayon)
        texte(3 * init_x - decallage - 37, init_y - 5, 'INIT GAME', 'black',
              'nw', 'Helvetica', 15)
        cercle(3 * init_x - decallage, init_y, rayon)
        texte(4 * init_x - decallage - 30, init_y - 5, 'QUITTER', 'black',
              'nw', 'Helvetica', 15)
        cercle(4 * init_x - decallage, init_y, rayon)
        attend_clic_gauche()  # attente d'un choix parmi les trois propositions
        # verifie les coo du clic de la souris
        action_param = click_cercle_param(ecran, rayon, abscisse_souris(),
                                          ordonnee_souris())
        mise_a_jour()
        if action_param > 0:
            menu = False
    return action_param


def click_cercle_param(ecran, rayon, coo_x, coo_y):
    """

    :param ecran:
    :param rayon:
    :param coo_x:
    :param coo_y:
    :return:
    """
    decallage = ecran // 8
    init_x = ecran // 4
    init_y = ecran // 2
    # param joueur == 1
    if distance(coo_x, coo_y, init_x - decallage, init_y) < rayon:
        return 1
    # rejouer replay == 2
    elif distance(coo_x, coo_y, 2 * init_x - decallage, init_y) < rayon:
        return 2
    # quitte initialiser jeu == 3
    elif distance(coo_x, coo_y, 3 * init_x - decallage, init_y) < rayon:
        return 3
    # quitte action == 4
    elif distance(coo_x, coo_y, 4 * init_x - decallage, init_y) < rayon:
        return 4
    else:
        return 0


def test_touche(nom, evenement, taille):
    """

    :param nom:
    :param evenement:
    :return:
    """
    if touche(evenement) == 'BackSpace':
        nom = nom[0:-1]
    elif touche(evenement) == 'space':
        nom += " "
    elif touche(evenement) in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
                               'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                               'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2',
                               '3', '4', '5', '6', '7', '8', '9', '0']:
        if len(nom) < taille:
            nom += touche(evenement)
    return nom


def affiche_param_joueur(ecran, rayon, param):
    """
        Permet d'afficher les option de parametres

        :param ecran: int
        :param rayon: int
        :param param: list
        :return: tuple

    """
    menu = True
    nom_j1 = param[0]
    nom_j2 = param[3]
    joueur_focus = 0
    taille_max = 30
    while menu:
        efface_tout()
        valide = False
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Touche':
            if joueur_focus == 1:
                nom_j1 = test_touche(nom_j1, ev, taille_max)
            elif joueur_focus == 2:
                nom_j2 = test_touche(nom_j2, ev, taille_max)
        elif type_ev(ev) == 'ClicGauche':
            joueur_focus = click_param_joueur(abscisse_souris(),
                                              ordonnee_souris())
            print(f"focus {joueur_focus}")
            param, valide = click_cercle_param_joueur(ecran, rayon,
                                                      abscisse_souris(),
                                                      ordonnee_souris(), param)
            print(f"retour click {param} {valide}")
        # Texte nom du joueur
        texte(40, 160, 'JOUEUR 1 :', 'black', 'nw', 'Helvetica', 24)
        rectangle(180, 150, 600, 200)
        texte(185, 160, nom_j1)
        # Choix de la couleur
        texte(180, 220, 'Blanc : ', 'black', 'nw', 'Helvetica', 24)
        texte(180, 270, 'Noir : ', 'black', 'nw', 'Helvetica', 24)
        texte(180, 420, 'Blanc : ', 'black', 'nw', 'Helvetica', 24)
        texte(180, 470, 'Noir : ', 'black', 'nw', 'Helvetica', 24)
        if param[1] == "B":
            cercle(280, 235, 10, remplissage='black')
            cercle(280, 285, 10)
            cercle(280, 435, 10)
            cercle(280, 485, 10, remplissage='black')
        else:
            cercle(280, 235, 10)
            cercle(280, 285, 10, remplissage='black')
            cercle(280, 435, 10, remplissage='black')
            cercle(280, 485, 10)
        # Choix de la position
        texte(380, 220, 'Haut : ', 'black', 'nw', 'Helvetica', 24)
        texte(380, 270, 'Bas : ', 'black', 'nw', 'Helvetica', 24)
        texte(380, 420, 'Haut : ', 'black', 'nw', 'Helvetica', 24)
        texte(380, 470, 'Bas : ', 'black', 'nw', 'Helvetica', 24)
        if param[2] == "H":
            cercle(480, 235, 10, remplissage='black')
            cercle(480, 285, 10)
            cercle(480, 435, 10)
            cercle(480, 485, 10, remplissage='black')
        else:
            cercle(480, 235, 10)
            cercle(480, 285, 10, remplissage='black')
            cercle(480, 435, 10, remplissage='black')
            cercle(480, 485, 10)
        texte(40, 360, 'JOUEUR 2 :', 'black', 'nw', 'Helvetica', 24)
        rectangle(180, 350, 600, 400)
        texte(185, 360, nom_j2)
        # Validation
        cercle(ecran // 2, ecran - 100, rayon)
        texte(ecran // 2 - 30, ecran - 105, "VALIDER", 'black', 'nw',
              'Helvetica', 15)
        mise_a_jour()
        if valide:
            menu = False
    param[0] = nom_j1
    param[3] = nom_j2
    return param


def click_param_joueur(coo_x, coo_y):
    if 180 < coo_x < 600 and 150 < coo_y < 200:
        return 1
    elif 180 < coo_x < 600 and 350 < coo_y < 400:
        return 2
    else:
        return 0


def click_cercle_param_joueur(ecran, rayon, coo_x, coo_y, param):
    """
        Permet de vérifie que le clique de la souris est bien dans les options

        :param ecran: int
        :param rayon: int
        :param coo_x: int
        :param coo_y: int
        :param param: list
        :return: tuple
            (list, booleens)
                parametre mis a jour
                booleeen qui retourne True si les parametres sont valide
           """
    # Test Validation
    if distance(coo_x, coo_y, ecran // 2, ecran - 100) < rayon:
        return param, True
    # Blanc joueur 1 ou Noir Joueur 2
    elif distance(coo_x, coo_y, 280, 235) < 10 or distance(coo_x, coo_y, 280,
                                                           485) < 10:
        param[1] = "B"
        return param, False
    # Noir joueur 1 ou Blanc joueur 2
    elif distance(coo_x, coo_y, 280, 285) < 10 or distance(coo_x, coo_y, 280,
                                                           435) < 10:
        param[1] = "N"
        return param, False
    # Haut joueur 1 ou # Bas joueur 2
    elif distance(coo_x, coo_y, 480, 235) < 10 or distance(coo_x, coo_y, 480,
                                                           485) < 10:
        param[2] = "H"
        return param, False
    # Bas joueur 1 ou Haut joueur 2
    elif distance(coo_x, coo_y, 480, 285) < 10 or distance(coo_x, coo_y, 480,
                                                           435) < 10:
        param[2] = "B"
        return param, False
    else:
        return param, False


def affiche_param_replay(ecran, rayon):
    """
        Permet d'afficher les option de parametres

        :param ecran: int
        :param rayon: int
        :return: tuple

    """
    menu = True
    taille_max = 64
    fichier = ""
    while menu:
        efface_tout()
        valide = False
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Touche':
            fichier = test_touche(fichier, ev, taille_max)
        elif type_ev(ev) == 'ClicGauche':
            valide = click_cercle_param_replay(ecran, rayon, abscisse_souris(),
                                               ordonnee_souris())
        # Texte nom du joueur
        texte(20, 170, 'NOM FICHIER :', 'black', 'nw', 'Helvetica', 15)
        rectangle(130, 150, 670, 200)
        texte(135, 170, fichier, taille=15)
        # Validation
        cercle(ecran // 2, ecran - 100, rayon)
        texte(ecran // 2 - 30, ecran - 105, "VALIDER", 'black', 'nw',
              'Helvetica', 15)
        mise_a_jour()
        if valide:
            menu = False
    return fichier


def click_cercle_param_replay(ecran, rayon, coo_x, coo_y):
    """
        Permet de vérifie que le clique de la souris est bien dans les options

        :param ecran: int
        :param rayon: int
        :param coo_x: int
        :param coo_y: int
        :return: tuple
            (list, booleens)
                parametre mis a jour
                booleeen qui retourne True si les parametres sont valide
           """
    # Test Validation
    if distance(coo_x, coo_y, ecran // 2, ecran - 100) < rayon:
        return True


def affiche_param_init(ecran, rayon):
    """
        Permet d'afficher les option de parametres

        :param ecran: int
        :param rayon: int
        :return: tuple

    """
    menu = True
    taille_max = 64
    fichier = ""
    position_focus = -1
    choix = -1
    while menu:
        efface_tout()
        valide = False
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Touche' and position_focus == 1:
            fichier = test_touche(fichier, ev, taille_max)
        elif type_ev(ev) == 'ClicGauche':
            position_focus = click_param_init(abscisse_souris(),
                                              ordonnee_souris())
            choix, valide = click_cercle_param_init(ecran, rayon,
                                                    abscisse_souris(),
                                                    ordonnee_souris(), choix)
        if position_focus == 1:
            choix = -1
        if choix >= 0:
            fichier = ""
            position_focus = 0
        # Texte position
        texte(40, 170, 'position :', 'black', 'nw', 'Helvetica', 15)
        rectangle(130, 150, 670, 200)
        texte(135, 170, fichier, taille=15)
        # Choix de la position initiale
        texte(40, 225, "Standard", 'black', 'nw',
              'Helvetica', 15)
        texte(40, 255, "Prise en passant", 'black', 'nw',
              'Helvetica', 15)
        texte(40, 285, 'Rocque', 'black', 'nw', 'Helvetica', 15)
        texte(40, 315, 'Pion evolution', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 345, 'deplacement tour', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 375, 'deplacement fou', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 405, 'deplacement cheval', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 435, 'deplacement roi', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 465, 'deplacement rene', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 495, 'deplacement pion', 'black', 'nw',
              'Helvetica', 15)
        texte(40, 525, 'Jeux Mat en 2 coups', 'black', 'nw',
              'Helvetica', 15)
        cercle(200, 230, 10)
        cercle(200, 260, 10)
        cercle(200, 290, 10)
        cercle(200, 320, 10)
        cercle(200, 350, 10)
        cercle(200, 380, 10)
        cercle(200, 410, 10)
        cercle(200, 440, 10)
        cercle(200, 470, 10)
        cercle(200, 500, 10)
        cercle(200, 530, 10)
        if position_focus == 0:
            cercle(200, 260 + (30 * (choix - 1)), 10, remplissage='black')
        # Validation
        cercle(ecran // 2, ecran - 100, rayon)
        texte(ecran // 2 - 30, ecran - 105, "VALIDER", 'black', 'nw',
              'Helvetica', 15)
        mise_a_jour()
        if valide:
            menu = False
    return fichier, choix


def click_param_init(coo_x, coo_y):
    if 130 < coo_x < 670 and 150 < coo_y < 200:
        return 1
    else:
        return -1


def click_cercle_param_init(ecran, rayon, coo_x, coo_y, option):
    """
        Permet de vérifie que le clique de la souris est bien dans les options

        :param ecran: int
        :param rayon: int
        :param coo_x: int
        :param coo_y: int
        :param option: int
        :return: tuple
            (list, booleens)
                parametre mis a jour
                booleeen qui retourne True si les parametres sont valide
           """
    # Test Validation
    if distance(coo_x, coo_y, ecran // 2, ecran - 100) < rayon:
        return option, True
    for i in range(0, 11):
        if distance(coo_x, coo_y, 200, 230 + (30 * i)) < 10:
            return i, False
    return option, False


def genrique(hauteur_plateau):
    efface_tout()
    hauteur_generique = hauteur_plateau + 10
    while hauteur_generique > -200:
        texte(150, hauteur_generique, 'CLARA CORREIA')
        texte(150, hauteur_generique + 30, 'LAURIE BEHLOUL')
        texte(150, hauteur_generique + 60, 'CPES 1')
        texte(150, hauteur_generique + 90, 'Jean Moulin')
        texte(150, hauteur_generique + 120, 'UPEM MLV 1° annee')
        hauteur_generique -= 20
        mise_a_jour()
        sleep(0.2)
        efface_tout()


def pixel_vers_case(top_x, top_y, x, y, ratio):
    """
    Permet de transformer une coo de pixel en coo de plateau
    :param top_x: int, coo x
    :param top_y: int, coo x
    :param x: int, coo x
    :param y: int, coo y
    :param ratio: int, ratio nb pixel par taille du carré
    :return: tuple, coo de la case

    >>> pixel_vers_case(10, 10, 50, 40, 10)
    (4, 3)
    """
    case_x = (x - top_x) // ratio
    case_y = (y - top_y) // ratio
    return case_x, case_y


def case_vers_pixel(x, y, largeur, largeur_jeu, decallage_plateau, ratio):
    """
    Permet de transformer une coo de pixel en coo de plateau
    :param x:
    :param y:
    :param largeur:
    :param largeur_jeu:
    :param decallage_plateau:
    :param ratio:
    :return:

    >>> case_vers_pixel(1, 2, 50, 40, 1, 10)
    (34, 20)
    """
    # On inverse les coordonnées du fait que l'on lit ligne colonne
    top_x = largeur - decallage_plateau - largeur_jeu
    top_y = (largeur - largeur_jeu) // 2
    case_x = top_x + y * ratio + ratio // 2
    case_y = top_y + x * ratio + ratio // 2
    return case_x, case_y


def dessine_jeu(largeur, largeur_jeu, decallage_plateau, nb_carre_ligne,
                name, param):
    """
    Permet de dessiner un plateau de jeu avec des carrees rouge ou blanc
    en fonction du plateau de jeu
    :param largeur:
    :param largeur_jeu:
    :param decallage_plateau:
    :param nb_carre_ligne:
    :param name:
    :param param:
    :return: Affichage upemtk du plateau

    """
    decallage_alphabet = 30
    decallage_numero = 10
    regul_police = 12
    top_x = largeur - decallage_plateau - largeur_jeu
    top_y = (largeur - largeur_jeu) // 2
    ratio = largeur_jeu // nb_carre_ligne
    top_label_x = top_x
    top_label_y = top_y
    # Nom du jeu
    texte(largeur // 2 - (len(name) // 2), 30, name, taille=regul_police * 2)
    # Nom des joueurs
    if param[2] == 'B':
        texte(20, top_y + (ratio // 4), param[3], taille=regul_police * 2)
        texte(20, ratio * (nb_carre_ligne + 1), param[0],
              taille=regul_police * 2)
    else:
        texte(20, top_y + (ratio // 4), param[0], taille=regul_police * 2)
        texte(20, ratio * (nb_carre_ligne + 1), param[3],
              taille=regul_police * 2)
    alphabet = ["H", "G", "F", "E", "D", "C", "B", "A"]
    for i in range(nb_carre_ligne):
        texte(top_label_x - regul_police + ratio // 2,
              top_y - decallage_alphabet, alphabet[i], taille=regul_police * 2)
        top_label_x += ratio
    for i in range(nb_carre_ligne):
        texte(top_x + (ratio * nb_carre_ligne) + decallage_numero,
              top_label_y - regul_police + ratio // 2, str(i + 1),
              taille=regul_police * 2)
        top_label_y += ratio
    for line in range(nb_carre_ligne):
        for col in range(nb_carre_ligne):
            if line % 2 == col % 2:
                rectangle(top_x, top_y, top_x + ratio, top_y + ratio,
                          couleur='black', remplissage='white')
            else:
                rectangle(top_x, top_y, top_x + ratio, top_y + ratio,
                          couleur='black', remplissage='brown')
            top_y += ratio
        top_x += ratio
        top_y = (largeur - largeur_jeu) // 2
    image(top_x - (3 * largeur_jeu // 4), largeur - 50, "I_recul.png")
    rectangle(top_x - (2 * largeur_jeu // 4) - 40,
              largeur - 75, top_x - (2 * largeur_jeu // 4) + 38, largeur - 27,
              epaisseur=4)
    image(top_x - (largeur_jeu // 4), largeur - 50, "I_avance.png")
    mise_a_jour()
    attend_clic_gauche()


def dessine_plateau(largeur, largeur_jeu, decallage_plateau, nb_carre_ligne,
                    j1, j2, param, nb_coups):
    """
    Permet de dessiner un plateua de jeu avec des carrees rouge ou blanc
    en fonction du plateau de jeu
    :param largeur:
    :param largeur_jeu:
    :param decallage_plateau:
    :param nb_carre_ligne:
    :param j1:
    :param j2:
    :param param:
    :param nb_coups:
    :return: Affichage upemtk du plateau

    """

    score_j1, score_j2 = score(j1, j2)
    ratio = largeur_jeu // nb_carre_ligne
    top_x = largeur - decallage_plateau - largeur_jeu
    top_y = (largeur - largeur_jeu) // 2
    # Nom des joueurs
    if param[2] == 'B':
        texte(20, top_y + (ratio // 4) + 30,  "score : " + str(score_j2),
              taille=20)
        texte(20, ratio * (nb_carre_ligne + 1) + 30,  "score : " + str(
            score_j1), taille=20)
    else:
        texte(20, top_y + (ratio // 4) + 30,  "score : " + str(score_j1),
              taille=20)
        texte(20, ratio * (nb_carre_ligne + 1) + 30,  "score : " + str(
            score_j2), taille=20)
    index = 0
    efface('piece')
    for piece in j1:
        piece_x, piece_y = case_vers_pixel(piece[1][0], piece[1][1], largeur,
                                           largeur_jeu, decallage_plateau,
                                           ratio)
        dessine_piece("P_" + str(piece[0]) + "_B", piece_x, piece_y,
                      str(piece[0]) + str(index))
    for piece in j2:
        piece_x, piece_y = case_vers_pixel(piece[1][0], piece[1][1], largeur,
                                           largeur_jeu, decallage_plateau,
                                           ratio)
        dessine_piece("P_" + str(piece[0]) + "_N", piece_x, piece_y,
                      str(piece[0]) + str(index))
    texte(top_x + (2 * largeur_jeu // 4) - 10, largeur - 65, nb_coups,
          taille=24)
    mise_a_jour()
    attend_clic_gauche()


def dessine_piece(type_piece, x, y, name):
    image(x, y, type_piece + ".png", tag='piece')
    mise_a_jour()


def get_piece(piece):
    if piece == 'r' or piece == 'R':
        return "T"
    elif piece == 'n' or piece == 'N':
        return "C"
    elif piece == 'b' or piece == 'B':
        return "F"
    elif piece == 'q' or piece == 'Q':
        return "D"
    elif piece == 'k' or piece == 'K':
        return "R"
    elif piece == 'p' or piece == 'P':
        return "P"


def inverse_plateau(j1, j2):
    inv_j1 = []
    inv_j2 = []
    for j in j1:
        inv_j1.append((j[0], (abs(j[1][0] - 7), abs(j[1][1] - 7))))
    for j in j2:
        inv_j2.append((j[0], (abs(j[1][0] - 7), abs(j[1][1] - 7))))
    return inv_j1, inv_j2


def position_initiale(definition, param):
    """

    :param definition:
    :param param:
    :return:
    """
    joueur_noir = []
    joueur_blanc = []
    index_x = 0
    index_y = 0
    for c in definition:
        if c.isdigit():
            index_x += int(c)
        elif c == '/':
            index_x = 0
            index_y += 1
        elif c.islower():
            joueur_noir.append([get_piece(c), (index_y, index_x)])
            index_x += 1
        elif c.isupper():
            joueur_blanc.append([get_piece(c), (index_y, index_x)])
            index_x += 1
        else:
            break
    if param[1] == "B":
        joueur1 = joueur_blanc
        joueur2 = joueur_noir
    else:
        joueur1 = joueur_noir
        joueur2 = joueur_blanc
    if param[2] == "H":
        joueur1, joueur2 = inverse_plateau(joueur1, joueur2)
    return joueur1, joueur2


def init_plateau():
    normal = ("Standard", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w "
                          "KQkq - 0 1")
    prise_en_passant = ("Prise en passant",  "8/pppp1ppp/8/3Pp3/8/8/8/8 w "
                                             "KQkq e4 0 1")
    rocque = ("Rocque", "r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1")
    pion_upgrade = ("Pion Upgrade", "8/P/8/43/8/8/p/8 w KQkq - 0 1")
    deplacment_tour = ("Tour", "8/8/8/4r3/8/8/8/8 w KQkq - 0 1")
    deplacement_fou = ("Fou", "8/8/8/4b3/8/8/8/8 w KQkq - 0 1")
    deplacement_cheval = ("Cheval", "8/8/8/4n3/8/8/8/8 w KQkq - 0 1")
    deplacement_roi = ("Le Roi", "8/8/8/4k3/8/8/8/8 w KQkq - 0 1")
    deplacement_dame = ("La Dame", "8/8/8/4q3/8/8/8/8 w KQkq - 0 1")
    deplacement_pion = ("Le Pion",  "8/ppp2ppp/3p4/4p3/8/3P4/PPPpPPPP/8 w "
                                    "KQkq - 0 1")
    mat_2_coups = [("Tigran Gharamian", "8/8/8/8/1B6/NN6/pk1K4/8 w - 0 ""0"), (
        "Anthony Wirig", "8/1p1P1p2/8/2pPp3/2PkP3/3P4/3K4/8 w - 0 0"),
                   ("Quotidien", "8/6Bp/8/6kp/4k1b1/4P1Q1/7K/8 w - 0 0")]
    return [normal, prise_en_passant, rocque, pion_upgrade, deplacment_tour,
            deplacement_fou, deplacement_cheval, deplacement_roi,
            deplacement_dame, deplacement_pion, mat_2_coups]


def score_piece(piece):
    """

    :param piece: str
    :return: int
    """
    score_pion = 1
    score_tour = 6
    score_cavalier = 3
    score_fou = 3
    score_reine = 9
    if piece == "P":
        return int(score_pion)
    elif piece == "T":
        return int(score_tour)
    elif piece == "C":
        return int(score_cavalier)
    elif piece == "F":
        return int(score_fou)
    elif piece == "D":
        return int(score_reine)
    else:
        return 0


def score(j1, j2):
    """

    :param j1:
    :param j2:
    :return:
    """
    score_j1 = 0
    score_j2 = 0
    for j in j1:
        score_j1 += score_piece(j[0])
    for j in j2:
        score_j2 += score_piece(j[0])
    return score_j1, score_j2


def check_avance(pos_x, pos_y):
    if 515 < pos_x < 565 and 625 < pos_y < 675:
        return True
    return False


def check_recul(pos_x, pos_y):
    if 265 < pos_x < 315 and 625 < pos_y < 675:
        return True
    return False


def set_joueur(option, init, gameplay, plateau, param, file_replay):
    """
    :param option:
    :param init:
    :param gameplay:
    :param plateau:
    :param param:
    :param file_replay:
    :return: tuple

    >>> set_joueur(1, "", 0, [("Le Roi", "8/8/8/4K3/8/8/8/8 w KQkq - 0 1")], \
    ["j1", "B", "B", "J2"], "")
    ([['R', (3, 4)]], [], 'Le Roi')
    """

    # On joue en replay on doit charger le jeu pour le consulter  on
    # ne prends pas les autres options
    gameplay_name = ""
    if option == 2:
        j1, j2 = position_initiale(plateau[0][1], param)
        gameplay_name = plateau[0][0]
    else:
        # On regarde si on doit charger un jeu
        if init != "":
            filin = open(init + ".jeu", "r")
            chaine_a_construire = filin.readline()
            j1, j2 = position_initiale(chaine_a_construire, param)
            filin.close()
        # On a selectionner un jeu
        elif gameplay >= 0:
            # Cas particulier du mat en 2 coups on choisi
            # aléatoirement un jeu
            if gameplay == 10:
                num_jeu = randint(0, 2)
                j1, j2 = position_initiale(plateau[gameplay][num_jeu][1],
                                           param)
                gameplay_name = plateau[gameplay][num_jeu][0]
            # On charge le jeu
            else:
                j1, j2 = position_initiale(plateau[gameplay][1], param)
                gameplay_name = plateau[gameplay][0]
        # Si on n a pas selectionne de jeu alors on charge le standard
        else:
            j1, j2 = position_initiale(plateau[0][1], param)
            gameplay_name = plateau[0][0]
    return j1, j2, gameplay_name


def main():
    """
    j1 = [['P', (1, 0)], ['P', (1, 1)], ['P', (1, 2)], ['P', (1, 3)],
          ['P', (1, 4)], ['P', (1, 5)], ['P', (1, 6)], ['P', (1, 7)],
          ['T', (0, 0)], ['T', (0, 7)], ['C', (0, 1)], ['C', (0, 6)],
          ['F', (0, 2)], ['F', (0, 5)], ['R', (0, 3)], ['D', (0, 4)]]
    j2 = [['P', (6, 0)], ['P', (6, 1)], ['P', (6, 2)], ['P', (6, 3)],
          ['P', (6, 4)], ['P', (6, 5)], ['P', (6, 6)], ['P', (6, 7)],
          ['T', (7, 0)], ['T', (7, 7)], ['C', (7, 1)], ['C', (7, 6)],
          ['F', (7, 2)], ['F', (7, 5)], ['R', (7, 3)], ['D', (7, 4)]]
    chaine = "5k2/p1p2p2/5N1P/1p4r1/8/1P6/5R2/7K"
    chaine = jeu()[1][1]
    """
    plateau = init_plateau()
    nb_case_echec = 8
    taille_ecran = 700
    taille_jeu = 500
    decallage_plateau = 30
    rayon_selection = 50
    param = ["Joueur1", "B", "B", "Joueur2"]
    cree_fenetre(taille_ecran, taille_ecran)
    affiche_ouverture(taille_ecran, "chess.png")
    menu = 0
    file_replay = ""
    init = ""
    gameplay_name = "Standard"
    option = 0
    gameplay = -1
    while menu < 3:
        efface_tout()
        menu = affiche_menu(taille_ecran, rayon_selection)
        efface_tout()
        if menu == 1:
            option = affiche_param(taille_ecran, rayon_selection)
            if option == 1:
                param = affiche_param_joueur(taille_ecran, rayon_selection,
                                             param)
            elif option == 2:
                file_replay = affiche_param_replay(taille_ecran,
                                                   rayon_selection)
            elif option == 3:
                init, gameplay = affiche_param_init(taille_ecran,
                                                    rayon_selection)
        # On joue
        elif menu == 2:
            if file_replay == "":
                j1, j2, gameplay_name = set_joueur(option, init, gameplay,
                                                   plateau, param, replay)
            elif len(file_replay) > 0:
                print(f"{file_replay}")
                replay_jeu_complet, gameplay_name = replay(file_replay +
                                                           ".txt")
                j1, j2 = position_initiale(plateau[0][1], param)
            print(f"param {param}")
            dessine_jeu(taille_ecran, taille_jeu, decallage_plateau,
                        nb_case_echec, gameplay_name, param)
            dessine_plateau(taille_ecran, taille_jeu, decallage_plateau,
                            nb_case_echec, j1, j2, param, 0)
            ratio = taille_jeu // nb_case_echec
            top_x = taille_ecran - decallage_plateau - taille_jeu
            top_y = (taille_ecran - taille_jeu) // 2
            idx_partie = 0
            while True:
                # attend_clic_gauche()
                dessine_plateau(taille_ecran, taille_jeu, decallage_plateau,
                                nb_case_echec, j1, j2, param, 0)
                pos_y, pos_x = pixel_vers_case(top_x, top_y, abscisse_souris(),
                                               ordonnee_souris(), ratio)

                if check_avance(abscisse_souris(), ordonnee_souris()):
                    print("AVANCE")
                    idx_partie += 1
                    if idx_partie > len(replay_jeu_complet):
                        idx_partie = len(replay_jeu_complet) - 2
                    print(f"{idx_partie} {replay_jeu_complet[idx_partie]}")
                    if idx_partie % 2 == 0:
                        j1 = replay_jeu_complet[idx_partie]
                    else:
                        j2 = replay_jeu_complet[idx_partie]

                elif check_recul(abscisse_souris(), ordonnee_souris()):
                    print("RECUL")
                    idx_partie -= 1
                    if idx_partie < 0:
                        idx_partie = 0
                    if idx_partie % 2 == 0:
                        j1 = replay_jeu_complet[idx_partie]
                    else:
                        j2 = replay_jeu_complet[idx_partie]
                print(f"X {pos_x} Y {pos_y}")

    genrique(taille_ecran)
    ferme_fenetre()


if __name__ == '__main__':
    main()
