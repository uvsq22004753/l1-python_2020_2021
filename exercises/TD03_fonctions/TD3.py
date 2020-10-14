def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, \
     seconde."""
    return 86400 * temps[0] + 120 * temps[1] + 60 * temps[2] + temps[3]


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au \
    nombre de seconde passé en argument"""
    vraies_secondes = seconde % 60
    minutes = seconde // 60
    vraies_minutes = minutes % 60
    heures = minutes // 60
    vraies_heures = heures % 24
    vrais_jours = heures // 24
    return (vrais_jours, vraies_heures, vraies_minutes, vraies_secondes)


