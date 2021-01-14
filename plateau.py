# coding: utf-8
"""
JEUX D'ECHEC .

Code testé sur pyvala
$ pylava plateau.py
$

Code testé avec doctest
$ python -m doctest plateau.py

Lancé du jeu
$ python plateau.py

Usage:
======
    python echec.py
    nécésssité de :
    >> Le fichier chess.py
    >> Le fichier standard.jeu
    >> La librairie upemtk.py
    >> Les images
        > P_C_B.png
        > P_C_N.png
        > P_D_B.png
        > P_D_N.png
        > P_F_B.png
        > P_F_N.png
        > P_P_B.png
        > P_P_N.png
        > P_R_B.png
        > P_R_N.png
        > P_T_B.png
        > P_T_N.png
        > I_recul.png
        > I_avance.png
        > I_inverse.png
        > I_stop.png
        > chess.png

"""

__authors__ = ("Clara CORREIA", "Laurie BEHLOUL", "Thalya LAUPA")
__contact__ = ("clara.correia.sne@gmail.com", "lauriebehloul1@gmail.com",
               "thalya.laupa@gmail.com")
__version__ = "1.0.0"
__date__ = "01/2021"

from upemtk import rectangle
from upemtk import mise_a_jour
from upemtk import cree_fenetre
from upemtk import abscisse_souris
from upemtk import ordonnee_souris
from upemtk import attend_clic_gauche
from upemtk import efface_tout
from upemtk import texte
from upemtk import ferme_fenetre
from upemtk import image
from upemtk import cercle
from upemtk import donne_ev
from upemtk import type_ev
from upemtk import touche
from upemtk import efface

from chess import check_position_piece
from chess import name_piece
from chess import deplacement_autorise
from chess import replay
from chess import pat
from chess import autre_piece
from chess import is_double_place
from chess import chgmt_pion
from chess import piece_choisit
from chess import transforme_pion
from chess import roi_bouge
from chess import tour_bouge
from chess import sauv_deplacement
from chess import cherche_roi
from chess import echec
from chess import mat
from chess import init_sauvegarde
from chess import sauvegarde
from chess import fin_jeu

from copy import deepcopy

from math import sqrt

from time import sleep  # librairie pour ralentir le temps d'affichage


###########################
#  Fonctions utilitaires  #
###########################
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

        >>> distance(0, 0, 10, 0)
        10.0
            """
    return sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


def test_touche(nom, evenement, taille):
    """
    Permet d'enregistrer les touches de clavier qui peuvent etre tape
    :param nom: str
    :param evenement: str
    :param taille: int
    :return: str
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
                               '3', '4', '5', '6', '7', '8', '9', '0', '.']:
        if len(nom) < taille:
            nom += touche(evenement)
    return nom


def inverse_id_joueur(id_joueur):
    """
    Permet d'inverser l'id du joueur
    :param id_joueur: int
    :return: int

    >>> inverse_id_joueur(0)
    1
    """
    if id_joueur == 0:
        return 1
    else:
        return 0


#########################################
#  Fonctions MENU ET ACTIONS ASSOCIEES  #
#########################################
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


def affiche_accueil(ecran, rayon):
    """
    Permet d'afficher l'ecran d'acceuil
    :param ecran: int
    :param rayon: int
    :return: int
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
    Permet de savoir quel cerlce a été cliqué
    :param ecran: int
    :param rayon: int
    :param coo_x: int
    :param coo_y: int
    :return: int
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
    """
    Permet d'afficher les paramètres
    :param ecran: int
    :param rayon:  int
    :return: int
    """
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
    Permet de savoir quel cerlce a été cliqué dans paramètres
    :param ecran: int
    :param rayon: int
    :param coo_x: int
    :param coo_y: int
    :return: int
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
            param, valide = click_cercle_param_joueur(ecran, rayon,
                                                      abscisse_souris(),
                                                      ordonnee_souris(), param)
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
        if param[2] == -1:
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
        param[2] = -1
        return param, False
    # Bas joueur 1 ou Haut joueur 2
    elif distance(coo_x, coo_y, 480, 285) < 10 or distance(coo_x, coo_y, 480,
                                                           435) < 10:
        param[2] = 1
        return param, False
    else:
        return param, False


def click_param_joueur(coo_x, coo_y):
    """
    Permet de verifier les coo du cercle joueurs
    :param coo_x: int
    :param coo_y: int
    :return: int
    """
    if 180 < coo_x < 600 and 150 < coo_y < 200:
        return 1
    elif 180 < coo_x < 600 and 350 < coo_y < 400:
        return 2
    else:
        return 0


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
        texte(40, 225, "Standard", 'black', 'nw', 'Helvetica', 15)
        texte(40, 255, "Prise en passant", 'black', 'nw', 'Helvetica', 15)
        texte(40, 285, 'Roque', 'black', 'nw', 'Helvetica', 15)
        texte(40, 315, 'Pion evolution', 'black', 'nw', 'Helvetica', 15)
        texte(40, 345, 'deplacement tour', 'black', 'nw', 'Helvetica', 15)
        texte(40, 375, 'deplacement fou', 'black', 'nw', 'Helvetica', 15)
        texte(40, 405, 'deplacement cheval', 'black', 'nw', 'Helvetica', 15)
        texte(40, 435, 'deplacement roi', 'black', 'nw', 'Helvetica', 15)
        texte(40, 465, 'deplacement reine', 'black', 'nw', 'Helvetica', 15)
        texte(40, 495, 'deplacement pion', 'black', 'nw', 'Helvetica', 15)
        texte(40, 525, 'Jeux Mat en 2 coups', 'black', 'nw', 'Helvetica', 15)
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


def click_param_init(coo_x, coo_y):
    """
    Permet de vérifier que le clic est bien dans l'initialisation
    :param coo_x: int
    :param coo_y: int
    :return: int
    """
    if 130 < coo_x < 670 and 150 < coo_y < 200:
        return 1
    else:
        return -1


def generique(hauteur_plateau):
    """
    Affiche le genrique de fin
    :param hauteur_plateau: int
    :return: none
    """
    efface_tout()
    hauteur_generique = hauteur_plateau + 10
    while hauteur_generique > -200:
        texte(150, hauteur_generique, 'CLARA CORREIA')
        texte(150, hauteur_generique + 30, 'LAURIE BEHLOUL')
        texte(150, hauteur_generique + 60, 'THALYA LAUPA')
        texte(150, hauteur_generique + 90, 'CPES 1')
        texte(150, hauteur_generique + 120, 'Jean Moulin')
        texte(150, hauteur_generique + 140, 'UPEM MLV 1° annee')
        hauteur_generique -= 20
        mise_a_jour()
        sleep(0.2)
        efface_tout()


###########################################
#  Fonctions gestion des correspondances  #
###########################################
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
    :param x: iny
    :param y: int
    :param largeur: int
    :param largeur_jeu: int
    :param decallage_plateau: int
    :param ratio: int
    :return: tuple: int, int

    >>> case_vers_pixel(1, 2, 50, 40, 1, 10)
    (34, 20)
    """
    # On inverse les coordonnées du fait que l'on lit ligne colonne
    top_x = largeur - decallage_plateau - largeur_jeu
    top_y = (largeur - largeur_jeu) // 2
    case_x = top_x + y * ratio + ratio // 2
    case_y = top_y + x * ratio + ratio // 2
    return case_x, case_y


def get_piece(piece):
    """
    Permet de traduire les pieces
    :param piece: str
    :return: str

    >>> get_piece('r')
    'T'
    """
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


def check_position_mouvement(pox_x, pos_y, list_mvt):
    """
    Permet de verifier la position du mouvement
    :param pox_x: int
    :param pos_y: int
    :param list_mvt: liste
    :return: booléens

    >>> check_position_mouvement(1,2, [(1,2), (0,3)])
    True
    """
    for mvt in list_mvt:
        if mvt == (pox_x, pos_y):
            return True
    return False


###########################################
#  Fonctions Dessin du jeux               #
###########################################
def dessine_jeu(largeur, largeur_jeu, decallage_plateau, nb_carre_ligne, name,
                action_replay, action_apprentissage):
    """
    Permet de dessiner un plateau de jeu avec des carrees rouge ou blanc
    en fonction du plateau de jeu
    :param largeur:int
    :param largeur_jeu: int
    :param decallage_plateau: int
    :param nb_carre_ligne: int
    :param name: str
    :param action_replay : int
    :param action_apprentissage: int
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
    if action_replay:
        # dessine les cases du jeu
        image(top_x + (3 * largeur_jeu // 4), largeur - 50, "I_avance.png")
        image(top_x + (largeur_jeu // 4), largeur - 50, "I_recul.png")
    elif not action_apprentissage:
        image(125, largeur - 50, "I_inverse.png")
    rectangle(top_x + (2 * largeur_jeu // 4) - 40, largeur - 75,
              top_x + (2 * largeur_jeu // 4) + 38, largeur - 27, epaisseur=4)
    image(50, largeur - 50, "I_stop.png")
    mise_a_jour()


def dessine_plateau(largeur, largeur_jeu, decallage_plateau, nb_carre_ligne,
                    j1, j2, sens_jeux, nb_coups, param, id_joueur):
    """
    Permet de dessiner un plateau de jeu avec des carrees rouge ou blanc
    en fonction du plateau de jeu
    :param largeur: int
    :param largeur_jeu: int
    :param decallage_plateau: int
    :param nb_carre_ligne: int
    :param j1: liste
    :param j2: liste
    :param sens_jeux: 1 joueur qui joue et son adversaie
    :param nb_coups: int
    :param param: int
    :param id_joueur: int
    :return: Affichage upemtk du plateau

    """
    efface('piece')
    efface('score')
    efface('nbCoup')
    efface('joueur')
    efface('tour')
    score_j1, score_j2 = score(j1, j2)
    ratio = largeur_jeu // nb_carre_ligne
    top_x = largeur - decallage_plateau - largeur_jeu
    top_y = (largeur - largeur_jeu) // 2
    # Nom des joueurs
    if id_joueur == 0:
        joueur_b = j1
        joueur_n = j2
        if param[1] == "B":
            tour_joueur = str(param[0])
        else:
            tour_joueur = str(param[3])
    else:
        joueur_b = j2
        joueur_n = j1
        if param[1] == "N":
            tour_joueur = str(param[0])
        else:
            tour_joueur = str(param[3])
    if sens_jeux == -1:
        texte(20, top_y + (ratio // 4), param[3], taille=24, tag="joueur")
        texte(20, ratio * (nb_carre_ligne + 1), param[0],
              taille=24, tag="joueur")
        texte(20, top_y + (ratio // 4) + 30, "score : " + str(score_j2),
              taille=20, tag='score')
        texte(20, ratio * (nb_carre_ligne + 1) + 30,
              "score : " + str(score_j1), taille=20, tag='score')
    else:
        texte(20, top_y + (ratio // 4), param[0], taille=24, tag="joueur")
        texte(20, ratio * (nb_carre_ligne + 1), param[3],
              taille=24, tag="joueur")
        texte(20, top_y + (ratio // 4) + 30, "score : " + str(score_j1),
              taille=20, tag='score')
        texte(20, ratio * (nb_carre_ligne + 1) + 30,
              "score : " + str(score_j2), taille=20, tag='score')
    texte(20, ratio * (nb_carre_ligne + 1) // 2 + 50, tour_joueur,
          taille=24, tag="tour")
    # dessine les pieces
    for piece in joueur_b:
        piece_x, piece_y = case_vers_pixel(piece[1][0], piece[1][1], largeur,
                                           largeur_jeu, decallage_plateau,
                                           ratio)
        dessine_piece("P_" + str(piece[0]) + "_B", piece_x, piece_y)
    for piece in joueur_n:
        piece_x, piece_y = case_vers_pixel(piece[1][0], piece[1][1], largeur,
                                           largeur_jeu, decallage_plateau,
                                           ratio)
        dessine_piece("P_" + str(piece[0]) + "_N", piece_x, piece_y)
    texte(top_x + (2 * largeur_jeu // 4) - 10, largeur - 65, nb_coups // 2,
          taille=24, tag="nbCoup")
    mise_a_jour()


def dessine_case(clear_mouvement, nb_carre_ligne, top_x, top_y, ratio, largeur,
                 largeur_jeu, list_mouvement, list_mange):
    """
    Permet de dessiner des case
    :param clear_mouvement: str
    :param nb_carre_ligne: int
    :param top_x: int
    :param top_y: int
    :param ratio: int
    :param largeur: int
    :param largeur_jeu: int
    :param list_mouvement: liste
    :param list_mange:liste
    :return: none
    """
    efface('case')
    remplissage_paire = "white"
    remplissage_impaire = "brown"
    for line in range(nb_carre_ligne):
        for col in range(nb_carre_ligne):
            if line % 2 == col % 2:
                remplissage_couleur = remplissage_paire
            else:
                remplissage_couleur = remplissage_impaire
            if clear_mouvement:
                if (col, line) in list_mouvement:
                    remplissage_couleur = "Green"
                elif (col, line) in list_mange:
                    remplissage_couleur = "Red"
            rectangle(top_x, top_y, top_x + ratio, top_y + ratio,
                      couleur='black', remplissage=remplissage_couleur,
                      tag='case')
            top_y += ratio
        top_x += ratio
        top_y = (largeur - largeur_jeu) // 2


def dessine_piece(type_piece, x, y):
    """
    Permet d 'afficher les immages des piece
    :param type_piece: str
    :param x: int
    :param y: int
    :return: none
    """
    image(x, y, type_piece + ".png", tag='piece')
    mise_a_jour()


def dessine_mvt(symbole, list_mvt, largeur, largeur_jeu, decallage_plateau,
                nb_carre_ligne):
    """
    Permet d'afficher le mvt en txt a cote pour connaitre le mvt effectue
    :param symbole: str
    :param list_mvt: liste
    :param largeur: int
    :param largeur_jeu: int
    :param decallage_plateau: int
    :param nb_carre_ligne: int
    :return:none
    """
    ratio = largeur_jeu // nb_carre_ligne
    for case_plateau in list_mvt:
        case_x, case_y = case_plateau
        piece_x, piece_y = case_vers_pixel(case_x, case_y, largeur,
                                           largeur_jeu, decallage_plateau,
                                           ratio)
        texte(piece_x, piece_y, symbole, tag="mvt")


def dessine_piece_choisit(choix, couleur):
    """
    Permet d'upgrader le pion
    :param choix: int
    :param couleur: str
    :return:str
    """
    x = 30
    y = 30
    piece_selectionnee = ""
    for selection in choix:
        piece = "P_" + selection + "_" + couleur
        dessine_piece(piece, x, y)
        x += 50
    evolution = False
    while not evolution:
        attend_clic_gauche()
        evolution, piece_selectionnee = \
            check_decision(abscisse_souris(), ordonnee_souris(), choix)
    return piece_selectionnee


def check_decision(pos_x, pos_y, choix):
    """
    Permet de savoir quel decision a prit le joueur
    :param pos_x:  int
    :param pos_y: int
    :param choix: int
    :return: str
    """
    if 10 < pos_x < 50 and 10 < pos_y < 50:
        return True, choix[0]
    elif 60 < pos_x < 100 and 10 < pos_y < 50 and len(choix) > 1:
        return True, choix[1]
    elif 110 < pos_x < 150 and 10 < pos_y < 50 and len(choix) > 2:
        return True, choix[2]
    elif 160 < pos_x < 200 and 10 < pos_y < 50 and len(choix) > 3:
        return True, choix[3]
    return False, ""


def rafraichir_plateau(clear_mouvement, nb_case_echec, top_x, top_y, ratio,
                       taille_ecran, taille_jeu, sens_jeux, joueur_qui_joue,
                       adversaire,  list_mvt_deplacement, list_mvt_mange,
                       decallage_plateau, param, nb_coup_joue, id_joueur):
    """
    Permet de rafraichir le plateau après une action
    :param clear_mouvement: int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param ratio: int
    :param taille_ecran:int
    :param taille_jeu: int
    :param sens_jeux: int
    :param joueur_qui_joue:liste
    :param adversaire: liste
    :param list_mvt_deplacement:liste
    :param list_mvt_mange: liste
    :param decallage_plateau: int
    :param param: int
    :param nb_coup_joue:str
    :param id_joueur: int
    :return: none
    """
    dessine_case(clear_mouvement, nb_case_echec, top_x, top_y, ratio,
                 taille_ecran, taille_jeu, list_mvt_deplacement,
                 list_mvt_mange)
    dessine_plateau(taille_ecran, taille_jeu, decallage_plateau, nb_case_echec,
                    joueur_qui_joue, adversaire, sens_jeux, nb_coup_joue,
                    param, id_joueur)


def rafraichir_case(clear_mouvement, nb_case_echec, top_x, top_y, ratio,
                    taille_ecran, taille_jeu, list_mvt_deplacement,
                    list_mvt_mange):
    """
   Permet de rafraichir les cases après une action
    :param clear_mouvement: int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param ratio: int
    :param taille_ecran:int
    :param taille_jeu: int
    :param list_mvt_deplacement:liste
    :param list_mvt_mange: liste
    :return: none
    """
    dessine_case(clear_mouvement, nb_case_echec, top_x, top_y, ratio,
                 taille_ecran, taille_jeu, list_mvt_deplacement,
                 list_mvt_mange)


def dessine_coup_joueur(nb_case_echec, ratio, mouv):
    """
    Permet de rafraichir seulement le coup du joueur
    :param nb_case_echec: int
    :param ratio: int
    :param mouv: str
    :return:none
    """
    efface('mouv')
    texte(20, ratio * (nb_case_echec + 1) // 2 + 80, mouv, taille=24,
          tag="mouv")
    mise_a_jour()


def dessine_tour_joueur(nb_case_echec, ratio, joueur):
    """
    Permet de rafraichir le nombre de tour du jeu
    :param nb_case_echec: int
    :param ratio: int
    :param joueur: int
    :return:none
    """
    efface("tour")
    texte(20, ratio * (nb_case_echec + 1) // 2 + 50, joueur,
          taille=24, tag="tour")
    mise_a_jour()

def dessine_echec_joueur(nb_case_echec, ratio, echec):
    """
    Permet de rafraichir seulement le coup du joueur
    :param nb_case_echec: int
    :param ratio: int
    :param mouv: str
    :return:none
    """
    efface('echec')
    texte(20, ratio * (nb_case_echec + 1) // 2 + 110, echec, taille=24,
          tag="echec", couleur="red")
    mise_a_jour()


###########################################
#  Fonctions Initialisation du jeu        #
###########################################
def position_initiale(definition, param):
    """
    Permet de creer un jeu
    :param definition: str
    :param param: str
    :return: liste

    >>> position_initiale('kq/8/KQ',  ["j1", "B", "B", "J2"])
    ([['R', (2, 0)], ['D', (2, 1)]], [['R', (0, 0)], ['D', (0, 1)]])

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
    if (param[2] == -1 and param[1] == "B") or (
            param[2] == 1 and param[1] == "N"):
        joueur_blanc, joueur_noir = inverse_plateau(joueur_blanc, joueur_noir)
    return joueur_blanc, joueur_noir


def init_plateau():
    """
    return: list ensemble des positions en fonction du jeu choisi
    """
    normal = ("Standard", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w "
                          "KQkq - 0 1")
    prise_en_passant = ("Le Pion", "8/1pppppp1/8/8/8/8/1PPPPPP1/8 w "
                                   "KQkq - 0 1")
    rocque = ("Rocque", "r2k3r/8/8/8/8/8/8/R2K3R w KQkq - 0 1")
    pion_upgrade = ("Pion Upgrade", "8/8/P/8/8/p/8/8 w KQkq - 0 1")
    deplacment_tour = ("Tour", "8/8/8/3rR3/8/8/8/8 w KQkq - 0 1")
    deplacement_fou = ("Fou", "8/8/8/3bB3/8/8/8/8 w KQkq - 0 1")
    deplacement_cheval = ("Cheval", "8/8/8/3nN3/8/8/8/8 w KQkq - 0 1")
    deplacement_roi = ("Le Roi", "8/8/8/3kK3/8/8/8/8 w KQkq - 0 1")
    deplacement_dame = ("La Dame", "8/8/8/3qQ3/8/8/8/8 w KQkq - 0 1")
    deplacement_pion = ("Le Pion", "8/PPp2ppp/3p4/4p3/8/3P4/PPPpPPpp/8 w "
                                   "KQkq - 0 1")
    mat_2_coups = [("Quotidien", "8/4K1kp/6NN/6B1/8/8/8/8 w - 0 0")]
    return [normal, prise_en_passant, rocque, pion_upgrade, deplacment_tour,
            deplacement_fou, deplacement_cheval, deplacement_roi,
            deplacement_dame, deplacement_pion, mat_2_coups]


def set_joueur(option, init, gameplay, plateau, param):
    """
    Permet de créer des set d ejoueurs
    :param option: str
    :param init: int
    :param gameplay: liste
    :param plateau: liste
    :param param: liste
    :return: tuple

    >>> set_joueur(1, "", 0, [("Le Roi", "8/8/8/4K3/8/8/8/8 w KQkq - 0 1")], \
    ["j1", "B", "B", "J2"])
    ([['R', (3, 4)]], [], 'Le Roi')
    """

    # On joue en replay on doit charger le jeu pour le consulter  on
    # ne prends pas les autres options
    gameplay_name = ""
    if option == 2:
        jb, jn = position_initiale(plateau[0][1], param)
        gameplay_name = plateau[0][0]
    else:
        # On regarde si on doit charger un jeu
        if init != "":
            filin = open(init + ".jeu", "r")
            chaine_a_construire = filin.readline()
            jb, jn = position_initiale(chaine_a_construire, param)
            filin.close()
        # On a selectionner un jeu
        elif gameplay >= 0:
            # Cas particulier du mat en 2 coups on choisi
            # aléatoirement un jeu
            if gameplay == 10:
                num_jeu = 0
                jb, jn = position_initiale(plateau[gameplay][num_jeu][1],
                                           param)
                gameplay_name = plateau[gameplay][num_jeu][0]
            # On charge le jeu
            else:
                jb, jn = position_initiale(plateau[gameplay][1], param)
                gameplay_name = plateau[gameplay][0]
        # Si on n a pas selectionne de jeu alors on charge le standard
        else:
            jb, jn = position_initiale(plateau[0][1], param)
            gameplay_name = plateau[0][0]
    return jb, jn, gameplay_name


###########################################
#  Fonctions Gestion des joueurs          #
###########################################
def inverse_plateau(j1, j2):
    """
    permet de changer le sens du plateau
    :param j1: liste
    :param j2: liste
    :return: tuple de liste

    >>> inverse_plateau([['R', (2, 0)], ['D', (2, 1)]], [['R', (0, 0)], \
    ['D', (0, 1)]])
    ([['R', (5, 7)], ['D', (5, 6)]], [['R', (7, 7)], ['D', (7, 6)]])
    """
    inv_j1 = []
    inv_j2 = []
    for j in j1:
        inv_j1.append([j[0], (abs(j[1][0] - 7), abs(j[1][1] - 7))])
    for j in j2:
        inv_j2.append([j[0], (abs(j[1][0] - 7), abs(j[1][1] - 7))])
    return inv_j1, inv_j2


def score(j1, j2):
    """
    Permet de stocker les score des pieces
    :param j1: liste
    :param j2: liste
    :return: int, int

    >>> score([['P', (2, 0)], ['D', (2, 1)]], [['T', (0, 0)], ['C', (0, 1)]])
    (10, 9)
    """
    score_j1 = 0
    score_j2 = 0
    for j in j1:
        score_j1 += score_piece(j[0])
    for j in j2:
        score_j2 += score_piece(j[0])
    return score_j1, score_j2


###########################################
#  Fonctions Gestion des pieces           #
###########################################
def score_piece(piece):
    """
    Donne un score aux pieces
    :param piece: str
    :return: int

    >>> score_piece("F")
    3
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


###########################################
#  Fonctions Inversion des mouvements       #
###########################################
def inverse_mouvement(mouvements):
    """
    permet d'inverser  les mouvement
    :param mouvements: liste
    :return: tuple

    >>> inverse_mouvement([0,1])
    (7, 6)
    """
    return abs(mouvements[0] - 7), abs(mouvements[1] - 7)


def inverse_list_mouvement(list_mouvements):
    """
    Permet d'inverser les liste de mouvement
    :param list_mouvements: liste
    :return: liste

    >>> inverse_list_mouvement([(0,7), (4,3)])
    [(7, 0), (3, 4)]
    """
    inv_mouvement = []
    for mvt in list_mouvements:
        inv_mouvement.append(inverse_mouvement(mvt))
    return inv_mouvement


def inverse_groupement_mouvement(replay_jeu_complet):
    """
    Permet d'inverser les mouvement du replay
    :param replay_jeu_complet: liste
    :return: liste
    """
    inv_replay_list = []
    inv_replay_piece = []
    for list_mvt in replay_jeu_complet:
        for piece in list_mvt:
            inv_replay_piece.append((piece[0], inverse_mouvement(piece[1])))
        inv_replay_list.append(inv_replay_piece)
    return inv_replay_list


def is_mouvement_ambigu(pos_x, pos_y, mouvement_piece, mange_mouvement_piece):
    """
    Permet de savoir faire la diff entre 2 piece ambigue
    :param pos_x: int
    :param pos_y: int
    :param mouvement_piece: liste
    :param mange_mouvement_piece: liste
    :return: booléens
    """
    if is_double_place(mouvement_piece, pos_x, pos_y) or \
            is_double_place(mange_mouvement_piece, pos_x, pos_y):
        return True
    else:
        return False


def inverse_tour_bouge():
    temp = tour_bouge[0]
    tour_bouge[0] = tour_bouge[1]
    tour_bouge[1] = temp
    temp = tour_bouge[2]
    tour_bouge[2] = tour_bouge[3]
    tour_bouge[3] = temp


###########################################
#  Fonctions Action sur Plateau           #
###########################################
def check_sortir(pos_x, pos_y):
    """
    Permet de savoir si l'on sort du plateau
    :param pos_x:  int
    :param pos_y:  int
    :return: booléens


    >>> check_sortir(50, 650)
    True
    """
    if 25 < pos_x < 75 and 625 < pos_y < 675:
        return True
    return False


def check_inverse(pos_x, pos_y, nb_case_echec, top_x, top_y,
                  ratio, taille_ecran, taille_jeu, param, list_mvt,
                  list_mvt_mange, joueur_qui_joue, adversaire,
                  replay_jeu_complet, decallage_plateau, id_mvt, sens_jeux,
                  nb_coup_joue, id_joueur):
    """
    Même principe lorsqe on inverse le jeu
    :param pos_x: int
    :param pos_y: int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param ratio: int
    :param taille_ecran:int
    :param taille_jeu: int
    :param param: liste
    :param list_mvt: liste
    :param list_mvt_mange:liste
    :param joueur_qui_joue: liste
    :param adversaire: liste
    :param replay_jeu_complet: str
    :param decallage_plateau: str
    :param id_mvt: int
    :param sens_jeux: str
    :param nb_coup_joue: int
    :param id_joueur: int
    :return: tuple
    """
    if 100 < pos_x < 150 and 625 < pos_y < 675:
        joueur_qui_joue, adversaire = inverse_plateau(joueur_qui_joue,
                                                      adversaire)
        list_mvt_deplacement = inverse_list_mouvement(list_mvt)
        list_mvt_mange = inverse_list_mouvement(list_mvt_mange)
        replay_jeu_complet = inverse_groupement_mouvement(replay_jeu_complet)
        id_mvt *= -1
        sens_jeux *= -1
        inverse_tour_bouge()
        rafraichir_plateau(True, nb_case_echec, top_x, top_y, ratio,
                           taille_ecran, taille_jeu, sens_jeux,
                           joueur_qui_joue, adversaire,
                           list_mvt_deplacement, list_mvt_mange,
                           decallage_plateau, param, nb_coup_joue, id_joueur)
        return (joueur_qui_joue, adversaire, list_mvt_deplacement,
                list_mvt_mange, replay_jeu_complet, param, id_mvt, sens_jeux)
    return (joueur_qui_joue, adversaire, list_mvt, list_mvt_mange,
            replay_jeu_complet, param, id_mvt, sens_jeux)


def check_avance(pos_x, pos_y, idx_partie, nb_case_echec, top_x, top_y, ratio,
                 taille_ecran, taille_jeu, list_mvt_deplacement,
                 list_mvt_mange, joueur_qui_joue, replay_jeu_complet,
                 decallage_plateau, sens_jeux, param, nb_coup_joue, id_joueur,
                 ):
    """
    Permet de vérifier si l'on avance
    :param pos_x: int
    :param pos_y: int
    :param idx_partie:int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param ratio: int
    :param taille_ecran:int
    :param taille_jeu: int
    :param list_mvt_deplacement:liste
    :param list_mvt_mange: liste
    :param joueur_qui_joue: liste
    :param replay_jeu_complet: liste
    :param decallage_plateau: str
    :param sens_jeux: str
    :param param: liste
    :param nb_coup_joue: int
    :param id_joueur: int
    :return: liste
    """
    joueur = joueur_qui_joue
    if 515 < pos_x < 565 and 625 < pos_y < 675:
        nb_coup_partie = len(replay_jeu_complet)
        idx_partie += 1
        if idx_partie < nb_coup_partie:
            adversaire = replay_jeu_complet[idx_partie]
            rafraichir_plateau(False, nb_case_echec, top_x, top_y, ratio,
                               taille_ecran, taille_jeu, sens_jeux,
                               joueur_qui_joue, adversaire,
                               list_mvt_deplacement, list_mvt_mange,
                               decallage_plateau, param,
                               nb_coup_joue, id_joueur)
            return adversaire, idx_partie, nb_coup_joue
        else:
            idx_partie -= 1
        nb_coup_joue += 1
    return joueur, idx_partie, nb_coup_joue


def check_recul(pos_x, pos_y, idx_partie, nb_case_echec, top_x, top_y, ratio,
                taille_ecran, taille_jeu, list_mvt_deplacement,
                list_mvt_mange, joueur_qui_joue, adversaire,
                replay_jeu_complet, decallage_plateau, sens_jeux, param,
                nb_coup_joue, id_joueur):
    """
    Permet de voir si on recule
    :param pos_x: int
    :param pos_y: int
    :param idx_partie:int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param ratio: int
    :param taille_ecran:int
    :param taille_jeu: int
    :param list_mvt_deplacement:liste
    :param list_mvt_mange: liste
    :param joueur_qui_joue: liste
    :param adversaire: liste
    :param replay_jeu_complet: liste
    :param decallage_plateau: str
    :param sens_jeux: str
    :param param: liste
    :param nb_coup_joue: int
    :param id_joueur: int
    :return: liste
    """
    joueur = joueur_qui_joue
    if 265 < pos_x < 315 and 625 < pos_y < 675:
        idx_partie -= 2
        if idx_partie > 0:
            joueur = replay_jeu_complet[idx_partie - 2]
            rafraichir_plateau(False, nb_case_echec, top_x, top_y, ratio,
                               taille_ecran, taille_jeu, sens_jeux,
                               joueur_qui_joue, adversaire,
                               list_mvt_deplacement, list_mvt_mange,
                               decallage_plateau, param, nb_coup_joue,
                               id_joueur)
        else:
            idx_partie = idx_partie + 2
        nb_coup_joue -= 1
        return joueur, idx_partie, nb_coup_joue
    return joueur, idx_partie, nb_coup_joue


###########################################
#  Fonctions Action de jeu                #
###########################################
def nouveau_tour(change_joueur, id_joueur, param, joueur_qui_joue, adversaire,
                 id_mvt, nb_coup_joue, nb_case_echec, top_x, top_y, ratio,
                 taille_ecran, taille_jeu, sens_jeux, list_mvt_deplacement,
                 list_mvt_mange, decallage_plateau, prise_passant,
                 is_prise_passant, coupj, coupj1, coupj2):
    """
    Permet de lister un nouv0 joueur
    :param change_joueur: int
    :param id_joueur: int
    :param param: liste
    :param joueur_qui_joue:liste
    :param adversaire: liste
    :param id_mvt: int
    :param nb_coup_joue:int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param ratio: str
    :param taille_ecran:int
    :param taille_jeu: int
    :param sens_jeux: int
    :param list_mvt_deplacement:lste
    :param list_mvt_mange: liste
    :param decallage_plateau: int
    :param prise_passant: int
    :param is_prise_passant: booléen
    :param coupj: int
    :param coupj1: int
    :param coupj2: int
    :return: tuple
    """
    new_joueur_qui_joue = deepcopy(joueur_qui_joue)
    new_adversaire = deepcopy(adversaire)
    rafraichir_plateau(True, nb_case_echec, top_x, top_y, ratio,
                       taille_ecran, taille_jeu, sens_jeux,
                       joueur_qui_joue, adversaire,
                       list_mvt_deplacement, list_mvt_mange,
                       decallage_plateau, param, nb_coup_joue, id_joueur)
    dessine_coup_joueur(nb_case_echec, ratio, coupj)
    if change_joueur:
        # sauvegarde le mvt fait
        if len(coupj2) > 0:
            sauvegarde(nb_coup_joue // 2, coupj2, coupj)
            coupj2 = ""
            coupj1 = coupj
        else:
            coupj2 = coupj
        # savoir quel joueur joue
        if id_joueur == 0:
            id_mvt *= -1
            new_joueur_qui_joue = deepcopy(adversaire)
            new_adversaire = deepcopy(joueur_qui_joue)
            id_joueur = 1
            # attention a la couleur du jouer 1 si il est noir il est
            # consideree comme le joueur 2
            if param[1] == "N":
                dessine_tour_joueur(nb_case_echec, ratio, param[0])
            else:
                dessine_tour_joueur(nb_case_echec, ratio, param[3])
        else:
            id_joueur = 0
            id_mvt *= -1
            new_joueur_qui_joue = deepcopy(adversaire)
            new_adversaire = deepcopy(joueur_qui_joue)
            if param[1] == "B":
                dessine_tour_joueur(nb_case_echec, ratio, param[0])
            else:
                dessine_tour_joueur(nb_case_echec, ratio, param[3])
        change_joueur = False
        nb_coup_joue += 1
        # Je viens d'ajuter une prise en passant, le joueur n'a qu'un tour
        # pour l'utiliser
        if is_prise_passant:
            val, piece = prise_passant
            prise_passant = False, piece
            is_prise_passant = False
        if prise_passant[0]:
            is_prise_passant = True
    return (id_joueur, id_mvt, new_joueur_qui_joue, new_adversaire,
            change_joueur, nb_coup_joue, prise_passant, is_prise_passant,
            coupj1, coupj2)


def check_piece_jeu(pos_x, pos_y, piece, index_pos, nb_case_echec, top_x,
                    top_y, ratio, taille_ecran, taille_jeu,
                    list_mvt_deplacement, list_mvt_mange, id_joueur, id_mvt,
                    prise_passant, joueur_qui_joue, adversaire,
                    decallage_plateau, change_joueur, sens_jeux, param,
                    nb_coup_joue, old_x, old_y):
    """
    Permet de recuperer l'ensemble des mvt du joueur
    :param pos_x: int
    :param pos_y:int
    :param piece:int
    :param index_pos:liste
    :param nb_case_echec:int
    :param top_x:int
    :param top_y:int
    :param ratio:str
    :param taille_ecran:int
    :param taille_jeu:int
    :param list_mvt_deplacement:liste
    :param list_mvt_mange:liste
    :param id_joueur:int
    :param id_mvt:int
    :param prise_passant:int
    :param joueur_qui_joue:liste
    :param adversaire:liste
    :param decallage_plateau:str
    :param change_joueur:int
    :param sens_jeux:str
    :param param:liste
    :param nb_coup_joue:int
    :param old_x:int
    :param old_y:int
    :return:tuple
    """
    if check_position_piece(pos_x, pos_y, joueur_qui_joue):
        piece, index_pos = name_piece(pos_x, pos_y, joueur_qui_joue)
        list_mvt_deplacement, list_mvt_mange = \
            deplacement_autorise(piece, pos_x, pos_y, joueur_qui_joue,
                                 adversaire,  id_joueur, id_mvt, index_pos,
                                 prise_passant)
        # On affiche les mouvemement possibles
        rafraichir_plateau(True, nb_case_echec, top_x, top_y, ratio,
                           taille_ecran, taille_jeu, sens_jeux,
                           joueur_qui_joue, adversaire,
                           list_mvt_deplacement, list_mvt_mange,
                           decallage_plateau, param, nb_coup_joue, id_joueur)
        rafraichir_case(True, nb_case_echec, top_x, top_y, ratio,
                        taille_ecran, taille_jeu, list_mvt_deplacement,
                        list_mvt_mange)
        change_joueur = False
        return (list_mvt_deplacement, list_mvt_mange, piece, pos_x, pos_y,
                index_pos, change_joueur)
    return (list_mvt_deplacement, list_mvt_mange, piece, old_x, old_y,
            index_pos, change_joueur)


def check_mouvement_jeu(pos_x, pos_y, piece, old_x, old_y, index_pos,
                        list_mvt_deplacement,
                        list_mvt_mange, id_joueur, id_mvt, prise_passant,
                        joueur_qui_joue, adversaire,
                        change_joueur, sens_jeux, param, coupj):
    """

    Peremt de stocker les mouvements
    :param pos_x: int
    :param pos_y: int
    :param piece: int
    :param old_x: int
    :param old_y: int
    :param index_pos:int
    :param list_mvt_deplacement:liste
    :param list_mvt_mange: liste
    :param id_joueur: int
    :param id_mvt: int
    :param prise_passant:booléen
    :param joueur_qui_joue: liste
    :param adversaire: liste
    :param change_joueur: booleens
    :param sens_jeux: int
    :param param: liste
    :param coupj:int
    :return: tuple
    """
    decision = ""
    ambiguite = False
    if check_position_mouvement(pos_x, pos_y, list_mvt_deplacement):
        if piece == "T" or piece == "C" or piece == "F":
            bouge_tour_roque(piece, old_x, old_y, param, sens_jeux)
            idx_autre_piece = autre_piece(piece, index_pos, joueur_qui_joue)
            if idx_autre_piece >= 0:
                # On doit regarder l'ensemble des positions possibles
                # mais pas celle qui mange car elles ne sont pas
                # dans la liste mvt_possible
                mouvement_piece_double, mange_mouvement_piece_double = \
                    deplacement_autorise(piece,
                                         joueur_qui_joue[idx_autre_piece]
                                         [1][0],
                                         joueur_qui_joue[idx_autre_piece]
                                         [1][1],
                                         joueur_qui_joue, adversaire,
                                         id_joueur, id_mvt, index_pos,
                                         prise_passant)
                ambiguite = is_mouvement_ambigu(pos_x, pos_y,
                                                mouvement_piece_double,
                                                mange_mouvement_piece_double)
        joueur_qui_joue[index_pos][1] = (pos_x, pos_y)
        if piece == 'P':
            # pion atteint la ligne ennemi et peux se transformer
            if pos_x == 0 or pos_x == 7:
                choix = chgmt_pion(joueur_qui_joue)
                decision = dessine_piece_choisit(choix, "B")
                joueur_qui_joue = transforme_pion(joueur_qui_joue, index_pos,
                                                  decision)
            if abs(pos_x - old_x) > 1:
                prise_passant = 'True', [['P', (pos_x, pos_y)]]
        if piece == 'R':
            if id_joueur == 0:
                roi_bouge[0] = True
            else:
                roi_bouge[1] = True
            # Il s'agit d'un petit Roque
            if abs(old_y - pos_y) > 1 and pos_y > old_y:
                _, index_pos = name_piece(old_x, 7, joueur_qui_joue)
                joueur_qui_joue[index_pos][1] = (old_x, old_y + 1)
            # Il s'agit d'un grand rocque
            if abs(old_y - pos_y > 1) and pos_y < old_y:
                _, index_pos = name_piece(old_x, 0, joueur_qui_joue)
                joueur_qui_joue[index_pos][1] = (old_x, old_y - 1)
        coupj = sauv_deplacement(piece, old_y, pos_x, pos_y, "",
                                 ambiguite, decision)
        list_mvt_deplacement = []
        list_mvt_mange = []
        change_joueur = True
    return (coupj, prise_passant, change_joueur, list_mvt_deplacement,
            list_mvt_mange, coupj)


def bouge_tour_roque(piece, old_x, old_y, param, sens_jeux):
    """
    Peremt de verifier si la tour a bouger pour le roque
    :param piece: str
    :param old_x: int
    :param old_y: int
    :param param: liste
    :param sens_jeux: int
    :return: booléen
    """
    if piece == "T":
        if (param[1] == "B" and param[2] == -1) or \
                (param[1] == "N" and param[2] == 1):
            blanc_bas = False
        else:
            blanc_bas = True
        if sens_jeux == -1:
            blanc_bas = not blanc_bas
        if (old_x, old_y) == (0, 0):
            if blanc_bas:
                tour_bouge[3] = True
            else:
                tour_bouge[1] = True
        elif (old_x, old_y) == (0, 7):
            if blanc_bas:
                tour_bouge[2] = True
            else:
                tour_bouge[0] = True
        elif (old_x, old_y) == (7, 7):
            if blanc_bas:
                tour_bouge[2] = True
            else:
                tour_bouge[0] = True
        elif (old_x, old_y) == (7, 0):
            if blanc_bas:
                tour_bouge[3] = True
            else:
                tour_bouge[1] = True


def check_mouvement_mange_jeu(pos_x, pos_y, piece, old_x, old_y, index_pos,
                              list_mvt_deplacement,
                              list_mvt_mange, id_joueur, id_mvt, prise_passant,
                              joueur_qui_joue, adversaire,
                              change_joueur, sens_jeux, param, coupj):
    """
    Permet de verifier la perte de piece mange
    :param pos_x: int
    :param pos_y: int
    :param piece: int
    :param old_x: int
    :param old_y: int
    :param index_pos:int
    :param list_mvt_deplacement:liste
    :param list_mvt_mange: liste
    :param id_joueur: int
    :param id_mvt: int
    :param prise_passant:liste
    :param joueur_qui_joue: liste
    :param adversaire: liste
    :param change_joueur: int
    :param sens_jeux: int
    :param param: liste
    :param coupj: int
    :return: tuple
    """
    decision = ""
    ambiguite = False
    if check_position_mouvement(pos_x, pos_y, list_mvt_mange):
        joueur_qui_joue[index_pos][1] = (pos_x, pos_y)
        # Coup prise en passant
        if prise_passant[0] and pos_x == int(
                            prise_passant[1][0][1][0]) + 1 * id_mvt and \
                pos_y == prise_passant[1][0][1][1]:
            piecem, index_piece_manger = \
                            name_piece(prise_passant[1][0][1][0],
                                       prise_passant[1][0][1][1], adversaire)
            coupj = sauv_deplacement(piece, old_y, old_x, pos_y, "x",
                                     ambiguite, "")
        else:
            if piece == "T" or piece == "C" or piece == "F":
                bouge_tour_roque(piece, old_x, old_y, param, sens_jeux)
                index_autre_piece = autre_piece(piece, index_pos,
                                                joueur_qui_joue)
                if index_autre_piece >= 0:
                    # On doit regarder l'ensemble des positions possibles
                    piece_x = joueur_qui_joue[index_autre_piece][1][0]
                    piece_y = joueur_qui_joue[index_autre_piece][1][1]
                    mouvement_piece_double, mange_mouvement_piece_double = \
                        deplacement_autorise(piece, piece_x, piece_y,
                                             joueur_qui_joue, adversaire,
                                             id_joueur, id_mvt, index_pos,
                                             prise_passant)
                    ambiguite = \
                        is_mouvement_ambigu(pos_x, pos_y,
                                            mouvement_piece_double,
                                            mange_mouvement_piece_double)

            if piece == 'R':
                if id_joueur == 0:
                    roi_bouge[0] = True
                else:
                    roi_bouge[1] = True
            # pion atteint la ligne ennemi et peux setransformer
            # tout en mangeant
            if (pos_x == 0 or pos_x == 7) and piece == "P":
                choix = chgmt_pion(joueur_qui_joue)
                decision = dessine_piece_choisit(choix, 'B')
                joueur_qui_joue = transforme_pion(joueur_qui_joue,
                                                  index_pos,
                                                  decision)
            coupj = sauv_deplacement(piece, old_y, pos_x, pos_y, "x",
                                     ambiguite, decision)
            piecem, index_piece_manger = name_piece(pos_x,
                                                    pos_y,
                                                    adversaire)
        if index_piece_manger > 0:
            adversaire.pop(index_piece_manger)
        list_mvt_deplacement = []
        list_mvt_mange = []
        change_joueur = True
    return (coupj, joueur_qui_joue, adversaire, change_joueur,
            list_mvt_deplacement, list_mvt_mange, coupj)


def check_echec(id_joueur, id_mvt, prise_passant, joueur_qui_joue, adversaire):
    """
    Permet de verifier si il y a echec
    :param id_joueur: v
    :param id_mvt: int
    :param prise_passant:liste
    :param joueur_qui_joue: liste
    :param adversaire: liste
    :return: booléen
    """
    trouve_roi, index_roi = cherche_roi(joueur_qui_joue)
    if trouve_roi:
        is_echec = echec(joueur_qui_joue[index_roi][1][0], joueur_qui_joue[
                         index_roi][1][1], adversaire, joueur_qui_joue,
                         id_joueur, id_mvt, prise_passant, True)
        if len(is_echec) > 0:
            return True
    return False


def check_mat(joueur_qui_joue, adversaire, id_joueur, id_mvt, prise_passant):
    """
    Permet de verifier si il y a mat
    :param joueur_qui_joue: liste
    :param adversaire: liste
    :param id_joueur: int
    :param id_mvt: int
    :param prise_passant:liste
    :return: booléens
    """
    trouve_roi, index_roi = cherche_roi(joueur_qui_joue)
    if trouve_roi:
        if mat(joueur_qui_joue, adversaire, id_joueur, id_mvt, prise_passant):
            print("echec et MAT!!")
            return True
    return False


def joue(param, jb, jn, nb_case_echec, taille_ecran, taille_jeu,
         decallage_plateau, replay_jeu_complet, sens_jeux):
    """
    Permet de jouer
    :param param: int
    :param jb: liste
    :param jn: liste
    :param nb_case_echec:int
    :param taille_ecran: int
    :param taille_jeu: int
    :param decallage_plateau:int
    :param replay_jeu_complet: int
    :param sens_jeux: int
    :return: none
    """
    # initialisation des variables
    ratio = taille_jeu // nb_case_echec
    top_x = taille_ecran - decallage_plateau - taille_jeu
    top_y = (taille_ecran - taille_jeu) // 2
    prise_passant = 'False', [['P', (0, 0)]]
    list_mvt_deplacement = []
    list_mvt_mange = []
    joueur_qui_joue = deepcopy(jb)
    adversaire = deepcopy(jn)
    jouer = True
    gain = []
    piece = ""
    index_pos = 0
    nouveau_round = False
    idx_partie = 1
    id_joueur = 0
    id_mvt = int(param[2] * -1)
    nb_coup_joue = 0
    is_prise_en_passant = False
    old_x = 0
    old_y = 0
    coupj = ""
    coupj1 = ""
    coupj2 = ""
    joueur_gagnant = -1
    # creation du fichier txt
    if param[1] == "B":
        init_sauvegarde("Projet Chess", "MLV", 1, param[0], param[3], "Human",
                        "Human")
    else:
        init_sauvegarde("Projet Chess", "MLV", 1, param[3], param[0], "Human",
                        "Human")
    while jouer:
        # A chaque tour on inverse le joueur
        (id_joueur, id_mvt, joueur_qui_joue, adversaire, nouveau_round,
         nb_coup_joue, prise_passant, is_prise_en_passant, coupj1, coupj2,) = \
            nouveau_tour(nouveau_round, id_joueur, param, joueur_qui_joue,
                         adversaire, id_mvt, nb_coup_joue, nb_case_echec,
                         top_x, top_y, ratio, taille_ecran, taille_jeu,
                         sens_jeux, list_mvt_deplacement,
                         list_mvt_mange, decallage_plateau, prise_passant,
                         is_prise_en_passant, coupj, coupj1, coupj2)

        if pat(joueur_qui_joue, adversaire, id_joueur, id_mvt,
               prise_passant):
            print("PAT !!!")
            gain = "PAT"
            dessine_echec_joueur(nb_case_echec, ratio, "PAT")
            attend_clic_gauche()
            jouer = False
        else:
            # A chaque tour on vérifie qu'il n'y a pas MAT
            if check_echec(id_joueur, id_mvt, prise_passant, joueur_qui_joue,
                           adversaire):
                print("ECHEC")
                dessine_echec_joueur(nb_case_echec, ratio, "ECHEC !!")
                attend_clic_gauche()
                coupj += "+"
            if check_mat(joueur_qui_joue, adversaire, id_joueur, id_mvt,
                         prise_passant):
                gain = "MAT"
                joueur_gagnant = id_joueur
                coupj += "#"
                dessine_echec_joueur(nb_case_echec, ratio, "MAT")
                attend_clic_gauche()
                jouer = False
            else:
                dessine_echec_joueur(nb_case_echec, ratio, " ")
                # On attend l'action qui consite à cliqer sur une piece et la
                # déplacer
                attend_clic_gauche()
                # On recupère la piece sur laquelle on a clique, on vérifie
                # quelle est dans le jeu
                pos_y, pos_x = pixel_vers_case(top_x, top_y, abscisse_souris(),
                                               ordonnee_souris(), ratio)
                # A chaque tour on vérifie qu'il ne veut pas sortir
                if check_sortir(abscisse_souris(), ordonnee_souris()):
                    jouer = False
                else:
                    # debut des actions du jeu
                    (list_mvt_deplacement, list_mvt_mange, piece, old_x, old_y,
                     index_pos, nouveau_round) = \
                        check_piece_jeu(pos_x, pos_y, piece, index_pos,
                                        nb_case_echec,
                                        top_x, top_y, ratio, taille_ecran,
                                        taille_jeu,
                                        list_mvt_deplacement, list_mvt_mange,
                                        id_joueur, id_mvt, prise_passant,
                                        joueur_qui_joue, adversaire,
                                        decallage_plateau, nouveau_round,
                                        sens_jeux,
                                        param, nb_coup_joue, old_x, old_y)
                    # On regarde si on a cliquer sur un mouvement sans manger
                    (coupj, prise_passant, nouveau_round,
                     list_mvt_deplacement, list_mvt_mange, coupj) = \
                        check_mouvement_jeu(pos_x, pos_y, piece, old_x, old_y,
                                            index_pos, list_mvt_deplacement,
                                            list_mvt_mange, id_joueur, id_mvt,
                                            prise_passant, joueur_qui_joue,
                                            adversaire, nouveau_round,
                                            sens_jeux, param, coupj)
                    # On regarde si on a cliquer sur un mouvement en mangeant
                    (coupj, joueur_qui_joue, adversaire, nouveau_round,
                     list_mvt_deplacement, list_mvt_mange, coupj) = \
                        check_mouvement_mange_jeu(pos_x, pos_y, piece, old_x,
                                                  old_y,
                                                  index_pos,
                                                  list_mvt_deplacement,
                                                  list_mvt_mange, id_joueur,
                                                  id_mvt,
                                                  prise_passant,
                                                  joueur_qui_joue,
                                                  adversaire, nouveau_round,
                                                  sens_jeux,
                                                  param, coupj)
                    # Gestion de l'avance de la partie (chargé ou en cours)
                    # si clique
                    joueur_qui_joue, idx_partie, nb_coup_joue = \
                        check_avance(abscisse_souris(), ordonnee_souris(),
                                     idx_partie,
                                     nb_case_echec, top_x, top_y, ratio,
                                     taille_ecran,
                                     taille_jeu, list_mvt_deplacement,
                                     list_mvt_mange, joueur_qui_joue,
                                     replay_jeu_complet, decallage_plateau,
                                     sens_jeux,
                                     param, nb_coup_joue, id_joueur)
                    # Gestion du recul de la partie (chargé ou en cours)
                    # si clique
                    joueur_qui_joue, idx_partie, nb_coup_joue = \
                        check_recul(abscisse_souris(), ordonnee_souris(),
                                    idx_partie,
                                    nb_case_echec, top_x, top_y, ratio,
                                    taille_ecran,
                                    taille_jeu, list_mvt_deplacement,
                                    list_mvt_mange, joueur_qui_joue,
                                    adversaire,
                                    replay_jeu_complet, decallage_plateau,
                                    sens_jeux,
                                    param, nb_coup_joue, id_joueur)
                    # Gestion de l'inversion de plateau en cours de jeu
                    # si clique
                    (joueur_qui_joue, adversaire, list_mvt_deplacement,
                     list_mvt_mange,
                     replay_jeu_complet, param, id_mvt, sens_jeux) = \
                        check_inverse(abscisse_souris(),
                                      ordonnee_souris(), nb_case_echec, top_x,
                                      top_y,
                                      ratio, taille_ecran, taille_jeu, param,
                                      list_mvt_deplacement, list_mvt_mange,
                                      joueur_qui_joue, adversaire,
                                      replay_jeu_complet, decallage_plateau,
                                      id_mvt,
                                      sens_jeux, nb_coup_joue, id_joueur)
    if gain == "PAT":
        fin_jeu("1-1")
    elif joueur_gagnant == 0:
        fin_jeu("1-0")
    elif joueur_gagnant == 1:
        fin_jeu("0-1")
    else:
        fin_jeu("1-1")
    print("Merci à bientot")


###########################################
#  Fonctions Action de jeu                #
###########################################
def check_action_replay(pos_x, pos_y, ratio, taille_ecran, taille_jeu,
                        replay_jeu_complet, decallage_plateau, nb_coup_joue,
                        nb_case_echec, top_x, top_y, sens_jeux, param,
                        id_joueur, partie_coord):
    """
    Replay
    :param pos_x: int
    :param pos_y: int
    :param ratio: int
    :param taille_ecran:int
    :param taille_jeu: int
    :param replay_jeu_complet:int
    :param decallage_plateau: int
    :param nb_coup_joue: int
    :param nb_case_echec: int
    :param top_x: int
    :param top_y: int
    :param sens_jeux:int
    :param param: int
    :param id_joueur:int
    :param partie_coord:int
    :return: tuple
    """
    nb_coup_partie = len(replay_jeu_complet)
    joueur = []
    adversaire = []
    sortie = check_sortir(pos_x, pos_y)
    if not sortie:
        if 515 < pos_x < 565 and 625 < pos_y < 675:
            nb_coup_joue += 2
            if 0 < nb_coup_joue < nb_coup_partie:
                joueur = replay_jeu_complet[nb_coup_joue]
                adversaire = replay_jeu_complet[nb_coup_joue + 1]
                id_joueur = inverse_id_joueur(id_joueur)
            else:
                nb_coup_joue -= 2
        elif 265 < pos_x < 315 and 625 < pos_y < 675:
            nb_coup_joue -= 2
            if 0 < nb_coup_joue < nb_coup_partie:
                joueur = replay_jeu_complet[nb_coup_joue]
                adversaire = replay_jeu_complet[nb_coup_joue + 1]
                id_joueur = inverse_id_joueur(id_joueur)
            else:
                nb_coup_joue = 0
        else:
            return nb_coup_joue, id_joueur, not sortie
        if id_joueur == 0 and param[1] == "B":
            rafraichir_plateau(False, nb_case_echec, top_x, top_y, ratio,
                               taille_ecran, taille_jeu, sens_jeux,
                               joueur, adversaire,
                               [], [], decallage_plateau, param,
                               nb_coup_joue, id_joueur)
        else:
            rafraichir_plateau(False, nb_case_echec, top_x, top_y, ratio,
                               taille_ecran, taille_jeu, sens_jeux,
                               adversaire, joueur,
                               [], [], decallage_plateau, param,
                               nb_coup_joue, id_joueur)
        idx_mouv = (nb_coup_joue - 2) // 2
        if idx_mouv >= len(partie_coord):
            idx_mouv = len(partie_coord) - 1
        mouv = partie_coord[idx_mouv]
        dessine_coup_joueur(nb_case_echec, ratio,  mouv)
    return nb_coup_joue, id_joueur, not sortie


def joue_replay(nb_case_echec,  taille_ecran,
                taille_jeu, decallage_plateau, replay_jeu_complet,
                param, sens_jeux, partie_coord):
    """
    Permet de jouer le replay
    :param nb_case_echec: int
    :param taille_ecran: int
    :param taille_jeu: int
    :param decallage_plateau:int
    :param replay_jeu_complet: int
    :param param: int
    :param sens_jeux:int
    :param partie_coord:int
    :return: booléen
    """
    ratio = taille_jeu // nb_case_echec
    top_x = taille_ecran - decallage_plateau - taille_jeu
    top_y = (taille_ecran - taille_jeu) // 2
    nb_coup_joue = 0
    id_joueur = 0
    # Gestion de l'avance de la partie (chargé ou en cours)
    rafraichir_plateau(False, nb_case_echec, top_x, top_y, ratio,
                       taille_ecran, taille_jeu, sens_jeux,
                       replay_jeu_complet[0], replay_jeu_complet[1],
                       [], [], decallage_plateau, param,
                       nb_coup_joue, id_joueur)
    # si clique
    jouer = True
    while jouer:
        attend_clic_gauche()
        nb_coup_joue, id_joueur, jouer = \
            check_action_replay(abscisse_souris(), ordonnee_souris(),
                                ratio, taille_ecran, taille_jeu,
                                replay_jeu_complet, decallage_plateau,
                                nb_coup_joue,
                                nb_case_echec, top_x, top_y, sens_jeux, param,
                                id_joueur, partie_coord)
        if nb_coup_joue > len(replay_jeu_complet):
            jouer = False


def main():
    plateau = init_plateau()
    nb_case_echec = 8
    taille_ecran = 700
    taille_jeu = 500
    decallage_plateau = 30
    rayon_selection = 50
    # Configuration Blanc en Bas
    param = ["Joueur1", "B", -1, "Joueur2"]
    cree_fenetre(taille_ecran, taille_ecran)
    affiche_ouverture(taille_ecran, "chess.png")
    menu = 0
    file_replay = ""
    init = ""
    gameplay_name = "Standard"
    option = 0
    gameplay = -1
    joueur_blanc = []
    joueur_noir = []
    replay_jeu_complet = []
    partie_coord = []
    action_replay = False
    action_apprentissage = False
    while menu < 3:
        efface_tout()
        menu = affiche_accueil(taille_ecran, rayon_selection)
        efface_tout()
        if menu == 1:
            option = affiche_param(taille_ecran, rayon_selection)
            if option == 1:
                param = affiche_param_joueur(taille_ecran, rayon_selection,
                                             param)
            elif option == 2:
                file_replay = affiche_param_replay(taille_ecran,
                                                   rayon_selection)
                action_apprentissage = False
            elif option == 3:
                init, gameplay = affiche_param_init(taille_ecran,
                                                    rayon_selection)
                file_replay = ""
                action_apprentissage = True
        # On joue
        elif menu == 2:
            if (param[1] == "B" and param[2] == -1) or \
                    (param[1] == "N" and param[2] == 1):
                sens_jeux = 1
            else:
                sens_jeux = -1
            if file_replay == "":
                joueur_blanc, joueur_noir, gameplay_name = \
                    set_joueur(option, init, gameplay, plateau, param)
                replay_jeu_complet.append(joueur_blanc)
                replay_jeu_complet.append(joueur_noir)
                action_replay = False
            elif len(file_replay) > 0:
                replay_jeu_complet, gameplay_name, nom_blanc, nom_noir,\
                    partie_coord = replay(file_replay + ".txt")
                param[0] = nom_blanc
                param[1] = "B"
                param[2] = -1
                param[3] = nom_noir
                joueur_blanc, joueur_noir = position_initiale(plateau[0][1],
                                                              param)
                replay_jeu_complet.insert(0, joueur_noir)
                replay_jeu_complet.insert(0, joueur_blanc)
                action_replay = True
            if action_replay:
                # On affiche le plateau avec les bon paramètre
                dessine_jeu(taille_ecran, taille_jeu, decallage_plateau,
                            nb_case_echec, gameplay_name, action_replay,
                            action_apprentissage)
                joue_replay(nb_case_echec, taille_ecran, taille_jeu,
                            decallage_plateau, replay_jeu_complet, param, -1,
                            partie_coord)
                menu = 1
            else:
                action_replay = False
                # On affiche le plateau avec les bon paramètre
                dessine_jeu(taille_ecran, taille_jeu, decallage_plateau,
                            nb_case_echec, gameplay_name, action_replay,
                            action_apprentissage)
                # On lance le jeu
                joue(param, joueur_blanc, joueur_noir, nb_case_echec,
                     taille_ecran,
                     taille_jeu, decallage_plateau, replay_jeu_complet,
                     sens_jeux)
                menu = 1
    generique(taille_ecran)
    ferme_fenetre()


if __name__ == '__main__':
    main()
