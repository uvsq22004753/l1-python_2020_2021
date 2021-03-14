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
import random as rd
################################################

######CONSTANTES################################
LARGEUR = 500
HAUTEUR = 500
LARGEUR_PARCELLE = 10

################################################

######VARIABLES GLOBALES########################
PCT_FORET = 25
PCT_EAU = 25
PCT_PRAIRIE = 50
LARGEUR = 500
HAUTEUR = 500
parcelle = []
################################################

######FONCTIONS################################
def creer_terrain():
    global LARGEUR, HAUTEUR, parcelle
    parcelle.append([LARGEUR, HAUTEUR])
    duree = 0
    NBR_PARCELLES = ((LARGEUR*HAUTEUR)//(LARGEUR_PARCELLE**2))
    NBR_PRAIRIE = int(PCT_PRAIRIE*NBR_PARCELLES/100)
    NBR_FORET = int(PCT_FORET*NBR_PARCELLES/100)
    NBR_EAU = NBR_PARCELLES - NBR_FORET - NBR_PRAIRIE
    couleurs = ["DeepSkyBlue2" for i in range(NBR_EAU)] + ["green4" for i in range(NBR_FORET)] + ["goldenrod1"   for i in range(NBR_PRAIRIE)]
    rd.shuffle(couleurs)
    terrain.config(height=HAUTEUR, width=LARGEUR)
    for i in range(LARGEUR//LARGEUR_PARCELLE):
        for j in range(HAUTEUR//LARGEUR_PARCELLE):
            color = couleurs.pop()
            id = terrain.create_rectangle((i*LARGEUR_PARCELLE, j*LARGEUR_PARCELLE),
                ((i+1)*LARGEUR_PARCELLE, (j+1)*LARGEUR_PARCELLE), fill=color)
            parcelle.append([id,color,duree,i,j])

def affichetext_prairies():
    global PCT_PRAIRIE
    label_PCT_prairies['text']=svEntry.get()
    PCT_PRAIRIE = int(label_PCT_prairies['text'])

def affichetext_forets():
    global PCT_FORET
    label_PCT_forets['text']=svEntry.get()
    PCT_FORET = int(label_PCT_forets['text'])

def affichetext_eau():
    global PCT_EAU
    label_PCT_eau['text']=svEntry.get()
    PCT_EAU = int(label_PCT_eau['text'])

def affichetext_hauteur():
    global HAUTEUR, LARGEUR
    label_taille_hauteur['text']=svEntry.get()
    HAUTEUR = int(label_taille_hauteur['text'])
    label_nbr_parcelles['text'] = str((LARGEUR*HAUTEUR)//(LARGEUR_PARCELLE**2))

def affichetext_largeur():
    global LARGEUR, HAUTEUR
    label_taille_largeur['text']=svEntry.get()
    LARGEUR = int(label_taille_largeur['text'])
    label_nbr_parcelles['text'] = str((LARGEUR*HAUTEUR)//(LARGEUR_PARCELLE**2))

def sauvegarder():
    global parcelle
    nom_fichier = svEntry.get() + '.txt'
    Fichier = open(nom_fichier, 'w')
    for i in parcelle : 
        txt = ' '.join([str(elem) for elem in i])  
        Fichier.write(txt + '\n')
    Fichier.close()

def charger():
    global HAUTEUR, LARGEUR, parcelle
    color = ''
    nom_fichier = svEntry.get() + '.txt'
    chargement = open(nom_fichier, "r")
    list_chargement = [(line.strip()).split() for line in chargement]
    chargement.close()
    terrain.config(height=int(list_chargement[0][0]), width=int(list_chargement[0][1]))
    HAUTEUR = int(list_chargement[0][1])
    LARGEUR = int(list_chargement[0][0])
    label_taille_hauteur['text']=HAUTEUR
    label_taille_largeur['text']=LARGEUR
    label_nbr_parcelles['text'] = str((LARGEUR*HAUTEUR)//(LARGEUR_PARCELLE**2))
    parcelle.append([LARGEUR,HAUTEUR])
    for i in list_chargement :
        if i != list_chargement[0] : 
            id = terrain.create_rectangle(int(i[3])*LARGEUR_PARCELLE, int(i[4])*LARGEUR_PARCELLE,
                (int(i[3])+1)*LARGEUR_PARCELLE, (int(i[4])+1)*LARGEUR_PARCELLE, fill=i[1])
            parcelle.append([id,i[1],int(i[2]),int(i[3]),int(i[4])])

###############################################

######PROGRAMME PRINCIPAL######################
simulation = tk.Tk()
simulation.title("propagation d'un incendie")
svEntry = tk.StringVar()

terrain = tk.Canvas(simulation, bg="black", height=HAUTEUR, width=LARGEUR)
bouton_creer_terrain = tk.Button(simulation, text="Générer le terrain", bg="NavajoWhite2", command=creer_terrain, width=30)
label_parcelles = tk.Label(simulation, text="PARCELLES : ", bg="NavajoWhite2", width=12, relief="raised")
label_nbr_parcelles = tk.Label(simulation, text=str((LARGEUR*HAUTEUR)//(LARGEUR_PARCELLE**2)), bg="NavajoWhite2", width=10)
bouton_hauteur = tk.Button(simulation, text="HAUTEUR(pixels): ", bg="NavajoWhite2", width=15, command=affichetext_hauteur)
label_taille_hauteur = tk.Label(simulation, text=str(HAUTEUR), bg="NavajoWhite2", width=10)
bouton_largeur = tk.Button(simulation, text="LARGEUR(pixels): ", bg="NavajoWhite2", width=15, command=affichetext_largeur)
label_taille_largeur = tk.Label(simulation, text=str(LARGEUR), bg="NavajoWhite2", width=10)
bouton_prairies = tk.Button(simulation, text="PRAIRIES(%): ", bg="goldenrod1", width=12, command=affichetext_prairies)
label_PCT_prairies = tk.Label(simulation, text=str(PCT_PRAIRIE), bg="goldenrod1", width=10)
bouton_forets = tk.Button(simulation, text="FORETS(%) : ", bg="green4", width=12, command=affichetext_forets)
label_PCT_forets = tk.Label(simulation, text=str(PCT_FORET), bg="green4", width=10)
bouton_eau = tk.Button(simulation, text="EAU(%) : ", bg="DeepSkyBlue2", width=12, command=affichetext_eau)
label_PCT_eau = tk.Label(simulation, text=str(PCT_EAU), bg="DeepSkyBlue2", width=10)
bouton_sauvegarder = tk.Button(simulation, text="sauvegarder le terrain", bg="NavajoWhite2", command=sauvegarder, width=30)
bouton_charger = tk.Button(simulation, text="charger un terrain", bg="NavajoWhite2", command=charger, width=30)
edit = tk.Entry(simulation, textvariable = svEntry, width=30)


terrain.grid(column=1, row=2, columnspan=6, rowspan=24)
bouton_creer_terrain.grid(row=2, column=0)
bouton_largeur.grid(column=1, row=0)
bouton_hauteur.grid(column=1, row=1)
label_taille_hauteur.grid(column=2, row=1)
label_taille_largeur.grid(column=2, row=0)
label_parcelles.grid(column=3, row=0)
bouton_prairies.grid(column=3, row=1)
label_nbr_parcelles.grid(column=4, row=0)
label_PCT_prairies.grid(column=4, row=1)
bouton_forets.grid(column=5, row=0)
bouton_eau.grid(column=5, row=1)
label_PCT_forets.grid(column=6, row=0)
label_PCT_eau.grid(column=6, row=1)
bouton_sauvegarder.grid(column=0, row=3)
bouton_charger.grid(column=0, row=4)
edit.grid(row=0, column=0)

simulation.mainloop()

###############################################