import random as rd
from math import *


def creer_tableau(n):
    """ créer une liste de liste de taille nxn """
    L = [[]for i in range(n)]
    for elem in L:
        elem.append(0)
        elem.extend([rd.randint(5, 9) for i in range(n-1)])
    return L


exe = creer_tableau(4)
print(exe)


def afficher_tableau(tab):
    """ affiche la liste de liste sous la forme d'un tableau """
    for elem in tab:
        for i in range(len(tab)):
            if i != len(tab)-1:
                print(elem[i], end=" ")
            else:
                print(elem[i])


afficher_tableau(exe)


def afficher_tableau_somme(tab):
    """ ajoute la somme de chaque ligne et de chaque colonne au tableau """
    for elem in tab:
        somme = sum(elem)
        print(somme)


afficher_tableau_somme(exe)