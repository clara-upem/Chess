__authors__ = ("Clara Correia", "Laurie Behloul")
__contact__ = ("clara.correia.sne@gmail.com", "lauriebehloul1@gmail.com")
__version__ = "1.0.0"
__date__ = "2020"

from datetime import datetime
from copy import deepcopy


roi_bouge = [False, False]
tour_bouge = [False, False, False, False]
pion_bouge = False


###########################################
#  Gestion de l'affichage txt             #
###########################################
def affiche_set(j1, j2, mvt_possible, mvt_mange):
    """
    Permet d'afficher les bordures du plateau (en print)
    Provisoire
    :param j1:list,tableau des pieces du joueur 1
    :param j2:list, tableau des pieces du noueur 2
    :param mvt_possible:list, tableau des mouvement possibles
    :param mvt_mange:list, tableau des pieces a mange possibles
    :return:print
    """
    print('   H0   G1   F2   E3   D4   C5   B6    A7')
    print(' _________________________________________')
    plateau = []
    for i in range(8):
        plateau.append(['1'] * 8)
    for i in range(8):
        print(f"{i}", end='')
        for j in range(8):
            print("!", end='')
            draw_pieces = read_place(i, j, j1, j2, mvt_possible, mvt_mange)
            plateau[i][j] = draw_pieces
            print(draw_pieces, end='')
        print('!')
        print(' _______________________________________ ')
    print(' _________________________________________')
    print('   H0   G1   F2   E3   D4   C5   B6    A7')


def read_place(x, y, j1, j2, mvt_possible, mvt_mange):
    """
    Permet de savoir le nom de la pieces sur la case(x, y)
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param j1:list, tableau des pieces du joueur 1
    :param j2:list, tableau des pieces du noueur 2
    :param mvt_possible:list, tableau des mouvement possibles
    :param mvt_mange:list, tableau des pieces a mange possibles
    :return:le texte de la pieces

    >>> read_place(1,1,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],\
    [['OO', (0, 0)]])
    ' P1 '

    >>> read_place(1,0,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],\
    [['OO', (0, 0)]])
    ' P2 '

    >>> read_place(0,1,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],\
    [['OO', (0, 0)]])
    ' XX '

    >>> read_place(0,0,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],\
    [['OO', (0, 0)]])
    ' OO '
        """
    case = '    '
    jouer = False
    for e in j1:
        if e[1] == (x, y):
            case = ' ' + e[0] + '1 '
            jouer = True
            break
    if not jouer:
        for e in j2:
            if e[1] == (x, y):
                case = ' ' + e[0] + '2 '
                break
    for e in mvt_possible:
        if e[1] == (x, y):
            case = ' ' + e[0] + ' '
    for e in mvt_mange:
        if e[1] == (x, y):
            case = ' ' + e[0] + ' '
    return case


def demande_case(texte):
    """
    Permet de selectionner une case version sans plateau
    :param texte:str
    :return:str, coo de la piece
    """
    saisie = False
    if texte != "-1-1":
        while not saisie:  # On tourne jusqu'à avoir une mise entiere
            try:  # On s'assure que la mise est un entier
                valeur_saisie = input(texte)
                to_int = int(valeur_saisie)
                to_int += 0
                return valeur_saisie
            except ValueError:
                print("Merci de saisir un entier ")
                saisie = False
    else:
        return -1


def creer_set(version):
    """
    Permet de generer differente situations de plateau
    :param version: int, represente different plateau
    :return: un plateau

    >>> creer_set(3)
    ([['P', (1, 0)]], [['P', (2, 1)], ['P', (2, 2)]], [])
    """
    j1 = []
    j2 = []
    if version == 1:
        j1 = [['P', (1, 0)], ['P', (1, 1)], ['P', (1, 2)], ['P', (1, 3)],
              ['P', (1, 4)], ['P', (1, 5)], ['P', (1, 6)], ['P', (1, 7)],
              ['T', (0, 0)], ['T', (0, 7)], ['C', (0, 1)], ['C', (0, 6)],
              ['F', (0, 2)], ['F', (0, 5)], ['R', (0, 3)], ['D', (0, 4)]]
        j2 = [['P', (6, 0)], ['P', (6, 1)], ['P', (6, 2)], ['P', (6, 3)],
              ['P', (6, 4)], ['P', (6, 5)], ['P', (6, 6)], ['P', (6, 7)],
              ['T', (7, 0)], ['T', (7, 7)], ['C', (7, 1)], ['C', (7, 6)],
              ['F', (7, 2)], ['F', (7, 5)], ['R', (7, 3)], ['D', (7, 4)]]
    elif version == 2:
        # Jeux prepare rocque
        j2 = [['P', (6, 0)], ['P', (6, 1)], ['P', (6, 2)], ['P', (4, 4)],
              ['P', (6, 5)], ['P', (6, 6)], ['P', (6, 7)], ['T', (7, 0)],
              ['T', (7, 7)], ['C', (5, 2)], ['C', (5, 5)], ['F', (7, 2)],
              ['F', (7, 5)], ['R', (7, 3)], ['D', (7, 4)]]
        j1 = [['P', (1, 0)], ['P', (1, 1)], ['P', (1, 2)], ['P', (1, 4)],
              ['P', (1, 5)], ['P', (1, 6)], ['P', (1, 7)], ['T', (0, 0)],
              ['T', (0, 7)], ['C', (2, 5)], ['C', (0, 6)], ['F', (2, 4)],
              ['F', (0, 5)], ['R', (0, 3)], ['D', (2, 2)]]
    elif version == 3:
        # Mange pion bordure
        j2 = [['P', (2, 1)], ['P', (2, 2)]]
        j1 = [['P', (1, 0)]]
    elif version == 4:
        # Mange pion
        j2 = [['P', (2, 0)], ['P', (2, 2)]]
        j1 = [['P', (6, 1)]]
    elif version == 5:
        # Prise en passant
        j1 = [['P', (1, 2)]]
        j2 = [['P', (3, 3)], ['P', (5, 2)]]
    elif version == 6:
        # Petit Rocque
        j1 = [['R', (0, 3)], ['T', (0, 0)]]
        j2 = [['P', (2, 3)], ['P', (5, 2)]]
    elif version == 7:
        # Grand Rocque
        j2 = [['R', (7, 3)], ['T', (7, 7)]]
        j1 = [['P', (2, 3)], ['P', (5, 2)]]
    elif version == 8:
        # Version Anglaise
        j1 = [['P', (1, 0)], ['P', (1, 1)], ['P', (1, 2)], ['P', (1, 3)],
              ['P', (1, 4)], ['P', (1, 5)], ['P', (1, 6)], ['P', (1, 7)],
              ['R', (0, 0)], ['R', (0, 7)], ['N', (0, 1)], ['N', (0, 6)],
              ['B', (0, 2)], ['B', (0, 5)], ['K', (0, 3)], ['Q', (0, 4)]]
        j2 = [['P', (6, 0)], ['P', (6, 1)], ['P', (6, 2)], ['P', (6, 3)],
              ['P', (6, 4)], ['P', (6, 5)], ['P', (6, 6)], ['P', (6, 7)],
              ['R', (7, 0)], ['R', (7, 7)], ['N', (7, 1)], ['N', (7, 6)],
              ['B', (7, 2)], ['B', (7, 5)], ['K', (7, 3)], ['Q', (7, 4)]]
    elif version == 9:
        # PAT
        j1 = [['F', (5, 3)], ['P', (4, 6)], ['D', (5, 7)], ['R', (0, 0)]]
        j2 = [['R', (7, 6)]]
        roi_bouge[0] = True
        roi_bouge[1] = True
    return j1, j2, []


###########################################
#  Gestion de recherche d'elements        #
###########################################
def name_piece(x, y, joueur):
    """
    Permet de savoir quel pieces est dans la case
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :return:tuple, nom de la pieces et son index dans le tableau du joueur

    >>> name_piece(0,0,[['R', (0, 3)], ['T', (0, 0)]])
    ('T', 1)
    """
    i = 0
    for e in joueur:
        if e[1] == (x, y):
            return e[0], i
        i += 1
    return 'X', -1


def cherche_piece(piece, joueur):
    """
       Permet de trouver l index d'une piece
       :param piece: list
       :param joueur: list
       :return: int
       """
    index_find = 0
    list_resultat = []
    for e in joueur:
        if e[0] == piece:
            list_resultat.append(index_find)
        index_find += 1
    if len(list_resultat) > 0:
        return True, list_resultat
    else:
        return False, -1


def cherche_roi(joueur):
    """
    Permet de trouver l index du roi
    :param joueur: list
    :return: int
    """
    index_r = 0
    for e in joueur:
        if e[0] == "R":
            return True, index_r
        index_r += 1
    return False, -1


def check_position_piece(x, y, joueur):
    """
    Permet de verifier si une piece est dans le set
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :return:True si il y a une pieces et False si il n'y en a pas

    >>> check_position_piece(1,1,[['P', (1, 0)]])
    False

    >>> check_position_piece(1, 0, [['P', (1, 0)]])
    True
    """
    for e in joueur:
        if e[1] == (x, y):
            return True
    return False


def index_position(x, y, joueur):
    """
    Permet de connaitre l'index d'une piece
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :return:True si il y a une pieces et False si il n'y en a pas

    """
    index = 0
    for e in joueur:
        if e[1] == (x, y):
            return index
        index += 1
    return -1


def est_dans_plateau(x, y):
    """
    Permet de verifier si la piece est dans le plateau
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :return:True si la piece est dans le plateau et False sinon

    >>> est_dans_plateau(1,1)
    True

    >>> est_dans_plateau(-1,0)
    False
    """
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False


def autre_piece(piece, index_pos, joueur):
    """
    Permet de trouver l'index (le placement) de l'autre piece du meme genre
    :param piece:
    :param index_pos: int
    :param joueur: list
    :return:
    """
    index = 0
    for e in joueur:
        # si le type de piece ("T" par exemple) correpond a piece
        if e[0] == piece:
            # si les deux index sont differents on retourne l'index
            if index_pos != index:
                return index
        index += 1
    return -1


###########################################
#  Gestion de l'evoluation du pion        #
###########################################
def nombre_occurence(chaine):
    """
    Permet de compter les occurences d'une chaine
    (Creer des index pour les pieces pouvant prendre la place d'un pion)

    :param chaine:
    :return: tuple

    >>> nombre_occurence("DTFFC")
    (1, 1, 2, 1)
    """
    index_d = 0
    index_t = 0
    index_f = 0
    index_c = 0
    for f in chaine:
        # index prenant en compte le nombre de piece qui peuvent changer
        if f == "D":
            index_d += 1
        elif f == "T":
            index_t += 1
        elif f == "F":
            index_f += 1
        elif f == "C":
            index_c += 1
    return index_d, index_t, index_f, index_c


def chgmt_pion(joueur):
    """
        Permet de trouver en quel pieces le pion peut se transformer
    :param joueur: list tableau de spieces du joueur
    :return:choix: list tableau avec le spiece que le joueut peux choisir

    >>> chgmt_pion([['T', (0, 7)], ['C', (0, 1)]])
    ['D', 'T', 'F', 'C']
    """
    chgmt = []
    for e in joueur:
        # cherhce les pieces qui peuvent etre change
        if e[0] in ("D", "T", "F", "C"):
            chgmt.append(e[0])
    index_d, index_t, index_f, index_c = nombre_occurence(chgmt)
    choix = []
    # tableau qui prend en element les pieces qui ont disparu et peuvent
    # etre change
    if index_d == 0:
        choix.append("D")
    if index_t == 0 or index_t == 1:
        choix.append("T")
    if index_f == 0 or index_f == 1:
        choix.append("F")
    if index_c == 0 or index_c == 1:
        choix.append("C")
    if len(choix) == 0:
        choix.append("D")
        choix.append("T")
        choix.append("F")
        choix.append("C")
    return choix


def transforme_pion(joueur, index, choix):
    """
        Permet de transformer la piece
    :param joueur: list, piece du joueur
    :param index:
    :param choix: list, piece choisi
    :return:joueur: list, nouveau tableau la piece est remplacee

    >>> transforme_pion([['T', (0, 7)], ['C', (0, 1)]], 0, "F")
    [['F', (0, 7)], ['C', (0, 1)]]
    """
    joueur[index][0] = choix
    return joueur


def piece_choisit(choix):  # pas de doctest car input
    """
    Permet de sasir le choix
    :param choix: list
    :return: decision: char

    """
    sortie = False
    decision = ""
    while not sortie:
        decision = input("choix possible:" + str(choix))
        if decision in choix:
            sortie = True
    return decision


###########################################
#  Gestion des mouvements de piece        #
###########################################
def mvt_t_h(x, y, joueur, adversaire):
    """
    Permet de définir tous les mouvements de la tour horizontalement
    :param x:int, index d'un tableau (lignes)
    :param y:int, index d'un tableau (colonnes)
    :param joueur: list, tableau pièces du joueur 1
    :param adversaire: list, tableau pièces du second joueur
    :return: return mvt_tour, mange_tour(list,list): permet d'obtenir
    le tableau de déplacement possible et le tableau de pièces qui peuvent
    etre mange.
    """
    mvt_tour_temp = []
    mange_tour_temp = []
    # Je regarde sur l'axe horizontal
    for i in range(8):
        # On ne regarde pas notre position
        if (x, y) != (x, i):
            # Regarde si je suis sur une piece de mon adversaire
            if check_position_piece(x, i, adversaire):
                if i < y:
                    mange_tour_temp = [(x, i)]
                    # espace libre entre deux pieces a supprimer
                    mvt_tour_temp = []
                # Si je suis à droite de la piece je stoppe ma recherche
                else:
                    mange_tour_temp.append((x, i))
                    break
            # Regarde si je suis ne suis pas sur une de mes pieces
            elif not check_position_piece(x, i, joueur):
                # Mouvement possible
                mvt_tour_temp.append((x, i))
            # Je suis sur une de mes pieces à droite j'arrete
            elif i > y:
                break
            # Je suis sur une de mes piece à gauche je continu mais je
            # repars de zero
            else:
                mange_tour_temp = []
                mvt_tour_temp = []
    return mvt_tour_temp, mange_tour_temp


def mvt_t_v(x, y, joueur, adversaire):
    """
    Permet de définir tous les mouvements de la tour verticalement
    :param x:int, index d'un tableau (lignes)
    :param y:int, index d'un tableau (colonnes)
    :param joueur: list, tableau pièces du joueur 1
    :param adversaire: list, tableau pièces du second joueur
    :return: return mvt_tour_temp, mange_tour_temp(list,list): permet d'obtenir
    le tableau de déplacement possible et le tableau de pièces qui peuvent
    etre mange.
    """
    mvt_tour_temp = []
    mange_tour_temp = []
    # Je regarde sur l'axe vertical
    for i in range(8):
        # On ne regarde pas notre position
        if (x, y) != (i, y):
            # Regarde si je suis sur une piece de mon adversaire
            if check_position_piece(i, y, adversaire):
                if i < x:
                    mange_tour_temp = [(i, y)]
                    # espace libre entre deux pieces a supprimer
                    mvt_tour_temp = []
                # Si je suis à droite de la piece je stoppe ma recherche
                else:
                    mange_tour_temp.append((i, y))
                    break
            # Regarde si je suis ne suis pas sur une de mes pieces
            elif not check_position_piece(i, y, joueur):
                # Mouvement possible
                mvt_tour_temp.append((i, y))
            # Je suis sur une de mes pieces à droite j'arrete
            elif i > x:
                break
            # Je suis sur une de mes piece à gauche je continu mais je
            # repars de zero
            else:
                mange_tour_temp = []
                mvt_tour_temp = []
    return mvt_tour_temp, mange_tour_temp


def mvt_t(x, y, joueur, adversaire, index_piece, id_joueur,
          prise_passant, en_cours_echec):
    """
    Permet de creer le tableau complet des mvt possibles de la tour
    :param x:int, index d'un tableau (lignes)
    :param y:int, index d'un tableau (colonnes)
    :param joueur: list, tableau pièces du joueur 1
    :param adversaire: list, tableau pièces du second joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    :return: list,list: permet d'obtenir le tableau de déplacement possible
    et le tableau de pièces qui peuvent etre mange.

    >>> mvt_t(1, 1, [["T", (4, 3)]],0, [])
    ([(0, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (0, 1), (2, 1), \
(3, 1), (4, 1), (5, 1), (6, 1), (7, 1)], [])
    """
    mvt_tour_v, mange_tour_v = mvt_t_v(x, y, joueur, adversaire)
    mvt_tour_h, mange_tour_h = mvt_t_h(x, y, joueur, adversaire)
    mvt_tour = mvt_tour_v + mvt_tour_h
    mange_tour = mange_tour_v + mange_tour_h
    if not en_cours_echec:
        # suppresion des mvt, l'ensemble des positions qui mettrait notre
        # roi  en echec
        mvt_tour = empeche_echec(mvt_tour, index_piece, joueur, adversaire,
                                 id_joueur, prise_passant)
        mange_tour = empeche_echec(mange_tour, index_piece, joueur,
                                   adversaire,  id_joueur, prise_passant)
    return mvt_tour, mange_tour


def mvt_f_diag_x(x, y, joueur, adversaire):
    """
    Permet de définir tous les mouvements du fou d'un sens
    :param x:int, index d'un tableau (lignes)
    :param y:int, index d'un tableau (colonnes)
    :param joueur: list, tableau pièces du joueur 1
    :param adversaire: list, tableau pièces du second joueur
    :return: return mvt_fou_temp, mange_fou_temp(list,list): permet d'obtenir
    le tableau de déplacement possible et le tableau de pièces qui peuvent
    etre mange.
    """
    mvt_fou_temp = []
    mange_fou_temp = []
    for i in range(-8, 8):
        # On parcours de gauche à droite
        if est_dans_plateau(x + i, y - i) and (x + i, y - i) != (x, y):
            # On trouve une piece adverse que l'on peut manger
            if check_position_piece(x + i, y - i, adversaire):
                if x + i < x:
                    mange_fou_temp = [(x + i, y - i)]
                    mvt_fou_temp = []
                else:
                    mange_fou_temp.append((x + i, y - i))
                    break
            # On est sur une case vide pas adversaire ni joueur
            elif not check_position_piece(x + i, y - i, joueur):
                mvt_fou_temp.append((x + i, y - i))
            # On est sur une case joueur si on est sur la droite du plateau
            # on arrete, sinon on vide les mouvements précédent
            else:
                if (x + i) > x:
                    break
                else:
                    mvt_fou_temp = []
                    mange_fou_temp = []
    return mvt_fou_temp, mange_fou_temp


def mvt_f_diag_y(x, y, joueur, adversaire):
    """
    Permet de définir tous les mouvements du fou de l'autre sens
    :param x:int, index d'un tableau (lignes)
    :param y:int, index d'un tableau (colonnes)
    :param joueur: list, tableau pièces du joueur 1
    :param adversaire: list, tableau pièces du second joueur
    :return: return mvt_fou_temp, mange_fou_temp(list,list): permet d'obtenir
    le tableau de déplacement possible et le tableau de pièces qui peuvent
    etre mange.
    """
    mvt_fou_temp = []
    mange_fou_temp = []
    for i in range(-8, 8):
        if est_dans_plateau(x + i, y + i) and (x + i, y + i) != (x, y):
            if check_position_piece(x + i, y + i, adversaire):
                if y + i < y:
                    mange_fou_temp = [(x + i, y + i)]
                    mvt_fou_temp = []
                else:
                    mange_fou_temp.append((x + i, y + i))
                    break
            elif not check_position_piece(x + i, y + i, joueur):
                mvt_fou_temp.append((x + i, y + i))
            elif (y + i) > y:
                break
            else:
                mvt_fou_temp = []
                mange_fou_temp = []

    return mvt_fou_temp, mange_fou_temp


def mvt_f(x, y, joueur, adversaire, index_piece, id_joueur,
          prise_passant, en_cours_echec):
    """
    Permet de définir tous les mouvements du fou
    :param x: int, index d'un tableau (lignes)
    :param y: int, index d'un tableau (colonnes)
    :param joueur: liste, tableau pièces du joueur 1
    :param adversaire: list, tableau pièces du second joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    : return: return mvt_fou, mange_fou (liste, liste): permet d'obtenir
    le tableau de déplacement possible et le tableau de pièces qui peuvent
    etre mange.

    >>> mvt_f(1, 1, [["F", (4, 3)]],0, [])
    ([(0, 2), (2, 0), (0, 0), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],\
 [])
    """
    mvt_fou_diag_x, mange_fou_diag_x = mvt_f_diag_x(x, y, joueur, adversaire)
    mvt_fou_diag_y, mange_fou_y = mvt_f_diag_y(x, y, joueur, adversaire)
    mvt_fou = mvt_fou_diag_x + mvt_fou_diag_y
    mange_fou = mange_fou_diag_x + mange_fou_y
    if not en_cours_echec:
        # suppresion des mvt, l'ensemble des positions qui mettrait notre roi
        # en echec
        mvt_fou = empeche_echec(mvt_fou, index_piece, joueur, adversaire,
                                id_joueur, prise_passant)
        mange_fou = empeche_echec(mange_fou, index_piece, joueur,
                                  adversaire, id_joueur, prise_passant)
    return mvt_fou, mange_fou


def mvt_c(x, y, joueur, adversaire, index_piece, id_joueur,
          prise_passant, en_cours_echec):
    """
   Permet de savoir quel déplacement fait le cavalier et quel pièce il peut
   manger
    :param x:int, index d'un tableau (lignes)
    :param y:int, index d'un tableau (colonnes)
    :param joueur:list, tableau pièces d'un joueur
    :param adversaire:list, tableau pièces de l'autre joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    :return: mvt_cavalier, mvt_cavalier_mange(list,list): tableau des
    mouvements possibles, tableau des pièces pouvant etre mange.
    """
    mvt_cavalier = []
    for i in range(1, 3):
        for j in range(1, 3):
            mvtx = (-1)**i
            mvty = (-1)**j
            if est_dans_plateau(x + mvtx, y + 2 * mvty) and not \
                    check_position_piece(x + mvtx, y + 2 * mvty, joueur):
                mvt_cavalier.append((x + mvtx, y + 2 * mvty))
            if est_dans_plateau(x + 2 * mvtx, y + mvty) and not \
                    check_position_piece(x + 2 * mvtx, y + mvty, joueur):
                mvt_cavalier.append((x + 2 * mvtx, y + mvty))
    mvt_cavalier_mange = mvt_mange_list(mvt_cavalier, adversaire)
    # On supprimme des mouvements autorises les mouvments mange
    doublon = cherche_doublon(mvt_cavalier, mvt_cavalier_mange)
    if len(doublon) > 0:
        index_pop = 0
        for index in doublon:
            index = index - index_pop
            mvt_cavalier.pop(index)
            # remet l'index comme av le pop
            index_pop += 1
    if not en_cours_echec:
        # suppresion des mvt, l'ensemble des positions qui mettrait notre
        # roi en echec
        mvt_cavalier = empeche_echec(mvt_cavalier, index_piece, joueur,
                                     adversaire, id_joueur, prise_passant)
        mvt_cavalier_mange = empeche_echec(mvt_cavalier_mange, index_piece,
                                           joueur, adversaire, id_joueur,
                                           prise_passant)
    return mvt_cavalier, mvt_cavalier_mange


def mvt_d(x, y, joueur, adversaire, index_piece, id_joueur,
          prise_passant, en_cours_echec):
    """
    Permet de lister les mouvements de la dame
    :param x:list, index d'un tableau (lignes)
    :param y:list,index d'un tableau (colonnes)
    :param joueur: list, tableau du joueur
    :param adversaire: list, tableau pièces du second joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    :return:mvt_dame_t[0] + mvt_dame_f[0], mvt_dame_t[1] + mvt_dame_f[1]:
    permet d'obtenir les déplacements de la dame par rapport au fou et à
    la tour, de manière horizontale et verticale.
    """
    mvt_dame_t = mvt_t(x, y, joueur, adversaire, index_piece, id_joueur,
                       prise_passant, en_cours_echec)
    mvt_dame_f = mvt_f(x, y, joueur, adversaire, index_piece,
                       id_joueur, prise_passant, en_cours_echec)
    return mvt_dame_t[0] + mvt_dame_f[0], mvt_dame_t[1] + mvt_dame_f[1]


def mvt_r(x, y, joueur, adversaire, index_piece, id_joueur, prise_passant,
          en_cours_echec):
    """
    Permet de définir tous les mouvements du roi
    :param x: int, index d'un tableau (lignes)
    :param y: int, index d'un tableau (colonnes)
    :param joueur: liste, tableau pièces du joueur
    :param adversaire:list, tableau pièces de l'autre joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    :return:  list, list: permet d'obtenir le tableau de déplacement
    possible et le tableau de pièces qui peuvent etre mange.

    """
    mvt_roi = []
    roi_r, tour_pr, tour_gr = roque_possible(id_joueur)
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            # Test pour supprimer le déplacement (0,0) pas de déplacement ;-)
            if (i, j) != (0, 0):
                if est_dans_plateau(x + i, y + j) \
                        and not check_position_piece(x + i, y + j, joueur):
                    mvt_roi.append((x + i, y + j))
    # roque
    # Petit Rocque
    if not roi_r and not tour_pr:
        pas_de_piece_pr = True
        for idx_roi in range(1, 3):
            pas_de_piece_pr = pas_de_piece_pr \
                and not check_position_piece(x, y + idx_roi, joueur) \
                and not check_position_piece(x, y + idx_roi, adversaire)
        if pas_de_piece_pr:
            mvt_roi.append((x, y + 2))
    # Grand rocque
    if not roi_r and not tour_gr:
        pas_de_piece_gr = True
        for idx_roi in range(1, 4):
            pas_de_piece_gr = pas_de_piece_gr \
                and not check_position_piece(x, y - idx_roi, joueur) \
                and not check_position_piece(x, y - idx_roi, adversaire)
        if pas_de_piece_gr:
            mvt_roi.append((x, y - 2))
    mvt_roi_mange = mvt_mange_list(mvt_roi, adversaire)
    # On supprimme des mouvements autorises les mouvments mange
    doublon = cherche_doublon(mvt_roi, mvt_roi_mange)
    # print(f"MVT MANGE ROI {doublon} ")
    mvt_roi = delete_doublon(mvt_roi, doublon)
    if not en_cours_echec:
        # suppresion des mvt, l'ensemble des positions qui mettrait notre
        # roi en echec
        mvt_roi = empeche_echec(mvt_roi, index_piece, joueur, adversaire,
                                id_joueur, prise_passant)
        # print(f"MVT ROI sans echec {mvt_roi} ")
        mvt_roi_mange = empeche_echec(mvt_roi_mange, index_piece, joueur,
                                      adversaire, id_joueur, prise_passant)
        # print(f"MVT MANGE ROI sans echec{mvt_roi_mange} ")
    return mvt_roi, mvt_roi_mange


def mvt_p(x, y, joueur, adversaire, index_piece, id_joueur,
          id_mvt, prise_passant, en_cours_echec):
    """
    Permet de lister les mouvements des pions
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :param adversaire:list, tableau de pieces de l'autre joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param id_mvt:int, permet de savoir si le joueur est en haut ou en bas
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    :return: mvt_pion, mvt_pion_mange (list, list):tableau des mouvement
    possibles, tableau des pieces pouvant etre mange par le pion.

    >>> mvt_p(1, 3, [['P', (1, 3)]], [['P', (6, 1)]], 1, [False, (7,2)])
    ([(2, 3), (3, 3)], [])

    """

    mvt_pion = []
    mvt_pion_mange = []
    # Deplacement pour manger du pion
    if est_dans_plateau(x + 1 * id_mvt, y - 1):
        if check_position_piece(x + 1 * id_mvt, y - 1, adversaire):
            mvt_pion_mange.append((x + 1 * id_mvt, y - 1))
    if est_dans_plateau(x + 1 * id_mvt, y + 1):
        if check_position_piece(x + 1 * id_mvt, y + 1, adversaire):
            mvt_pion_mange.append((x + 1 * id_mvt, y + 1))
    # Cas particulier de la prise en passant
    if prise_passant[0]:
        if check_position_piece(x, y + 1, prise_passant[1]):
            mvt_pion_mange.append((x + 1 * id_mvt, y + 1))
        if check_position_piece(x, y - 1, prise_passant[1]):
            mvt_pion_mange.append((x + 1 * id_mvt, y - 1))
    # Deplacement du pion pour avancer
    if (not check_position_piece(x + 1 * id_mvt, y, joueur)) and \
            (not check_position_piece(x + 1 * id_mvt, y, adversaire)):
        mvt_pion.append((x + 1 * id_mvt, y))
        if (x == 1 or x == 6) and \
                not check_position_piece(x + 2 * id_mvt, y, joueur) and \
                not check_position_piece(x + 2 * id_mvt, y, adversaire) and \
                not check_position_piece(x + 1 * id_mvt, y, joueur) and \
                not check_position_piece(x + 1 * id_mvt, y, adversaire):
            mvt_pion.append((x + 2 * id_mvt, y))
    if not en_cours_echec:
        # suppresion des mvt, l'ensemble des positions qui mettrait notre
        # roi en echec
        mvt_pion = empeche_echec(mvt_pion, index_piece, joueur, adversaire,
                                 id_joueur, prise_passant, id_mvt)
        mvt_pion_mange = empeche_echec(mvt_pion_mange, index_piece, joueur,
                                       adversaire, id_joueur, prise_passant,
                                       id_mvt)
    return mvt_pion, mvt_pion_mange


###########################################
#  Gestion de l'echec                     #
###########################################
def echec(roi_x, roi_y, joueur_qui_joue, adversaire, id_joueur,
          id_mvt, prise_passant, en_cours_echec):
    """
    Permet de savoir si le roi adverse est en echec
    :param roi_x: int
    :param roi_y: int
    :param joueur_qui_joue:list
    :param adversaire: list, tableau pièces du second joueur
    :param id_joueur: list, tableau pièces du second joueur
    :param id_mvt:int, permet de savoir si le joueur est en haut ou en bas
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param en_cours_echec:bool, indique si on est en echec
    :return: list, index des pieces qui met en echec le roi adverse
    """
    # il faut parcourir toutes les pieces de notre jeu et verifier que l'on
    # a pas de roi adverse dans nos tableaux mange
    index = 0
    mange = []
    list_echec = []
    for p in joueur_qui_joue:
        if p[0] == "T":
            _, mange = mvt_t(p[1][0], p[1][1], joueur_qui_joue, adversaire,
                             index, id_joueur, prise_passant, en_cours_echec)
        if p[0] == "F":
            _, mange = mvt_f(p[1][0], p[1][1], joueur_qui_joue, adversaire,
                             index, id_joueur, prise_passant, en_cours_echec)
        if p[0] == "C":
            _, mange = mvt_c(p[1][0], p[1][1], joueur_qui_joue, adversaire,
                             index, id_joueur, prise_passant, en_cours_echec)
        if p[0] == "D":
            _, mange = mvt_d(p[1][0], p[1][1], joueur_qui_joue, adversaire,
                             index, id_joueur, prise_passant,
                             en_cours_echec)
        if p[0] == "P":
            id_mvt *= -1
            _, mange = mvt_p(p[1][0], p[1][1], joueur_qui_joue, adversaire,
                             index, id_joueur, id_mvt, prise_passant,
                             en_cours_echec)
        if p[0] == "R":
            _, mange = mvt_r(p[1][0], p[1][1], joueur_qui_joue, adversaire,
                             index, id_joueur, prise_passant, en_cours_echec)
        if is_double_place(mange, roi_x, roi_y):
            list_echec.append(index)
        index += 1
    return list_echec


def echec_simple(mvt, roi_x, roi_y,):
    """
    Permet de savoir si le roi adverse est en echec
    :param mvt:list
    :param roi_x: int
    :param roi_y: int
    :return: list, index des pieces qui met en echec le roi adverse
    """
    # il faut parcourir toutes les pieces de notre jeu et verifier que l'on
    # a pas de roi adverse dans nos tableaux mange
    if is_double_place([mvt], roi_x, roi_y):
        return True
    return False


def test_reste_en_echec(mouvement, index_piece, joueur, adversaire,
                        id_joueur, prise_passant):
    list_echec = reste_en_echec(mouvement, index_piece, joueur,
                                adversaire, id_joueur, prise_passant)
    return list_echec


def mat(joueur, adversaire, id_joueur, id_mvt, prise_passant):
    # le joueur dois pouvoir bouger une piece et qu'il n'y ai plus de
    # situation d
    # echec
    index_piece = 0
    mange = []
    mvt = []
    for p in joueur:
        if p[0] == "T":
            mvt, mange = mvt_t(p[1][0], p[1][1], joueur, adversaire,
                               index_piece, id_joueur,
                               prise_passant, True)
        if p[0] == "F":
            mvt, mange = mvt_f(p[1][0], p[1][1], joueur, adversaire,
                               index_piece, id_joueur,
                               prise_passant, True)
        if p[0] == "C":
            mvt, mange = mvt_c(p[1][0], p[1][1], joueur, adversaire,
                               index_piece, id_joueur, prise_passant, True)
        if p[0] == "D":
            mvt, mange = mvt_d(p[1][0], p[1][1], joueur, adversaire,
                               index_piece, id_joueur,
                               prise_passant, True)
        if p[0] == "P":
            mvt, mange = mvt_p(p[1][0], p[1][1], joueur, adversaire,
                               index_piece, id_joueur, id_mvt,
                               prise_passant, True)
        if p[0] == "R":
            mvt, mange = mvt_r(p[1][0], p[1][1], joueur, adversaire,
                               index_piece, id_joueur, prise_passant, True)
        # Je dois analyser les mouvements et verifier que je ne suis plus en
        # echec je simule donc mon mouvement puis je contrôle l'echec
        if len(mvt) > 0:
            list_echec = test_reste_en_echec(mvt, index_piece, joueur,
                                             adversaire, id_joueur,
                                             prise_passant)
            if len(list_echec) == 0:
                # Il n'y a pas d'echec
                return False
        if len(mange) > 0:
            list_echec = test_reste_en_echec(mange, index_piece, joueur,
                                             adversaire, id_joueur,
                                             prise_passant)
            if len(list_echec) == 0:
                # Il n'y a pas d'echec
                return False
        index_piece += 1
    return True


def pat(joueur, adversaire, id_joueur, id_mvt, prise_passant):
    index_piece = 0
    mvt = []
    mange = []
    en_cours_echec = False
    # print(f"Analyse du PAT {id_joueur} {joueur}")
    trouve_roi, index_roi = cherche_roi(joueur)
    if trouve_roi:
        is_echec = echec(joueur[index_roi][1][0], joueur[
            index_roi][1][1], adversaire, joueur,
                         id_joueur, id_mvt, prise_passant, True)
        if len(is_echec) > 0:
            return False
        else:
            for p in joueur:
                if p[0] == "T":
                    mvt, mange = mvt_t(p[1][0], p[1][1], joueur, adversaire,
                                       index_piece, id_joueur,
                                       prise_passant, en_cours_echec)
                if p[0] == "F":
                    mvt, mange = mvt_f(p[1][0], p[1][1], joueur, adversaire,
                                       index_piece, id_joueur,
                                       prise_passant, en_cours_echec)
                if p[0] == "C":
                    mvt, mange = mvt_c(p[1][0], p[1][1], joueur, adversaire,
                                       index_piece, id_joueur, prise_passant,
                                       en_cours_echec)
                if p[0] == "D":
                    mvt, mange = mvt_d(p[1][0], p[1][1], joueur, adversaire,
                                       index_piece, id_joueur, prise_passant,
                                       en_cours_echec)
                if p[0] == "P":
                    mvt, mange = mvt_p(p[1][0], p[1][1], joueur, adversaire,
                                       index_piece, id_joueur, id_mvt,
                                       prise_passant, en_cours_echec)
                if p[0] == "R":
                    mvt, mange = mvt_r(p[1][0], p[1][1], joueur, adversaire,
                                       index_piece, id_joueur, prise_passant,
                                       en_cours_echec)
                # Ici je n'ai pas de mouvements possible alors que je ne suis
                #  pas enechec je suis en PAT
                if len(mvt) > 0 or len(mange) > 0:
                    return False
                index_piece += 1
            return True
    return False


def echec_mon_roi(roi_x, roi_y, joueur_qui_joue_simule, adv_simule,
                  id_joueur, prise_passant, id_mvt):
    # On doit regarder tous les coups possible de l'adversaire qui peut
    # manger le roi
    if id_joueur == 0:
        new_id_joueur = 1
    else:
        new_id_joueur = 0
    list_echec = echec(roi_x, roi_y, adv_simule, joueur_qui_joue_simule,
                       new_id_joueur, id_mvt, prise_passant, True)
    if len(list_echec) == 0:
        return False
    else:
        return True


def reste_en_echec(mvt, index_piece, joueur, adversaire,
                   id_joueur, prise_passant):
    # On doit regarder tous les coups possible de l'adversaire qui peut
    # manger le roi
    joueur_qui_joue_simule = deepcopy(joueur)
    list_echec = []
    for m in mvt:
        adv_simule = deepcopy(adversaire)
        joueur_qui_joue_simule[index_piece][1] = m

        index_pos_val = index_position(m[0], m[1], adversaire)
        if index_pos_val > 0:
            adv_simule.pop(index_pos_val)
        # On vient de creer un mouvement de piece, il faut maintenant vérifier
        # que  l'adversaire ne peut pas manger mon roi
        trouve_roi, index_roi = cherche_roi(joueur_qui_joue_simule)
        if trouve_roi:
            if id_joueur == 0:
                new_id_joueur = 1
                new_id_mvt = -1
            else:
                new_id_joueur = 0
                new_id_mvt = 1
            list_echec = echec(joueur_qui_joue_simule[index_roi][1][0],
                               joueur_qui_joue_simule[index_roi][1][1],
                               adv_simule, joueur_qui_joue_simule,
                               new_id_joueur, new_id_mvt,
                               prise_passant, True)
    return list_echec


def empeche_echec(mvt, index_piece, joueur_qui_joue,
                  adversaire, id_joueur, prise_passant, id_mvt=1):
    """
    Permet de creer un tableau de mvt possibles qui ne mette pas le roi en
    echec
    :param mvt: list
    :param index_piece: int
    :param joueur_qui_joue: list
    :param adversaire: list, tableau pièces du second joueur
    :param index_piece: int, index de la piece
    :param id_joueur:int, permet de savoir quel joueur joue
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :param id_mvt:int
    :return: new_mvt : list des mvt possibles sans mise en echec du roi du
    joueur
    """
    # ATTENTION en python on ne copie pas assigner à une nouvelle liste une
    # liste déjà existante ne la duplique pas mais donne tout simplement
    # une deuxième porte d’accès à cette liste
    # List() et [:] ne sont pas récursifs. Ce qui veut dire qu’ils ne vont
    # dupliquer que la liste de premier niveau et pas les listes qu’elle
    # peut  elle-même contenir.il est nécessaire de passer par la fonction
    # deepcopy(). Cette fonction permet de copier tout object et les objects
    # qu’il peut imbriquer.
    joueur_qui_joue_simule = deepcopy(joueur_qui_joue)
    new_mvt = []
    for e in mvt:
        adv_simule = deepcopy(adversaire)
        joueur_qui_joue_simule[index_piece][1] = e
        # Je vérifie que je ne mange pas une piece adverse si oui
        # alors je supprime l'element de jeu adverse
        index_pos_val = index_position(e[0], e[1], adversaire)
        if index_pos_val > 0:
            adv_simule.pop(index_pos_val)
        # On vient de creer un mouvement de piece, il faut maintenant
        # vérifier que l'adversaire ne peut pas manger mon roi
        trouve_roi, index_roi = cherche_roi(joueur_qui_joue_simule)
        # Si on est dans un jeu d'apprentissage il peut ne pas y avoir de roi
        if trouve_roi:
            roi_x = joueur_qui_joue_simule[index_roi][1][0]
            roi_y = joueur_qui_joue_simule[index_roi][1][1]
            if not echec_mon_roi(roi_x, roi_y, joueur_qui_joue_simule,
                                 adv_simule, id_joueur, prise_passant, id_mvt):
                # ajout du mvt car pas d'echec
                new_mvt.append(e)
        else:
            new_mvt.append(e)
    return new_mvt


###########################################
#  Gestion du replay                      #
###########################################
def replay(jeu_str):
    fichier = open(jeu_str, "r")
    readlines = fichier.readlines()
    fichier.close()
    j1, j2, mvt_possible = creer_set(1)
    index = 0
    chaine_coord = ""
    nom_blanc = "Blanc"
    nom_noir = "Noir"
    for j in readlines:
        if index == 4:
            nom_blanc = j.split()
        if index == 5:
            nom_noir = j.split()
        if 11 < index:
            chaine_coord += j
        index += 1
    coord = chaine_coord.split()
    index = 0
    vainqueur_jeu = ""
    partie_joue = []
    partie_coord = []
    for e in coord:
        find_dot = e.find('.')
        if index % 2 == 0 and find_dot < 1:
            index += 1
            id_mvt = -1
            j1, j2 = analyse_piece(e, j1, j2, id_mvt)
            partie_joue.append(deepcopy(j1))
            partie_joue.append(deepcopy(j2))
            partie_coord.append(e)
        elif find_dot < 1:
            index += 1
            id_mvt = 1
            j2, j1 = analyse_piece(e, j2, j1, id_mvt)
            partie_joue.append(deepcopy(j1))
            partie_joue.append(deepcopy(j2))
            partie_coord.append(e)
    partie_joue.append(deepcopy(j1))
    partie_joue.append(deepcopy(j2))
    if coord[-1] == '0-1':
        vainqueur_jeu = "Bravo joueur 2"
    elif coord[-1] == '1-0':
        vainqueur_jeu = "Bravo joueur 1"
    elif coord[-1] == '1-1':
        vainqueur_jeu = "Belle partie nulle"
    return partie_joue, vainqueur_jeu, nom_blanc[1], nom_noir[1], partie_coord


def analyse_piece(mvt_piece, joueur, adversaire, id_mvt):
    prise_passant = 'False', [['P', (0, 0)]]
    ret_adversaire = deepcopy(adversaire)
    is_mange = False
    coo_x = -1
    coo_y = -1
    if mvt_piece[0].islower():
        joueur, is_mange, coo_x, coo_y = analyse_pion(mvt_piece, joueur,
                                                      id_mvt)
    elif mvt_piece[0] == 'Q':
        joueur, is_mange, coo_x, coo_y = analyse_dame(mvt_piece, joueur)
    elif mvt_piece[0] == 'N':
        joueur, is_mange, coo_x, coo_y = \
            analyse_cavalier(mvt_piece, joueur, adversaire, prise_passant)
    elif mvt_piece[0] == 'B':
        joueur, is_mange, coo_x, coo_y = \
            analyse_fou(mvt_piece, joueur, adversaire, prise_passant)
    elif mvt_piece[0] == 'R':
        joueur, is_mange, coo_x, coo_y = \
            analyse_tour(mvt_piece, joueur, adversaire, prise_passant)
    elif mvt_piece[0] == 'K':
        _, index_piece = cherche_roi(joueur)
        coo_x, coo_y, _, _, is_mange, is_echec, is_mat, _ = translate(
            mvt_piece[1:])
        joueur[index_piece][1] = (coo_x, coo_y)
    elif mvt_piece[0] == 'O':
        # c'est un roque il faut savoir si il est à droite ou à gauche
        is_mange = False
        coo_x = -1
        coo_y = -1
        joueur = analyse_roque(joueur, mvt_piece, id_mvt)
    if is_mange:
        idx_efface = index_position(coo_x, coo_y, ret_adversaire)
        ret_adversaire.pop(idx_efface)
    return joueur, ret_adversaire


def analyse_roque(joueur, mvt_piece, id_mvt):
    _, position_roi = cherche_roi(joueur)
    if mvt_piece == 'O-O':
        # Petit Roque
        if id_mvt < 0:
            _, index_piece = name_piece(0, 0, joueur)
            joueur[position_roi][1] = (0, 1)
            joueur[index_piece][1] = (0, 2)
        else:
            name, index_piece = name_piece(7, 0, joueur)
            joueur[position_roi][1] = (7, 1)
            joueur[index_piece][1] = (7, 2)
    else:
        if id_mvt < 0:
            _, index_piece = name_piece(0, 7, joueur)
            joueur[position_roi][1] = (0, 5)
            joueur[index_piece][1] = (0, 4)
        else:
            _, index_piece = name_piece(7, 7, joueur)
            joueur[position_roi][1] = (7, 5)
            joueur[index_piece][1] = (7, 4)
    return joueur


def analyse_tour(mouvement, joueur, adversaire, prise_passant):
    _, position = cherche_piece("T", joueur)
    (coo_x, coo_y, pos_ambiguite_x, pos_ambiguite_y, is_mange, is_echec,
     is_mat, _) = translate(mouvement[1:])
    for p in position:
        mvt, mange = mvt_t(joueur[p][1][0], joueur[p][1][1], joueur,
                           adversaire, position[0], 1, prise_passant, True)
        if (coo_x, coo_y) in mvt or (coo_x, coo_y) in mange:
            ambiguite_x = controle_ambiguite(pos_ambiguite_x, joueur[p][1][0])
            ambiguite_y = controle_ambiguite(pos_ambiguite_y, joueur[p][1][1])
            if joueur[p][1] == (ambiguite_x, ambiguite_y):
                joueur[p][1] = (coo_x, coo_y)
                break
    return joueur, is_mange, coo_x, coo_y


def analyse_fou(mouvement, joueur, adversaire, prise_passant):
    _, position = cherche_piece("F", joueur)
    (coo_x, coo_y, pos_ambiguite_x, pos_ambiguite_y, is_mange, is_echec,
     is_mat, _) = translate(mouvement[1:])
    for p in position:
        mvt, mange = mvt_f(joueur[p][1][0], joueur[p][1][1], joueur,
                           adversaire, position[0], 1, prise_passant, True)
        if (coo_x, coo_y) in mvt or (coo_x, coo_y) in mange:
            ambiguite_x = controle_ambiguite(pos_ambiguite_x, joueur[p][1][0])
            ambiguite_y = controle_ambiguite(pos_ambiguite_y, joueur[p][1][1])
            if joueur[p][1] == (ambiguite_x, ambiguite_y):
                joueur[p][1] = (coo_x, coo_y)
                break
    return joueur, is_mange, coo_x, coo_y


def get_position(lettre_plateau):
    lettre = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    index_lettre = 0
    for le in lettre:
        if le == lettre_plateau:
            return index_lettre
        index_lettre += 1
    return -1


def translate(mouvements):
    """
    :param mouvements:
    :return:

    >>> translate("e4")
    (3, 3, -1, -1, False, False, false, "")

    >>> translate("exd5")
    (4, 4, -1, -1, True, False, False, "")

    >>> translate("ec3")
    (2, 5, -1, 3, False, False, False, "")

    >>> translate("fxe2")
    (1, 3, -1, -1, True, False, False, "")
    """
    pos_y = -1
    pos_x = -1
    is_mange = False
    is_echec = False
    is_mat = False
    is_une_lettre = True
    is_un_chiffre = True
    pos_ambiguite_x = -1
    pos_ambiguite_y = -1
    promotion = ""
    for c in mouvements:
        if c == "x":
            is_mange = True
        elif c == "+":
            is_echec = True
        elif c == "#":
            is_mat = True
        elif c.isalpha() and c.islower():
            if is_une_lettre:
                pos_y = get_position(c)
                is_une_lettre = False
            else:
                pos_ambiguite_y = pos_y
                pos_y = get_position(c)
        elif c.isnumeric():
            if is_un_chiffre:
                pos_x = int(c) - 1
                is_un_chiffre = False
            else:
                pos_ambiguite_x = pos_y
                pos_x = int(c) - 1
        elif c.isupper():
            promotion = c
    return (pos_x, pos_y, pos_ambiguite_x, pos_ambiguite_y, is_mange,
            is_echec, is_mat, promotion)


def controle_ambiguite(val_ambigu, val):
    if val_ambigu >= 0:
        return val_ambigu
    else:
        return val


def en_francais(promotion):
    if promotion == "Q":
        return "D"
    elif promotion == "B":
        return "F"
    elif promotion == "N":
        return "C"
    elif promotion == 'R':
        return "T"


def analyse_pion(mouvement, joueur, id_mvt):
    # On bouge un pion
    (coo_x, coo_y, pos_ambiguite_x, pos_ambiguite_y, is_mange, is_echec,
     is_mat, promotion) = translate(mouvement)
    if is_mange:
        if pos_ambiguite_y >= 0:
            name, index_piece = name_piece(coo_x + (1 * id_mvt),
                                           pos_ambiguite_y, joueur)
            if index_piece < 0 or name != "P":
                name, index_piece = name_piece(coo_x + (1 * id_mvt),
                                               pos_ambiguite_y, joueur)
            joueur[index_piece][1] = (coo_x, coo_y)

        else:
            name, index_piece = \
                name_piece(coo_x + (1 * id_mvt), coo_y + 1, joueur)
            if index_piece < 0 or name != "P":
                name, index_piece = name_piece(coo_x + (1 * id_mvt), coo_y - 1,
                                               joueur)
            joueur[index_piece][1] = (coo_x, coo_y)
            return joueur, is_mange, coo_x, coo_y
    else:
        name, index_piece = name_piece(coo_x + (1 * id_mvt), coo_y, joueur)
        if index_piece < 0:
            name, index_piece =\
                name_piece(coo_x + (2 * id_mvt), coo_y,  joueur)
        joueur[index_piece][1] = (coo_x, coo_y)
    if promotion != "":
        joueur[index_piece][0] = en_francais(promotion)
    return joueur, is_mange, coo_x, coo_y


def analyse_dame(mouvement, joueur):
    _, index_piece = cherche_piece("D", joueur)
    coo_x, coo_y, _, _, is_mange, is_echec, is_mat, _ = translate(mouvement[
                                                                  1:])
    idx = index_piece[0]
    joueur[idx][1] = (coo_x, coo_y)
    return joueur, is_mange, coo_x, coo_y


def analyse_cavalier(mouvement, joueur, adversaire, prise_passant):
    _, position = cherche_piece("C", joueur)
    (coo_x, coo_y, pos_ambiguite_x, pos_ambiguite_y, is_mange, is_echec,
     is_mat, _) = translate(mouvement[1:])
    for p in position:
        mvt, mange = mvt_c(joueur[p][1][0], joueur[p][1][1], joueur,
                           adversaire, position[0], 1, prise_passant, True)
        if (coo_x, coo_y) in mvt or (coo_x, coo_y) in mange:
            ambiguite_x = controle_ambiguite(pos_ambiguite_x, joueur[p][1][0])
            ambiguite_y = controle_ambiguite(pos_ambiguite_y, joueur[p][1][1])
            if joueur[p][1] == (ambiguite_x, ambiguite_y):
                joueur[p][1] = (coo_x, coo_y)
                break
    return joueur, is_mange, coo_x, coo_y


###########################################
#  Gestion des mouvements                 #
###########################################
def creer_mvt(list_mvt, dessin):
    """
    Permet de visualiser les mouvement des pieces
    :param list_mvt:list, tableau
    :param dessin: str, XX pour position de mvt et OO pour mange
    :return:list: de dessin

    >>> creer_mvt([ (3, 3),  (5, 2)], "P")
    [('P', (3, 3)), ('P', (5, 2))]
    """
    retour_list = []
    for e in list_mvt:
        retour_list.append((dessin, e))
    return retour_list


def cherche_doublon(mouvement, mouvement_mange):
    """
    Permet de savoir si une case est a la fois dans le tableau mange et/ou mvt
    :param mouvement:list, tableau des mouvements possibles propre a une piece
    :param mouvement_mange:list, tableau des mouvements possibles pour
    manger une piece de l'adversaire
    :return:list, tableau des coo de la case etant dans les 2 cases cite
    precedemment

    >>> cherche_doublon([(1,0), (0,0)], [(0,0)],)
    [1]
    """
    trouver = []
    # index = 0
    for mvt in mouvement_mange:
        index = 0
        for mange in mouvement:
            if mvt == mange:
                trouver.append(index)
            index += 1
    return trouver


def mvt_mange_list(mvt, adversaire):
    """
    Permet de creer un tableau avec les pieces mange
    :param mvt:list, tableau des mouvement possibles par une pieces
    :param adversaire:list, tableau
    :return:list, tableau contenant les coo des pieces pouvant etre mange

    >>> mvt_mange_list([['P', (1, 0)], ['P', (1, 1)]],[['P', (1, 1)], ['P',\
    (1, 2)]])
    []
    """
    mvt_mange = []
    for e in mvt:
        for f in adversaire:
            if e == f[1]:
                mvt_mange.append(f[1])
    return mvt_mange


def roque_possible(id_joueur):
    """
    Permet de savoir si les pieces de roques ont bougées
    :param id_joueur: int
    :return:tuple: booléens du statut des pieces associees
    """
    if id_joueur == 0:
        roi_r = roi_bouge[0]
        tour_gr = tour_bouge[0]
        tour_pr = tour_bouge[1]
    else:
        roi_r = roi_bouge[1]
        tour_gr = tour_bouge[2]
        tour_pr = tour_bouge[3]
    return roi_r, tour_pr, tour_gr


def delete_doublon(mvt_roi, doublon):
    """
    Permet de supprimer les mvt qui sont dans les deux tableau : deplacement et
    manger
    :param mvt_roi: list
    :param doublon: list
    :return: list,   ensemble des mouvements du roi
    """
    # print(f"{doublon} {mvt_roi}")
    if len(doublon) > 0:
        for index in doublon:
            mvt_roi.pop(index)
    return mvt_roi


def is_double_place(mouvement_piece, case_arrivee_x, case_arrivee_y):
    """
    Permet de savoir si une piece peut aller a un endroit precis
    :param mouvement_piece: list
    :param case_arrivee_x: int
    :param case_arrivee_y: int
    :return: booleens
    """
    for e in mouvement_piece:
        x, y = e
        if x == case_arrivee_x and y == case_arrivee_y:
            return True
    return False


def deplacement_autorise(piece, case_x, case_y, joueur_qui_joue, adversaire,
                         id_joueur, id_mvt, index_piece, prise_passant):
    """
    Permet le deplacement des pieces
    :param piece: str
    :param case_x: int
    :param case_y: int
    :param joueur_qui_joue: list
    :param adversaire: list
    :param id_joueur: int
    :param id_mvt: int
    :param index_piece: int
    :param prise_passant: list
    :return: ret_list_mvt_deplacement, ret_list_mvt_mange (list,
    list) retourne des listes des mvt et des possibilite de manger
    """
    ret_list_mvt_deplacement = []
    ret_list_mvt_mange = []
    if piece == 'P':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_p(case_x, case_y,
                                                             joueur_qui_joue,
                                                             adversaire,
                                                             index_piece,
                                                             id_joueur,
                                                             id_mvt,
                                                             prise_passant,
                                                             False)
    elif piece == 'T':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_t(case_x, case_y,
                                                             joueur_qui_joue,
                                                             adversaire,
                                                             index_piece,
                                                             id_joueur,
                                                             prise_passant,
                                                             False)
    elif piece == 'C':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_c(case_x, case_y,
                                                             joueur_qui_joue,
                                                             adversaire,
                                                             index_piece,
                                                             id_joueur,
                                                             prise_passant,
                                                             False)
    elif piece == 'F':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_f(case_x, case_y,
                                                             joueur_qui_joue,
                                                             adversaire,
                                                             index_piece,
                                                             id_joueur,
                                                             prise_passant,
                                                             False)
    elif piece == 'R':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_r(case_x, case_y,
                                                             joueur_qui_joue,
                                                             adversaire,
                                                             index_piece,
                                                             id_joueur,
                                                             prise_passant,
                                                             False)
    elif piece == 'D':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_d(case_x, case_y,
                                                             joueur_qui_joue,
                                                             adversaire,
                                                             index_piece,
                                                             id_joueur,
                                                             prise_passant,
                                                             False)
    return ret_list_mvt_deplacement, ret_list_mvt_mange


###########################################
#  Gestion de la sauvegarde du jeu        #
###########################################
def init_sauvegarde(name, site, nb_jeu, white_name, black_name, typej1,
                    typej2):
    """
    Permet de creer un fichier de sauvegarde des mvt pour pouvoir rejouer
    /format pgn
    :param name:str
    :param site:str
    :param nb_jeu:str
    :param white_name:str
    :param black_name:str
    :param typej1:str
    :param typej2:str
    :return: None
    """
    fichier = open("data.txt", "w")
    fichier.write(f'[Event "{name}"] \n')
    fichier.write(f'[Site "{site}" ] \n')
    t = datetime.now()
    fichier.write(f'Date "{t.strftime("%Y.%m.%d")}" ]\n')
    fichier.write(f'[Round "{nb_jeu}" ]\n')
    fichier.write(f'[White "{white_name}" ]\n')
    fichier.write(f'[Black "{black_name}" ]\n')
    fichier.write(f'[Time_begin "{t.strftime("%H:%M:%S")}"]\n')
    fichier.write(f'[WhiteType: "{typej1} ]"\n')
    fichier.write(f'[BlackType: "{typej2} ]"\n\n')
    fichier.close()


def translate_piece(piece):
    """
    Permet de traduire les pieces en anglais pour la sauvegarde
    :param piece:
    :return:str

    >>> translate_piece("T")
    'R'

    """
    if piece == 'P':
        return ""
    elif piece == 'T':
        return "R"
    elif piece == 'C':
        return "N"
    elif piece == 'F':
        return "B"
    elif piece == 'D':
        return "Q"
    else:
        return piece


def sauvegarde(nbcoup, coupj1, coupj2):
    """
    Permet de sauvegarder
    :param nbcoup:int
    :param coupj1:int
    :param coupj2:int
    :return: None
    """
    fichier = open("data.txt", "a")
    fichier.write(f"{nbcoup}. {coupj1} {coupj2} ")
    if nbcoup % 5 == 0 and nbcoup != 0:
        fichier.write("\n")
    fichier.close()


def fin_jeu(result):
    """
    Permet de sauvegarder la partie termine
    :param result: str
    :return: None
     """
    fichier = open("data.txt", "r")
    readlines = fichier.readlines()
    fichier.close()
    fichier = open("data.txt", "w")
    index = 0
    for readline in readlines:
        if index == 7:
            t = datetime.now()
            fichier.write(f'[Time_end "{t.strftime("%H:%M:%S")}"]\n')
            fichier.write(f'[Result "{result}"]\n')
            fichier.write(readline)
        else:
            fichier.write(readline)
        index += 1
    fichier.write(f"\n{result}")
    fichier.close()


def sauv_deplacement(piece, pos_init_y, pos_x, pos_y, mange,
                     ambigu, promotion):
    """
    Permet de definir un  mvt en format pgn
    :param piece:str
    :param pos_init_y:int
    :param pos_x:int
    :param pos_y:int
    :param mange:str
    :param ambigu: booleens
    :param promotion:str
    :return:str
    """
    colonne = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    rocque = False
    deplacement = ""
    if piece == 'R':
        if abs(pos_init_y - pos_y) == 2:
            deplacement = "O-O"
            rocque = True
        elif abs(pos_init_y - pos_y) == 3:
            deplacement = "O-O-O"
            rocque = True
        else:
            piece = "K"
    sauv_piece = translate_piece(piece)
    if mange == "x" and piece == "P":
        mange = colonne[pos_init_y] + mange
    if not rocque:
        if ambigu:
            deplacement = str(sauv_piece + colonne[pos_init_y] + mange +
                              colonne[pos_y] + str(pos_x + 1))
        else:
            deplacement = str(
                sauv_piece + mange + colonne[pos_y] + str(pos_x + 1))
        # En cas de promotion d un pion
        if promotion != "":
            deplacement += "="+promotion
    return deplacement


###########################################
#  On joue en mode texte                  #
###########################################
def chess():
    """

    :return:
    """
    joueur1, joueur2, mvt_possible = creer_set(1)
    init_sauvegarde("CPES YEAH !!!", "MLV", "1", "CC", "LB", "Human", "Human")
    affiche_set(joueur1, joueur2, mvt_possible, mvt_mange=[])
    jouer = True
    id_joueur = 0
    nb_coup = 1
    prise_passant = 'False', [['P', (0, 0)]]
    coupj = ""
    coupj1 = ""
    gain = []
    partie = []
    while jouer:
        if id_joueur == 0:
            id_mvt = 1
            joueur_qui_joue = deepcopy(joueur1)
            adversaire = deepcopy(joueur2)
        else:
            id_mvt = -1
            joueur_qui_joue = deepcopy(joueur2)
            adversaire = deepcopy(joueur1)
        # On test le pat
        if pat(joueur_qui_joue, adversaire, id_joueur, id_mvt,
               prise_passant):
            print("PAT !!!")
            gain.append("PAT")
            jouer = False
        else:
            click_ok = False
            print(f"Joueur {id_joueur + 1} c'est à vous")
            piece = ""
            index_pos = 0
            list_mvt_deplacement = []
            list_mvt_mange = []
            case_x = 0
            case_y = 0
            while not click_ok:
                # case_x = int(input("case x "))
                # case_y = int(input("case y "))
                deplacement = demande_case("case xy")
                case_x = int(deplacement[0])
                case_y = int(deplacement[1])
                if check_position_piece(case_x, case_y, joueur_qui_joue):
                    piece, index_pos = name_piece(case_x, case_y,
                                                  joueur_qui_joue)
                    list_mvt_deplacement, list_mvt_mange =  \
                        deplacement_autorise(piece, case_x, case_y,
                                             joueur_qui_joue, adversaire,
                                             id_joueur, id_mvt, index_pos,
                                             prise_passant)
                    click_ok = True
                if not click_ok:
                    if case_x == -1 and case_y == -1:
                        click_ok = True
                        jouer = False
                    else:
                        print("Vous coordonnées ne sont pas exactes !")
                print(f"case selectionnée {deplacement}")
                # print(f"list mange {list_mvt_mange}")
                # print(f"list deplacement {list_mvt_deplacement}")
                # print(f"list joueur {joueur_qui_joue}")
                # print(f"List adversaire {adversaire}")
            mvt_possible = creer_mvt(list_mvt_deplacement, "XX")
            mvt_mange = creer_mvt(list_mvt_mange, "OO")
            affiche_set(joueur1, joueur2, mvt_possible, mvt_mange)
            piece_avancer = False
            # Tant que le pion n'a pas avancer
            decision = ""
            ambiguite = False
            while not piece_avancer:
                # case_arrivee_x = int(input("case arrivee x "))
                # case_arrivee_y = int(input("case arrivee y "))
                deplacement = demande_case("case arrivee xy")
                case_arrivee_x = int(deplacement[0])
                case_arrivee_y = int(deplacement[1])
                if check_position_piece(case_arrivee_x, case_arrivee_y,
                                        mvt_possible):
                    # Ici il faut ajouter une méthode pour savoir si 2 pieces
                    # identiques peuvent être sur la meme case
                    ambiguite = False
                    if piece == "T" or piece == "C" or piece == "F":
                        index_autre_piece = autre_piece(piece, index_pos,
                                                        joueur_qui_joue)
                        if index_autre_piece >= 0:
                            # On doit regarder l'ensemble des position possible
                            # mais pas celle qui mange car elles ne sont pas
                            # dans la liste mvt_possible
                            mouvement_piece, mange_mouvement_piece = \
                                deplacement_autorise(piece,  joueur_qui_joue[
                                    index_autre_piece][1][0], joueur_qui_joue[
                                    index_autre_piece][1][1], joueur_qui_joue,
                                                     adversaire, id_joueur,
                                                     id_mvt,
                                                     index_pos, prise_passant)
                            if is_double_place(mouvement_piece, case_arrivee_x,
                                               case_arrivee_y) or  \
                                    is_double_place(mange_mouvement_piece,
                                                    case_arrivee_x,
                                                    case_arrivee_y):
                                ambiguite = True
                            else:
                                ambiguite = False
                    joueur_qui_joue[index_pos][1] = \
                        (case_arrivee_x, case_arrivee_y)
                    if piece == 'P':
                        # pion atteint la ligne ennemi et peux se transformer
                        if case_arrivee_x == 0 or case_arrivee_x == 7:
                            choix = chgmt_pion(joueur_qui_joue)
                            decision = piece_choisit(choix)
                            joueur_qui_joue = transforme_pion(joueur_qui_joue,
                                                              index_pos,
                                                              decision)
                        # Erreur de gestion de prise en passant a regarder
                        prise_passant = 'True', [
                            ['P', (case_arrivee_x, case_arrivee_y)]]
                    if piece == 'R':
                        if id_joueur == 0:
                            roi_bouge[0] = True
                        else:
                            roi_bouge[1] = True
                        # Il s'agit d'un petit Roque
                        if abs(case_y - case_arrivee_y > 1) and \
                                case_arrivee_y > case_y:
                            piece, index_pos = name_piece(case_x, 7,
                                                          joueur_qui_joue)
                            joueur_qui_joue[index_pos][1] = (case_x,
                                                             case_y + 1)
                            if id_joueur == 0:
                                tour_bouge[0] = True
                            else:
                                tour_bouge[2] = True
                        # Il s'agit d'un grand rocque
                        if abs(case_y - case_arrivee_y > 1) and \
                                case_arrivee_y < case_y:
                            _, index_pos = name_piece(case_x, 0,
                                                      joueur_qui_joue)
                            joueur_qui_joue[index_pos][1] = (case_x,
                                                             case_y - 1)
                            if id_joueur == 0:
                                tour_bouge[1] = True
                            else:
                                tour_bouge[3] = True
                    piece_avancer = True
                coupj = sauv_deplacement(piece, case_y, case_arrivee_x,
                                         case_arrivee_y, "", ambiguite,
                                         decision)
                if not piece_avancer and \
                        check_position_piece(case_arrivee_x,
                                             case_arrivee_y,
                                             mvt_mange):
                    joueur_qui_joue[index_pos][1] = \
                        (case_arrivee_x, case_arrivee_y)
                    # Coup prise en passant
                    if prise_passant[0] and case_arrivee_x == int(
                            prise_passant[1][0][1][0]) + 1 * id_mvt and  \
                            case_arrivee_y == prise_passant[1][0][1][1]:
                        piece, index_piece_manger = \
                            name_piece(prise_passant[1][0][1][0],
                                       prise_passant[1][0][1][1], adversaire)
                        coupj = sauv_deplacement(piece, case_y,
                                                 case_arrivee_x,
                                                 case_arrivee_y, "x",
                                                 ambiguite,
                                                 "")
                    else:
                        if piece == "T" or piece == "C" or piece == "F":
                            index_autre_piece = autre_piece(piece, index_pos,
                                                            joueur_qui_joue)
                            if index_autre_piece >= 0:
                                # On doit regarder l'ensemble des position
                                # possible
                                piece_x = joueur_qui_joue[
                                    index_autre_piece][1][0]
                                piece_y = joueur_qui_joue[
                                    index_autre_piece][1][1]
                                mouvement_piece, mange_mouvement_piece = \
                                    deplacement_autorise(piece, piece_x,
                                                         piece_y,
                                                         joueur_qui_joue,
                                                         adversaire, id_joueur,
                                                         id_mvt, index_pos,
                                                         prise_passant)
                                if is_double_place(mouvement_piece,
                                                   case_arrivee_x,
                                                   case_arrivee_y) or \
                                        is_double_place(mange_mouvement_piece,
                                                        case_arrivee_x,
                                                        case_arrivee_y):
                                    ambiguite = True
                                else:
                                    ambiguite = False

                        # pion atteint la ligne ennemi et peux se
                        # transformer tout en mangeant
                        if (case_arrivee_x == 0 or case_arrivee_x == 7) and \
                                piece == "P":
                            choix = chgmt_pion(joueur_qui_joue)
                            decision = piece_choisit(choix)
                            joueur_qui_joue = transforme_pion(joueur_qui_joue,
                                                              index_pos,
                                                              decision)
                        coupj = sauv_deplacement(piece, case_y,
                                                 case_arrivee_x,
                                                 case_arrivee_y,
                                                 "x", ambiguite, decision)
                    piecem, index_piece_manger = name_piece(case_arrivee_x,
                                                            case_arrivee_y,
                                                            adversaire)
                    adversaire.pop(index_piece_manger)
                    piece_avancer = True
                if not piece_avancer:
                    print("Vous coordonnées ne sont pas exactes !")
            # On regarde à la fin du coup si on est en echec voir echec et mat
            trouve_roi, index_roi = cherche_roi(adversaire)
            is_echec = []
            if trouve_roi:
                is_echec = echec(adversaire[index_roi][1][0], adversaire[
                    index_roi][1][1], joueur_qui_joue, adversaire,
                                 id_joueur, id_mvt, prise_passant, True)
            if len(is_echec) > 0:
                # ajout du mvt car pas d'echec
                print("ECHEC!!")
                coupj += "+"
                # Ajouter sauvergarde dans le fichier
                # J'inverse ici adversaire et joueur car c'est mon adversaire
                # qui doit protéger son roi
                if id_joueur == 0:
                    if mat(adversaire, joueur_qui_joue, 1, -1, prise_passant):
                        print("echec et MAT!!")
                        gain.append("MAT")
                        gain.append(id_joueur)
                        coupj += "#"
                        jouer = False
                else:
                    if mat(adversaire, joueur_qui_joue, 0, 1, prise_passant):
                        print("echec et MAT!!")
                        gain.append("MAT")
                        gain.append(id_joueur)
                        coupj += "#"
                        jouer = False
            if id_joueur == 0:
                joueur1 = deepcopy(joueur_qui_joue)
                joueur2 = deepcopy(adversaire)
                coupj1 = coupj
                id_joueur = 1
            else:
                joueur2 = deepcopy(joueur_qui_joue)
                joueur1 = deepcopy(adversaire)
                id_joueur = 0
                coupj2 = coupj
                partie.append((joueur_qui_joue, adversaire))
                sauvegarde(nb_coup, coupj1, coupj2)
                nb_coup += 1
            print(f"joueur 1 {joueur1}")
            print(f"joueur 2 {joueur2}")
            affiche_set(joueur1, joueur2, [], [])
    if gain[0] == "PAT":
        fin_jeu("1-1")
    elif gain[1] == 0:
        fin_jeu("1-0")
    else:
        fin_jeu("0-1")
    print("Merci à bientot")
    print(f" {len(partie)}")


if __name__ == '__main__':
    # Doctype with reST Nowadays, the probably more prevalent format is the
    # reStructuredText (reST) format that is used by Sphinx to generate
    # documentation. Note: it is used by default in JetBrains PyCharm
    # (type triple quotes after defining a method and hit enter).
    '''
    help(creer_set)
    help(read_place)
    help(affiche_set)
    help(check_position_piece)
    help(name_piece)
    help(mvt_p)
    help(est_dans_plateau)
    help(cherche_doublon)
    help(mvt_c)
    '''
    chess()
    """
    partie_complete, vainqueur = replay("70coups.txt")
    index_replay = 0
    for coup in partie_complete:
        print(f"j1:{coup[0]}")
        print(f"j2:{coup[1]}")
        print(f"{index_replay} engagement")
        nj1, nj2 = inverse_plateau(coup[0], coup[1])
        affiche_set(nj1, nj2, [], [])
        print("--------------------------------------------")
        index_replay += 1
    print(vainqueur)
    """
