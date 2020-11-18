carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]


carre_pas_mag = carre_mag.copy()
for i in range(0, len(carre_pas_mag)):
    if 3 in carre_pas_mag[i]:
        carre_pas_mag[i][carre_pas_mag[i].index(3)] = 7
print(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si \
    toutes les lignes ont la même somme, et -1 sinon """
    sum_ligne = sum(carre[0])
    for i in range(1, len(carre)):
        if sum(carre[i]) != sum_ligne:
            sum_ligne = -1
            break
    return sum_ligne

