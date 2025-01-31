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
from tkinter import *
import random as rd
################################################

######CONSTANTES################################
ratioHauteur = 0.8
largeurCanvas = 500
hauteurCanvas = 500
nbParcellesLargeur = 50
nbParcellesHauteur = 50
largeurParcelle = min(largeurCanvas/nbParcellesLargeur,hauteurCanvas/nbParcellesHauteur)
hauteurParcelle = min(largeurCanvas/nbParcellesLargeur,hauteurCanvas/nbParcellesHauteur)
decalageX = (largeurCanvas-nbParcellesLargeur*largeurParcelle)/2
decalageY = (hauteurCanvas-nbParcellesHauteur*hauteurParcelle)/2
couleurs = ["green","yellow","blue"]
poidsForet = 20
poidsPrairie = 100
poidsEau = 20
casesModif = []
nouvellesCasesFeu = []
casesNoires = []
dureeFeu = 1
dureeCendre = 0
id = 0
fonte = ("TkDefaultFont",16)
################################################

######VARIABLES GLOBALES########################
simulation = False
nbParcellesFeu = 0
vitesseSimulation = 10
nbCasesPrairie = 0
nbCasesForet = 0
nbCasesEau = 0
nbCasesCH = 0
nbCasesCE = 0
listeCouleurs = []
cases = []
################################################

######FONCTIONS################################
def creation() : 
    global cases, nbCasesPrairie, nbCasesForet, nbCasesEau, nbCasesCH, nbCasesCE, nbParcellesFeu, casesNoires, casesModif
    cases[:] = []
    casesNoires[:] = []
    casesModif[:] = []
    listeCouleurs.clear()
    nbCasesPrairie, nbCasesForet, nbCasesEau = 0, 0, 0
    for n in range(0,nbParcellesLargeur*nbParcellesHauteur):
        i = n // nbParcellesLargeur
        j = n % nbParcellesLargeur
        couleur = rd.choices(couleurs,[poidsForet,poidsPrairie,poidsEau])[0]
        listeCouleurs.append(couleur)
        duree = 0
        id = c.create_rectangle(j*largeurParcelle+decalageX,i*hauteurParcelle+decalageY,j*largeurParcelle+largeurParcelle+decalageX,i*hauteurParcelle+hauteurParcelle+decalageY,fill=couleur,width=0)
        cases.append([id,couleur,duree,i,j])
    #c.create_text(j*hauteurParcelle+hauteurParcelle/2,i*largeurParcelle+largeurParcelle/2,text=(id))
    nbCasesPrairie = listeCouleurs.count("yellow")
    nbCasesForet = listeCouleurs.count("green")
    nbCasesEau = listeCouleurs.count("blue")
    nbCasesCH, nbCasesCE, nbParcellesFeu = 0, 0, 0
    majLabels()


def afficheCarre(carre):
    for i in carre:
        for j in i:
            print('{:^10}'.format(j),end='')
        print("\n")


def modif():
    c.itemconfigure(1,fill="black")


def AllumerClic(event):
    x, y = event.x, event.y
    source = c.find_closest(x,y)[0]
    #bruler(source)
    #print("ID:",source)
    for i in range(0,len(cases)):
        if cases[i][0] == source:
            bruler(i)
            return
   

def bruler(index):
    global nbParcellesFeu, nbCasesPrairie, nbCasesForet
    if cases[index][1] != "red" and cases[index][1] != "blue":
        if cases[index][1] == "yellow":
            nbCasesPrairie -= 1
        elif cases[index][1] == "green":
            nbCasesForet -= 1
        elif cases[index][1] == "grey":
            nbCasesCH -= 1
        else:
            nbCasesCE -= 1
        c.itemconfig(cases[index][0],fill="red")
        cases[index][1] = "red"
        cases[index][2] = dureeFeu
        nbParcellesFeu += 1
        casesModif.append(index)
        majLabels()

    
def simuler():
    #Changement de couleur des cases avec duree = 0
    global nbParcellesFeu, nbCasesCH, nbCasesCE
    for i in casesModif:
        cases[i][2] -= 1   
        #Propagation du feu
        if cases[i][1] == "red":
            colonne = i % nbParcellesLargeur
            casesVoisines = [i-1,i+1,i-nbParcellesLargeur,i+nbParcellesLargeur]
            #print("i=",i,"colonne=",colonne,casesVoisines)
            for x in casesVoisines:
                if (x >= 0 and x < nbParcellesLargeur*nbParcellesHauteur and x not in nouvellesCasesFeu and
                not (colonne == 0 and x==i-1) and not (colonne == nbParcellesLargeur-1 and x==i+1)):
                    if cases[x][1] == "yellow":
                        nouvellesCasesFeu.append(x)
                    if cases[x][1] == "green":
                        if rd.random() < 0.1:
                            nouvellesCasesFeu.append(x)

        if cases[i][2] <= 0:
            if cases[i][1] == "red":
                cases[i][1] = "grey"
                cases[i][2] = dureeCendre
                c.itemconfig(cases[i][0],fill="grey")
                nbCasesCH += 1
                nbParcellesFeu -= 1
                #print(i,"devient gris")
            else:
                nbCasesCH -= 1
                nbCasesCE += 1
                cases[i][1] = "black"
                c.itemconfig(cases[i][0],fill="black")
                casesNoires.append(i)
    #Les cases noires deviennent inertes
    for i in casesNoires:
        casesModif.remove(i)
    casesNoires.clear()

    for i in nouvellesCasesFeu:
        bruler(i)
    nouvellesCasesFeu.clear()
    #afficheCarre(cases)
    majLabels()


def majLabels():
    labelPrairie.config(text="Prairie: "+str('{: >6}'.format(nbCasesPrairie)))
    labelForet.config(text="Forêt: "+str('{: >6}'.format(nbCasesForet)))
    labelEau.config(text="Eau: "+str('{: >6}'.format(nbCasesEau)))
    labelNbCasesFeu.config(text=format("Feu : "+str('{: >4}'.format(nbParcellesFeu))))
    labelCendresChaudes.config(text="Cendres chaudes: "+str('{: >6}'.format(nbCasesCH)))
    labelCendresEteintes.config(text="Cendres éteintes: "+str('{: >6}'.format(nbCasesCE)))


def activerSimulationAuto():
    global simulation
    simulation = not simulation
    simulerAuto()


def simulerAuto():
    global simulation
    if simulation:
        if nbParcellesFeu:
            simuler()
            fen.after(int(1.0/vitesseSimulation*1000),simulerAuto)
        else:
            simulation = False
        

def augmenterVitesse():
    global vitesseSimulation
    vitesseSimulation += 1
    labelVitesseSim.config(text=format("Etapes / seconde: "+str(vitesseSimulation)))


def baisserVitesse():
    global vitesseSimulation
    if vitesseSimulation > 1:
        vitesseSimulation -= 1
        labelVitesseSim.config(text=format("Etapes / seconde: "+str(vitesseSimulation)))


def sauvegarder():
    global cases, nbCasesPrairie, nbCasesForet, nbCasesEau, nbCasesCH, nbCasesCE, nbParcellesFeu, casesNoires, casesModif, nouvellesCasesFeu
    cases.extend([[nbCasesPrairie, nbCasesForet, nbCasesEau, nbCasesCH, nbCasesCE, nbParcellesFeu], casesNoires, casesModif, nouvellesCasesFeu])
    nom_fichier = svEntry.get() + '.txt'
    Fichier = open(nom_fichier, 'w')
    for i in cases : 
        txt = ' '.join([str(elem) for elem in i])  
        Fichier.write(txt + '\n')
    Fichier.close()


def charger():
    global cases, nbCasesPrairie, nbCasesForet, nbCasesEau, nbCasesCH, nbCasesCE, nbParcellesFeu, casesNoires, casesModif, nouvellesCasesFeu
    cases[:] = []
    casesNoires[:] = []
    casesModif[:] = []
    nouvellesCasesFeu[:] = []
    nom_fichier = svEntry.get() + '.txt'
    chargement = open(nom_fichier, "r")
    list_chargement = [(line.strip()).split() for line in chargement]
    chargement.close()
    for i in list_chargement :
        if i == list_chargement[len(list_chargement)-4] :
            nbCasesPrairie = int(list_chargement[len(list_chargement)-4][0])
            nbCasesForet = int(list_chargement[len(list_chargement)-4][1])
            nbCasesEau = int(list_chargement[len(list_chargement)-4][2])
            nbParcellesFeu = int(list_chargement[len(list_chargement)-4][5])
            nbCasesCH = int(list_chargement[len(list_chargement)-4][3])
            nbCasesCE = int(list_chargement[len(list_chargement)-4][4])
            majLabels()
        elif i == list_chargement[len(list_chargement)-2] : 
            casesModif = [int(elem) for elem in i ]
        elif i == list_chargement[len(list_chargement)-3] :
            casesNoires = [int(elem) for elem in i]
        elif i == list_chargement[len(list_chargement)-1] :
            nouvellesCasesFeu = [int(elem) for elem in i]
        else : 
            id = c.create_rectangle(int(i[4])*largeurParcelle+decalageX, int(i[3])*hauteurParcelle+decalageY,
                (int(i[4]))*largeurParcelle+largeurParcelle+decalageX, (int(i[3]))*hauteurParcelle+hauteurParcelle+decalageY, fill=i[1], width=0)
            cases.append([id,i[1],int(i[2]),int(i[3]),int(i[4])])

###############################################

######PROGRAMME PRINCIPAL######################
fen = Tk()
svEntry = StringVar()
fen.title('simulation incendie')

c = Canvas(fen,width=largeurCanvas,height=hauteurCanvas,bg="white")
bouton = Button(fen,text="Simuler (1 étape)",command=simuler,font=fonte)
boutonSimAuto = Button(text="Simulation automatique",command=activerSimulationAuto,font=fonte)
labelNbCases = Label(fen,text=format("Parcelles : "+str(nbParcellesLargeur*nbParcellesHauteur)),font=fonte)
labelNbCasesFeu = Label(fen,text=format("Feu : "+str('{: >4}'.format(nbParcellesFeu))),bg="red",fg="white",font=fonte)
labelPrairie = Label(fen,text="Prairie: ",bg="yellow",font=fonte)
labelForet = Label(fen,text="Forêt: ",bg="green",fg="white",font=fonte)
labelEau = Label(fen,text="Eau: ",bg="blue",fg="white",font=fonte)
labelCendresChaudes = Label(fen,text="Cendres chaudes: "+str('{: >6}'.format(nbCasesCH)),bg="grey",fg="white",font=fonte)
labelCendresEteintes = Label(fen,text="Cendres éteintes: "+str('{: >6}'.format(nbCasesCE)),bg="black",fg="white",font=fonte)
labelVitesseSim = Label(fen,text=format("Etapes / seconde: "+str(vitesseSimulation)),font=fonte)
bouton_sauvegarder = Button(simulation, text="sauvegarder le terrain", command=sauvegarder,bg="purple",fg="white",font=fonte)
bouton_charger = Button(simulation, text="charger un terrain", bg="purple",fg="white",font=fonte, command=charger)
bouton_terrain = Button(fen, text="créer terrain", bg="purple",fg="white",font=fonte, command=creation)
edit = Entry(simulation, textvariable = svEntry, width=30)

c.grid(row=5,column=0,columnspan=3,rowspan=2)
bouton.grid(row=0,column=3)
boutonSimAuto.grid(row=1,column=3)
labelNbCases.grid(row=0,column=0)
labelNbCasesFeu.grid(row=0,column=2)
labelPrairie.grid(row=0,column=1)
labelForet.grid(row=1,column=1)
labelEau.grid(row=2,column=1)
labelCendresChaudes.grid(row=1,column=2)
labelCendresEteintes.grid(row=2,column=2)
labelVitesseSim.grid(row=2,column=3)
bouton_sauvegarder.grid(column=0, row=2)
bouton_charger.grid(column=0, row=3)
edit.grid(row=1, column=0)
bouton_terrain.grid(column=0,row=4)

fen.bind('<space>',lambda e:simuler())
fen.bind('<Right>',lambda e:augmenterVitesse())
fen.bind('<Left>',lambda e:baisserVitesse())
c.bind('<Button-1>',AllumerClic)

fen.mainloop()
###############################################