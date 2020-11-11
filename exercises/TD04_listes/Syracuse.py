def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    valeurs_suite_syracuse = []
    while n != 1:
        valeurs_suite_syracuse += [n]
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3 + 1
    valeurs_suite_syracuse.append(1.0)
    return (valeurs_suite_syracuse)


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    test = True
    iteration = 1
    while iteration <= n_max and test:
        test = syracuse(iteration)[len(syracuse(iteration))-1] == 1
        iteration += 1
    return test

print(testeConjecture(10))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [len(syracuse(n))-1 for n in range(1, n_max + 1)]


def max_tempsVolListe(n_max):
    return max(tempsVolListe(n_max)), tempsVolListe(n_max).index(max(tempsVolListe(n_max))) + 1


def altitude_maximale(n_max):
    """renvoie l'entier compris entre 1 et n_max ayant la plus grande altitude maximale"""
    altitude_maximale_n = [max(syracuse(i)) for i in range(1, n_max + 1)]
    return max(altitude_maximale_n), altitude_maximale_n.index(max(altitude_maximale_n)) + 1
