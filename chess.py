__authors__ = ("Clara Correia", "Laurie Behloul")
__contact__ = ("clara.correia.sne@gmail.com", "lauriebehloul1@gmail.com")
__version__ = "1.0.0"
__date__ = "2020"

from datetime import datetime

roi_bouge = [False, False]
tour_bouge = [False, True, False, False]
pion_bouge = False


def creer_set(version):
    """
    Permet de generer differente situations de plateau
    :param version: int, represente different plateau
    :return: un plateau

    >>>creer_set(3)
    >>>([['P', (1, 0)]], [['P', (2, 1)], ['P', (2, 2)]], [])
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
        j1 = [['P', (1, 1)]]
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
    return j1, j2, []


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

    >>>read_place(1,1,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],
    [['OO', (0, 0)]])
    >>>' P1 '

    >>>read_place(1,0,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],
    [['OO', (0, 0)]])
    >>>' P2 '

    >>>read_place(0,1,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],
    [['OO', (0, 0)]])
    >>>' XX '

    >>>read_place(0,0,[['P', (1, 1)]],[['P', (1, 0)]], [['XX', (0, 1)]],
    [['OO', (0, 0)]])
    >>>' OO '
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
    print('   A0   B1   C2   D3   E4   F5   G6    H7')
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
    print('   A0   B1   C2   D3   E4   F5   G6    H7')


def check_position(x, y, joueur):
    """
    Permet de verifier si une piece est
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :return:True si il y a une pieces et False si il n'y en a pas

    >>>check_position(1,1,[['P', (1, 0)]])
    >>>False

    >>>check_position(1, 0, [['P', (1, 0)]])
    >>>True
    """
    for e in joueur:
        if e[1] == (x, y):
            return True
    return False


def name_piece(x, y, joueur):
    """
    Permet de savoir quel pieces est dans la case
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :return:tuple, nom de la pieces et son index dans le tableau du joueur

    >>>name_piece(0,0,[['R', (0, 3)], ['T', (0, 0)]])
    >>>('T', 1)
    """
    i = 0
    for e in joueur:
        if e[1] == (x, y):
            return e[0], i
        i += 1


def mvt_p(x, y, joueur, adversaire, id_joueur, prise_passant):
    """
    Permet de lister les mouvements des pions
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :param joueur: list, tableau de pieces d'un joueur
    :param adversaire:list, tableau de pieces de l'autre joueur
    :param id_joueur:int, permet de savoir si le joueur est en haut ou en bas
    :param prise_passant:List,indique si on est en situation de prise en
    passant.
    :return: mvt_pion, mvt_pion_mange (list, list):tableau des mouvement
    possibles, tableau des pieces pouvant etre mange par le pion.

    >>> mvt_p(1, 3, ['P', [1, 3], ...], ['P', [6, 1], ...], 1)
    >>> [(2, 3), (3, 3)] []

    """

    mvt_pion = []
    mvt_pion_mange = []
    # Deplacement pour manger du pion
    if est_dans_plateau(x + 1 * id_joueur, y - 1):
        if check_position(x + 1 * id_joueur, y - 1, adversaire):
            mvt_pion_mange.append((x + 1 * id_joueur, y - 1))
    if est_dans_plateau(x + 1 * id_joueur, y + 1):
        if check_position(x + 1 * id_joueur, y + 1, adversaire):
            mvt_pion_mange.append((x + 1 * id_joueur, y + 1))
    # Cas particulier de la prise en passant
    if prise_passant[0]:
        if check_position(x, y + 1, prise_passant[1]):
            mvt_pion_mange.append((x + 1 * id_joueur, y + 1))
        if check_position(x, y - 1, prise_passant[1]):
            mvt_pion_mange.append((x + 1 * id_joueur, y - 1))
    # Deplacement du pion pour avancer
    if not check_position(x + 1 * id_joueur, y, joueur):
        mvt_pion.append((x + 1 * id_joueur, y))
        if x == 1 or x == 6:
            if not check_position(x + 2 * id_joueur, y, joueur):
                mvt_pion.append((x + 2 * id_joueur, y))
    return mvt_pion, mvt_pion_mange


def est_dans_plateau(x, y):
    """
    Permet de verifier si la piece est dans le plateau
    :param x:int, index d'un tableau (lignes)
    :param y:int, index du tableau (colonnes)
    :return:True si la piece est dans le plateau et False sinon

    >>>est_dans_plateau(1,1)
    >>>True

    >>>est_dans_plateau(-1,0)
    >>>False
    """
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False


def cherche_doublon(mouvement, mouvement_mange):
    """
    Permet de savoir si une case est a la fois dans le tableau mange et/ou mvt
    :param mouvement:list, tableau des mouvements possibles propre a une piece
    :param mouvement_mange:list, tableau des mouvements possibles pour
    manger une piece de l'adversaire
    :return:list, tableau des coo de la case etant dans les 2 cases cite
    precedemment

    >>>cherche_doublon([(1,0), (0,0)], [(0,0)],)
    >>>[1]
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


def mvt_c(x, y, joueur, adversaire):
    """

    :param x:
    :param y:
    :param joueur:
    :param adversaire:
    :return:
    """
    mvt_cavalier = []
    for i in range(1, 3):
        for j in range(1, 3):
            mvtx = (-1)**i
            mvty = (-1)**j
            if est_dans_plateau(x + mvtx, y + 2 * mvty) and not \
                    check_position(x + mvtx, y + 2 * mvty, joueur):
                mvt_cavalier.append((x + mvtx, y + 2 * mvty))
            if est_dans_plateau(x + 2 * mvtx, y + mvty) and not \
                    check_position(x + 2 * mvtx, y + mvty, joueur):
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

    return mvt_cavalier, mvt_cavalier_mange


def mvt_mange_list(mvt, adversaire):
    """
    Permet de creer un tableau avec les pieces mange
    :param mvt:list, tableau des mouvement possibles par une pieces
    :param adversaire:list, tableau
    :return:list, tableau contenant les coo des pieces pouvant etre mange

    >>>mvt_mange_list([['P', (1, 0)], ['P', (1, 1)]],[['P', (1, 1)], ['P',
    (1, 2)]])
    >>>[]
    """
    mvt_mange = []
    for e in mvt:
        for f in adversaire:
            if e == f[1]:
                mvt_mange.append(f[1])
    return mvt_mange


def mvt_r(x, y, joueur, adversaire, id_joueur):
    """

    :param x:
    :param y:
    :param joueur:
    :param adversaire:
    :param id_joueur:
    :return:
    """
    mvt_roi = []
    mvt_roi_mange = []
    if id_joueur == -1:
        roi_r = roi_bouge[0]
        tour_pr = tour_bouge[2]
        tour_gr = tour_bouge[3]
    else:
        roi_r = roi_bouge[1]
        tour_pr = tour_bouge[0]
        tour_gr = tour_bouge[1]
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            # Test our supprimer le déplacement (0,0) pas de déplacement ;-)
            if (i, j) != (0, 0):
                if est_dans_plateau(x + i, y + j) \
                        and not check_position(x + i, y + j, joueur):
                    mvt_roi.append((x + i, y + j))
    # roque
        # Petit Rocque
        if not roi_r and not tour_pr:
            pas_de_piece_pr = True
            for idx_roi in range(1, 3):
                pas_de_piece_pr = pas_de_piece_pr \
                    or check_position(x, y-idx_roi, joueur) \
                    or check_position(x, y-idx_roi, adversaire)
            if pas_de_piece_pr:
                mvt_roi.append((x, y - 2))
        # Grand rocque
        if not roi_r and not tour_gr:
            pas_de_piece_gr = True
            for idx_roi in range(1, 4):
                pas_de_piece_gr = pas_de_piece_gr \
                    or check_position(x, y + idx_roi, joueur) \
                    or check_position(x, y + idx_roi, adversaire)
            if pas_de_piece_gr:
                mvt_roi.append((x, y + 3))
        mvt_roi_mange = mvt_mange_list(mvt_roi, adversaire)
        # On supprimme des mouvements autorises les mouvments mange
        doublon = cherche_doublon(mvt_roi, mvt_roi_mange)
        if len(doublon) > 0:
            for index in doublon:
                mvt_roi.pop(index)
    return mvt_roi, mvt_roi_mange


def mvt_t(x, y, joueur, adversaire):
    """

    :param x:
    :param y:
    :param joueur:
    :param adversaire:
    :return:
    """
    mvt_tour_temp = []
    mange_tour_temp = []
    # Je regarde sur l'axe horizontal
    for i in range(8):
        # On ne regarde pas notre position
        if (x, y) != (x, i):
            # Regarde si je suis sur une piece de mon adversaire
            if check_position(x, i, adversaire):
                if i < y:
                    mange_tour_temp = [(x, i)]
                    # espace libre entre deux pieces a supprimer
                    mvt_tour_temp = []
                # Si je suis à droite de la piece je stoppe ma recherche
                else:
                    mange_tour_temp.append((x, i))
                    break
            # Regarde si je suis ne suis pas sur une de mes pieces
            elif not check_position(x, i, joueur):
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
    mvt_tour = mvt_tour_temp
    mange_tour = mange_tour_temp
    mvt_tour_temp = []
    mange_tour_temp = []
    # Je regarde sur l'axe vertical
    for i in range(8):
        # On ne regarde pas notre position
        if (x, y) != (i, y):
            # Regarde si je suis sur une piece de mon adversaire
            if check_position(i, y, adversaire):
                if i < x:
                    mange_tour_temp = [(i, y)]
                    # espace libre entre deux pieces a supprimer
                    mvt_tour_temp = []
                # Si je suis à droite de la piece je stoppe ma recherche
                else:
                    mange_tour_temp.append((i, y))
                    break
            # Regarde si je suis ne suis pas sur une de mes pieces
            elif not check_position(i, y, joueur):
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
    mvt_tour += mvt_tour_temp
    mange_tour += mange_tour_temp
    return mvt_tour, mange_tour


def mvt_f(x, y, joueur, adversaire):
    """

    :param x:
    :param y:
    :param joueur:
    :param adversaire:
    :return:
    """
    mvt_fou_temp = []
    mange_fou_temp = []
    for i in range(-8, 8):
        if est_dans_plateau(x + i, y - i) and (x + i, y - i) != (x, y):
            # On trouve une piece adverse que l'on peut manger
            if check_position(x + i, y - i, adversaire):
                if x + i < x:
                    mange_fou_temp = [(x + i, y - i)]
                    mvt_fou_temp = []
                else:
                    mange_fou_temp.append((x + i, y - i))
                    break
            # On est sur une case vide pas adversaire ni joueur
            elif not check_position(x + i, y - i, joueur):
                mvt_fou_temp.append((x + i, y - i))
            # On est sur une case joueur si on est sur la droite du plateau
            # on arrete, sinon on vide les mouvements précédent
            else:
                if (x + i) > x:
                    break
                else:
                    mvt_fou_temp = []
    mvt_fou = mvt_fou_temp
    mange_fou = mange_fou_temp
    mvt_fou_temp = []
    mange_fou_temp = []
    for i in range(-8, 8):
        if est_dans_plateau(x + i, y + i) and (x + i, y + i) != (x, y):
            if check_position(x + i, y + i, adversaire):
                if y + i < y:
                    mange_fou_temp = [(x + i, y + i)]
                    mvt_fou_temp = []
                else:
                    mange_fou_temp.append((x + i, y + i))
                    break
            elif not check_position(x + i, y + i, joueur):
                mvt_fou_temp.append((x + i, y + i))
            elif (y + i) > y:
                break
            else:
                mvt_fou_temp = []
    mvt_fou += mvt_fou_temp
    mange_fou += mange_fou_temp
    return mvt_fou, mange_fou


def mvt_d(x, y, joueur, adversaire):
    """

    :param x:
    :param y:
    :param joueur:
    :param adversaire:
    :return:
    """
    mvt_dame_t = mvt_t(x, y, joueur, adversaire)
    mvt_dame_f = mvt_f(x, y, joueur, adversaire)
    return mvt_dame_t[0] + mvt_dame_f[0], mvt_dame_t[1] + mvt_dame_f[1]


def creer_mvt(list_mvt, dessin):
    """
    Permet de visualiseerr les mouvement des pieces
    :param list_mvt:list, tableau
    :param dessin: str, XX pour position de mvt et OO pour mange
    :return:
    """
    retour_list = []
    for e in list_mvt:
        retour_list.append((dessin, e))
    return retour_list


def init_sauvegarde(name, site, nb_jeu, white_name, black_name, typej1,
                    typej2):
    """

    :param name:
    :param site:
    :param nb_jeu:
    :param white_name:
    :param black_name:
    :param typej1:
    :param typej2:
    :return:
    """
    fichier = open("data.txt", "w")
    fichier.write(f'[Event "{name}"] \n')
    fichier.write(f'[Site "{site}" ] \n')
    t = datetime.now()
    fichier.write(f'Date "{t.strftime("%Y.%m.%d")}" ]\n')
    fichier.write(f'[Round "{nb_jeu}" ]\n')
    fichier.write(f'[White "{white_name}" ]\n')
    fichier.write(f'[Black "{black_name}"]\n')
    fichier.write(f'[Time_begin "{t.strftime("%H:%M:%S")}"]\n')
    fichier.write(f'[WhiteType: "{typej1}]"\n')
    fichier.write(f'[BlackType: "{typej2}]"\n\n')
    fichier.close()


def sauvegarde(nbcoup, coupj1, coupj2, echec, mat):
    """

    :param nbcoup:
    :param coupj1:
    :param coupj2:
    :param echec:
    :param mat:
    :return:
    """
    fichier = open("data.txt", "a")
    print(f"NB COUPS :{nbcoup}")
    print(f"coup 1 :{coupj1}")
    print(f"coup 2 :{coupj2}")
    fichier.write(f"{nbcoup}. {coupj1} {coupj2} ")
    if nbcoup % 5 == 0 and nbcoup != 0:
        fichier.write("\n")
    fichier.close()


def fin_jeu(result):
    """
    :param result:
    :return:
    :example:
    >>> fin_jeu("1-0")
    >>> # le fichier est modifier en ajoutant l'heure de fin et le résultat

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
    fichier.write(f"{result}")
    fichier.close()


def demande_case(texte):
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


def sauv_deplacement(piece, pos_init_x, pos_init_y, pos_x, pos_y, mange,
                     ambigu):
    # colonne = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    colonne = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    sauv_piece = ""
    rocque = False
    deplacement = ""
    if piece == 'P':
        sauv_piece = ""
    elif piece == 'T':
        sauv_piece = "R"
    elif piece == 'C':
        sauv_piece = "N"
    elif piece == 'F':
        sauv_piece = "B"
    elif piece == 'R':
        print(f"Rocque ? {pos_y - pos_init_y}")
        if abs(pos_init_y - pos_y) == 2:
            deplacement = "O-O"
            rocque = True
        elif abs(pos_init_y - pos_y) == 3:
            deplacement = "O-O-O"
            rocque = True
        else:
            sauv_piece = "K"
    elif piece == 'D':
        sauv_piece = "Q"
    if mange == "x" and piece == "P":
        mange = colonne[pos_init_y] + mange
    if not rocque:
        if ambigu:
            deplacement = str(sauv_piece + colonne[pos_init_y] + mange + \
                                                              colonne[pos_y] +
                                                   str(pos_x + 1))
        else:
            deplacement = str(
                sauv_piece + mange + colonne[pos_y] + str(pos_x + 1))
    return deplacement


def deplacement_autorise(piece, case_x, case_y, joueur_qui_joue, adversaire,
                         id_mvt, prise_en_passant):
    ret_list_mvt_deplacement = []
    ret_list_mvt_mange = []
    if piece == 'P':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_p(case_x, case_y,
                                                     joueur_qui_joue,
                                                     adversaire, id_mvt,
                                                     prise_en_passant)
    elif piece == 'T':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_t(case_x, case_y,
                                                     joueur_qui_joue,
                                                     adversaire)
    elif piece == 'C':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_c(case_x, case_y,
                                                     joueur_qui_joue,
                                                     adversaire)
    elif piece == 'F':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_f(case_x, case_y,
                                                     joueur_qui_joue,
                                                     adversaire)
    elif piece == 'R':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_r(case_x, case_y,
                                                     joueur_qui_joue,
                                                     adversaire, id_mvt)
    elif piece == 'D':
        ret_list_mvt_deplacement, ret_list_mvt_mange = mvt_d(case_x, case_y,
                                                     joueur_qui_joue,
                                                     adversaire)
    return ret_list_mvt_deplacement, ret_list_mvt_mange


def autre_piece(piece, index_position, joueur):
    index = 0
    for e in joueur:
        if e[0] == piece:
            if index_position != index:
                return index
        index += 1
    return -1


def double_place(mouvement_piece, case_arrivee_x,
                                        case_arrivee_y):
    for e in mouvement_piece[0]:
        x,y = e
        if x == case_arrivee_x and y == case_arrivee_y:
            return True
    return False


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
    prise_en_passant = 'False', [['P', (0, 0)]]
    coupj = ""
    coupj1 = ""
    while jouer:
        if id_joueur == 0:
            id_mvt = 1
            joueur_qui_joue = joueur1
            adversaire = joueur2
        else:
            id_mvt = -1
            joueur_qui_joue = joueur2
            adversaire = joueur1
        click_ok = False
        print(f"Joueur {id_joueur + 1} c'est à vous")
        piece = ""
        index_position = 0
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
            if check_position(case_x, case_y, joueur_qui_joue):
                piece, index_position = name_piece(case_x, case_y,
                                                   joueur_qui_joue)
                list_mvt_deplacement, list_mvt_mange = deplacement_autorise(
                    piece, case_x, case_y, joueur_qui_joue, adversaire,
                              id_mvt, prise_en_passant)
                click_ok = True
            if not click_ok:
                if case_x == -1 and case_y == -1:
                    click_ok = True
                    jouer = False
                else:
                    print("Vous coordonnées ne sont pas exactes !")
            print(f"list mange {deplacement}")
            print(f"list mange {list_mvt_mange}")
            print(f"list deplacement {list_mvt_deplacement}")
            print(f"list joueur {joueur_qui_joue}")
            print(f"List adversaire {adversaire}")
        mvt_possible = creer_mvt(list_mvt_deplacement, "XX")
        mvt_mange = creer_mvt(list_mvt_mange, "OO")
        affiche_set(joueur1, joueur2, mvt_possible, mvt_mange)
        piece_avancer = False
        while not piece_avancer:
            # case_arrivee_x = int(input("case arrivee x "))
            # case_arrivee_y = int(input("case arrivee y "))
            deplacement = demande_case("case arrivee xy")
            case_arrivee_x = int(deplacement[0])
            case_arrivee_y = int(deplacement[1])
            if check_position(case_arrivee_x, case_arrivee_y, mvt_possible):
                # Ici il faut ajouter une méthode pour savoir si 2 pieces
                # identiques peuvent être su la meme case
                ambiguite = False
                if piece == "T" or piece == "C" or piece == "F":
                    index_autre_piece = autre_piece(piece, index_position,
                                                    joueur_qui_joue)
                    if index_autre_piece >= 0:
                        # On doit regarder l'ensemble des position possible
                        mouvement_piece = deplacement_autorise(piece,
                                    joueur_qui_joue[index_autre_piece][1][0],
                                    joueur_qui_joue[index_autre_piece][1][1],
                                    joueur_qui_joue,
                                    adversaire,
                                    id_mvt,
                                    "")
                        if double_place(mouvement_piece, case_arrivee_x,
                                        case_arrivee_y):
                            ambiguite = True
                        else:
                            ambiguite = False
                coupj = sauv_deplacement(piece, case_x, case_y,
                                         case_arrivee_x,
                                         case_arrivee_y, "", ambiguite)
                joueur_qui_joue[index_position][1] = (
                case_arrivee_x, case_arrivee_y)
                if piece == 'P':
                    prise_en_passant = 'True', [
                        ['P', (case_arrivee_x, case_arrivee_y)]]
                if piece == 'R':
                    # Il s'agit d'un petit Rocque
                    if abs(case_y - case_arrivee_y > 1) and case_arrivee_y >\
                            case_y:
                        piece, index_position = name_piece(case_x, 7,
                                                           joueur_qui_joue)
                        joueur_qui_joue[index_position][1] = (case_x,
                                                              case_y + 1)
                    # Il s'agit d'un grand rocque
                    if abs(case_y - case_arrivee_y > 1) and case_arrivee_y <\
                            case_y:
                        piece, index_position = name_piece(case_x, 0,
                                                           joueur_qui_joue)
                        joueur_qui_joue[index_position][1] = \
                            (case_x, case_y - 1)
                piece_avancer = True
            ambiguite = False
            if not piece_avancer and check_position(case_arrivee_x,
                                                    case_arrivee_y, mvt_mange):
                joueur_qui_joue[index_position][1] = \
                    (case_arrivee_x, case_arrivee_y)
                if prise_en_passant[0] and case_arrivee_x == int(
                        prise_en_passant[1][0][1][0]) + 1 * id_mvt and  \
                        case_arrivee_y == prise_en_passant[1][0][1][1]:
                    piece, index_piece_manger = \
                        name_piece(prise_en_passant[1][0][1][0],
                                   prise_en_passant[1][0][1][1], adversaire)
                    print(f"chess prise en passant")
                    coupj = sauv_deplacement(piece, case_x, case_y,
                                             case_arrivee_x,
                                             case_arrivee_y, "x", ambiguite)
                else:
                    if piece == "T" or piece == "C" or piece == "F":
                        index_autre_piece = autre_piece(piece, index_position,
                                                        joueur_qui_joue)
                        if index_autre_piece >= 0:
                            # On doit regarder l'ensemble des position possible
                            mouvement_piece = deplacement_autorise(piece,
                                                                   joueur_qui_joue[
                                                                       index_autre_piece][
                                                                       1][0],
                                                                   joueur_qui_joue[
                                                                       index_autre_piece][
                                                                       1][1],
                                                                   joueur_qui_joue,
                                                                   adversaire,
                                                                   id_mvt, "")
                            if double_place(mouvement_piece, case_arrivee_x,
                                            case_arrivee_y):
                                ambiguite = True
                            else:
                                ambiguite = False
                    coupj = sauv_deplacement(piece, case_x, case_y,
                                             case_arrivee_x,
                                             case_arrivee_y, "x", ambiguite)
                piecem, index_piece_manger = name_piece(case_arrivee_x,
                                                        case_arrivee_y,
                                                        adversaire)
                adversaire.pop(index_piece_manger)
                piece_avancer = True
            if not piece_avancer:
                print("Vous coordonnées ne sont pas exactes !")
        if id_joueur == 0:
            joueur1 = joueur_qui_joue
            joueur2 = adversaire
            coupj1 = coupj
            id_joueur = 1
        else:
            id_mvt = -1
            joueur2 = joueur_qui_joue
            joueur1 = adversaire
            id_joueur = 0
            coupj2 = coupj
            sauvegarde(nb_coup, coupj1, coupj2, 'N', 'N')
        affiche_set(joueur1, joueur2, [], [])
        if id_joueur == 0:
            # jouer_encore = input("On continue ? O/N")
            jouer_encore = 'O'
            nb_coup += 1
            if jouer_encore == 'N':
                jouer = False
    fin_jeu("1-1")
    print("Merci à bientot")


if __name__ == '__main__':
    # Doctype with reST Nowadays, the probably more prevalent format is the
    # reStructuredText (reST) format that is used by Sphinx to generate
    # documentation. Note: it is used by default in JetBrains PyCharm
    # (type triple quotes after defining a method and hit enter).
    help(creer_set)
    help(read_place)
    help(affiche_set)
    help(check_position)
    help(name_piece)
    help(mvt_p)
    help(est_dans_plateau)
    help(cherche_doublon)
    help(mvt_c)
    chess()
