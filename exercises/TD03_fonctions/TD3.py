
import sys
import time


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde du temps donné comme \
    (jours, heures, minutes, secondes)."""
    return 86400 * temps[0] + 3600 * temps[1] + 60 * temps[2] + temps[3]


def secondeEnTemps(seconde):
    """on donne un temps en seconde et la fonction renvoie un tuple \
    (jours, heures, minutes, secondes)"""
    vraies_secondes = seconde % 60
    minutes = seconde // 60
    vraies_minutes = minutes % 60
    heures = minutes // 60
    vraies_heures = heures % 24
    vraies_jours = heures // 24
    return (vraies_jours, vraies_heures, vraies_minutes, vraies_secondes)


def afficheTemps(temps):
    """" renvoie le tuple sous la forme d'une chaîne de caractère"""
    valeurs = ["jour", "heure", "minute", "seconde"]
    affichage = " "
    for i, j in zip(temps, valeurs):
        if i == 1:
            affichage = affichage + str(i) + " " + j + " "
        elif i > 1:
            affichage = affichage + str(i) + " " + j + 's' + " "
    print(affichage)


def demandeTemps():
    """ demande à l'utilisateur de rentrer un temps et sort un tuple \
    (jours, heures, minutes, secondes). Si les valeurs sont mal rentrées, \
    renvoie d'un message d'erreur"""
    donnees = []
    demande = 0
    consigne = ("jours", "heures", "minutes", "secondes")
    for i, j in zip(range(0, 4), consigne):
        phrase_consigne = "entrer un nombre de" + " " + j
        demande = int(input(phrase_consigne))
        if (i == 0 and demande >= 0) or (i == 1 and 0 <= demande < 24) \
            or (i == 2 and 0 <= demande < 60) \
                or (i == 3 and 0 <= demande < 60):
            donnees += [demande]
        else:
            sys.exit("erreur de saisie")
    return tuple(donnees)


def demandeTemps2():
    """ demande à l'utilisateur de rentrer un temps et sort un tuple\
     (jours, heures, minutes, secondes). Si les valeurs sont mal rentrées, \
     redemande à l'utilisateur de les rentrer"""
    donnees = []
    demande = 0
    consigne = ("jours", "heures", "minutes", "secondes")
    for i, j in zip(range(0, 4), consigne):
        phrase_consigne = "entrer un nombre de" + " " + j
        demande = int(input(phrase_consigne))
        while not ((i == 0 and demande >= 0) or (i == 1 and 0 <= demande < 24)\
            or (i == 2 and 0 <= demande < 60) \
                or (i == 3 and 0 <= demande < 60)):
            demande = int(input(phrase_consigne))
        donnees += [demande]
    return tuple(donnees)


def sommeTemps(temps1, temps2):
    """ additionne deux temps et renvoie un tuple"""
    somme_temps = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(somme_temps)


def proportionTemps(temps, proportion):
    """ renvoie la proportion d'un temps sous la forme d'un tuple"""
    temps_seconde = tempsEnSeconde(temps)
    temps_proportionné_seconde = temps_seconde * proportion
    return secondeEnTemps(temps_proportionné_seconde)


def tempsEnDate(temps):
    """ donne la date sous la forme \
    (année, jours, heures, minutes, secondes)"""
    annee = temps[0] // 365
    jours = temps[0] % 365
    return (1970 + annee, jours + 1, temps[1], temps[2], temps[3])


def afficheDate(date):
    """affiche la date selon ce modèle : jours mois années \
    heures minutes secondes"""
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",\
            "août", "septembre", "octobre", "novembre", "décembre"]
    jours_mois = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    valeurs = ["heure", "minute", "seconde"]
    affichage = " "
    for i in range(0, len(jours_mois) + 1):
        if i == 0 and date[1] <= jours_mois[1]:
            affichage = affichage + str(date[1]) + " " + mois[i] + " " + str(date[0]) + " "
        elif i > 0 and jours_mois[i - 1] < date[1] <= jours_mois[i]:
            affichage = affichage + str(date[1]-jours_mois[i-1]) + " " + mois[i] + " " + str(date[0]) + " "
    for i, j in zip(date[2:], valeurs):
        if i == 1:
            affichage = affichage + str(i) + " " + j + " "
        elif i > 1:
            affichage = affichage + str(i) + " " + j + 's' + " "

    print(affichage)


def bisextile(jours):
    """affiche toutes les années bissextiles entre 1970 et \
    1970 plus un nombre de jours donné"""
    annee = 1970 + (jours // 365)
    annee_bisextile = []
    for i in range(1970, annee + 1):
        if (int(i) % 4 == 0) and (int(i) % 100 != 0 or (int(i) % 100 == 0 and int(i) % 400 == 0)):
            annee_bisextile += [i]
    return annee_bisextile


def nombreBisextile(jour):
    """compte le nombre d'années bissextiles"""
    return len(bisextile(jour))


def tempsEnDateBisextile(temps):
    """ donne la date sous la forme (année, jours, heures, minutes, secondes)\
     en prenant en compte les années bissextiles """
    annee = (temps[0] - nombreBisextile(temps[0])) // 365
    jours = (temps[0] - nombreBisextile(temps[0])) % 365
    return (1970 + annee, jours + 1, temps[1], temps[2], temps[3])


def afficheDate2(date=tempsEnDateBisextile(secondeEnTemps(int(time.time())))):
    """affiche la date en temps réel selon ce modèle :\
     jours mois années heures minutes secondes"""
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",\
            "août", "septembre", "octobre", "novembre", "décembre"]
    jours_mois = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    valeurs = ["heure", "minute", "seconde"]
    affichage = " "
    for i in range(0, len(jours_mois) + 1):
        if i == 0 and date[1] <= jours_mois[1]:
            affichage = affichage + str(date[1]) + " " + mois[i] + " " + str(date[0]) + " "
        elif i > 0 and jours_mois[i - 1] < date[1] <= jours_mois[i]:
            affichage = affichage + str(date[1]-jours_mois[i-1]) + " " + mois[i] + " " + str(date[0]) + " "
    for i, j in zip(date[2:], valeurs):
        if i == 1:
            affichage = affichage + str(i) + " " + j + " "
        elif i > 1:
            affichage = affichage + str(i) + " " + j + 's' + " "

    print(affichage)
