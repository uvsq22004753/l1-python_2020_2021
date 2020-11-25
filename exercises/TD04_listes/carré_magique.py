carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]


carre_pas_mag = carre_mag.copy()
for i in range(0, len(carre_pas_mag)):
    if 3 in carre_pas_mag[i]:
        carre_pas_mag[i][carre_pas_mag[i].index(3)] = 7
print(carre_pas_mag)

import numpy as np
def afficheCarre(carre):
    """la fonction permet d'afficher les listes deux dimensions sous forme de carrés"""
    return np.array(carre)

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si \
    toutes les lignes ont la même somme, et -1 sinon """
    sum_ligne = sum(carre[0])
    for i in range(1, len(carre)):
        if sum(carre[i]) != sum_ligne:
            sum_ligne = -1
            break
    return sum_ligne


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si\
         toutes les colonnes ont la même somme, et -1 sinon """
    carre_par_colonne = [[], [], [], []]
    for i in range(0, len(carre)):
        carre_par_colonne[i].extend([carre[0][i], carre[1][i], carre[2][i], carre[3][i]])

    sum_colonne = sum(carre_par_colonne[0])
    for i in range(1, len(carre)):
        if sum(carre_par_colonne[i]) != sum_colonne:
            sum_colonne = -1
            break
    return sum_colonne


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si \
        les 2 diagonales ont la même somme, et -1 sinon """
    carre_par_diagonale = [[], []]
    for i in range(0, len(carre)):
        carre_par_diagonale[0].append(carre[i][i])
        carre_par_diagonale[1].append(carre[i][-(i+1)])
    sum_diagonale = sum(carre_par_diagonale[0])
    for i in range(1, len(carre_par_diagonale)):
        if sum(carre_par_diagonale[i]) != sum_diagonale:
            sum_diagonale = -1
            break
    return sum_diagonale


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testDiagonalesEgales(carre) == testColonnesEgales(carre) == \
            testLignesEgales(carre) and testLignesEgales(carre) != -1:
        return True
    else:
        return False


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille
        du carré, et False sinon """
    liste_valeurs = [i for i in range(1, (len(carre)**2) + 1)]
    for i in range(0, len(carre)):
        for j in range(0, len(carre)):
            if carre[i][j] in liste_valeurs:
                liste_valeurs.remove(carre[i][j])
            else:
                return False
    if liste_valeurs == []:
        return True
    else:
        return False
