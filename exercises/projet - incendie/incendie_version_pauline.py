#########################
# Groupe de TD:
# groupe LDDBI 
# Auteurs:
# Pauline HOSTI
# Rania SAIFI
# Adeline MOUTOU
# Clément MAOUCHE
# Maya SANTINI
# Nathan CARRE
# Adresse du dépôt GitHub:
# https://github.com/Nathan-Carre/projet_incendie
################################################

######LIBRAIRIES################################
import tkinter as tk
import random
################################################

######CONSTANTES################################
LARGEUR = 400
HAUTEUR = 300
################################################

######VARIABLES GLOBALES########################
################################################

######FONCTIONS################################
###############################################

######PROGRAMME PRINCIPAL######################
simulation = tk.Tk()
simulation.title("propagation d'un incendie")

terrain = tk.Canvas(simulation, bg="NavajoWhite2", height=HAUTEUR, width=LARGEUR)
bouton_creer_terrain = tk.Button(simulation, text="Générer le terrain", bg="peachpuff2")

terrain.grid(column=1, row=0)
bouton_creer_terrain.grid(column=0,row=0)

simulation.mainloop()

###############################################