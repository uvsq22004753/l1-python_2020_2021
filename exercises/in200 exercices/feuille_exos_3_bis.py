import random as rd
import copy

########### création ou chargement des tableaux #################


def creer_tableau(n):
    """ créer une liste de liste de taille nxn """
    L = [[]for i in range(n-1)]
    L.append([0 for i in range(n-1)])
    L.append(["*" for i in range(n+1)])
    L.append([0 for i in range(n)])
    for i in range(n+2):
        if i != n and i != n+1:
            if i == 0:
                L[i].extend([0 for i in range(n-1)])
            elif 1 <= i <= n-2:
                L[i].append(0)
                L[i].extend([rd.randint(5, 9) for i in range(n-2)])
            L[i].extend([0, "*", 0])
    L_final = somme(L)
    return L_final


def creer_tableau_2():
    choix = input("taper 'nouveau' si vous souhaitez charger un nouveau tableau et taper 'charger' sinon : ")
    if choix == "charger":
        nom_fichier = input("entrer le nom du fichier (ne pas oublier .txt) : ")
        chargement = open(nom_fichier, "r")
        list_chargement = [(line.strip()).split() for line in chargement]
        chargement.close()
        afficher_tableau(list_chargement)
    elif choix == "nouveau":
        n = input("entrer la taille du tableau (un entier) : ")
        tableau = creer_tableau(int(n))
        afficher_tableau(tableau)


def somme(tab):
    for k in range(len(tab)-2):
        for i in range(len(tab)-2):
            tab[len(tab)-1][k] += tab[i][k]
            tab[k][len(tab)-1] += tab[k][i]
    return tab


######### afficher sous forme de tableau ############################


def afficher_tableau(tab):
    """ affiche la liste de liste sous la forme d'un tableau """
    for elem in tab:
        for i in range(len(elem)):
            if i != len(elem)-1:
                if (isinstance(elem[i], int)) and (elem[1] >= 10):
                    print(elem[i], end="  ")
                else:
                    print(elem[i], end="   ")
            else:
                print(elem[i])


########## automate des tas de sable version sequentiel ##############


def etape_sequentiel(tab):
    changement = True
    tab_modif = copy.deepcopy(tab)

    tab_modif[len(tab)-1].clear()
    tab_modif[len(tab)-1] = [0 for i in range(len(tab)-2)]
    for i in range(len(tab)-3):
        tab_modif[i][len(tab)-1] = 0

    for i in range(1, len(tab)-3):
        for k in range(1, len(tab)-3):
            if tab_modif[i][k] >= 4:
                tab_modif[i][k] = tab[i][k] - 4
                tab_modif[i][k-1] += 1
                tab_modif[i][k+1] += 1
                tab_modif[i+1][k] += 1
                tab_modif[i-1][k] += 1

                changement = True
                return [tab_modif, changement]
    return [tab, False]


def automate_sequentiel(tab):
    res = etape_sequentiel(tab)
    while res[1]:
        res = etape_sequentiel(res[0])
    res_vrai = somme(res[0])
    return res_vrai


####### automate des tas de sable version parallele ##########################


def etape_parallele(tab):
    changement = False
    tab_modif = copy.deepcopy(tab)

    tab_modif[len(tab)-1].clear()
    tab_modif[len(tab)-1] = [0 for i in range(len(tab)-2)]
    for i in range(len(tab)-3):
        tab_modif[i][len(tab)-1] = 0

    for i in range(1, len(tab)-3):
        for k in range(1, len(tab)-3):
            if tab_modif[i][k] >= 4:      
                tab_modif[i][k] = tab_modif[i][k] - 4
                tab_modif[i][k-1] += 1
                tab_modif[i][k+1] += 1
                tab_modif[i+1][k] += 1
                tab_modif[i-1][k] += 1

                changement = True
    if changement:
        return [tab_modif, changement]
    else:
        return [tab, changement]

def automate_parallele1(tab):
    nom_fichier = input("entrer le nom du fichier (ne pas oublier .txt) ")
    res = etape_parallele(tab)
    while res[1]:
        res = etape_parallele(res[0])
    res_vrai = somme(res[0])
    Fichier = open(nom_fichier, 'w')
    for elem in res_vrai:
        txt = ' '.join([str(i) for i in elem])
        Fichier.write(txt + '\n')
    Fichier.close()
    return res[0]


def automate_parallele(tab):
    res = etape_parallele(tab)
    while res[1]:
        res = etape_parallele(res[0])
    res_vrai = somme(res[0])
    return res_vrai


############# commandes tests ###################

test = creer_tableau(4)
afficher_tableau(test)
print("------------")
test_para = automate_parallele(test)
afficher_tableau(test_para)
print("--------------")
test_seq = automate_sequentiel(test)
afficher_tableau(test_seq)
