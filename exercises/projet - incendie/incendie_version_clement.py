from tkinter import *
import random


def afficheCarre(carre):
    for i in carre:
        for j in i:
            print('{:^10}'.format(j),end='')
        print("\n")


def modif():
    c.itemconfigure(1,fill="black")


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def AllumerClic(event):
    x, y = event.x, event.y
    source = c.find_closest(x,y)[0]
    #bruler(source)
    #print("ID:",source)
    for i in range(0,len(cases)):
        if cases[i][0] == source:
            print("Index:",i)
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
    #print(casesModif)
    #Changement de couleur des cases avec duree = 0
    global nbParcellesFeu, nbCasesCH, nbCasesCE
    print(len(casesModif))
    print("casesModif:",casesModif)
    print("casesNoires",casesNoires)
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
                        if random.random() < 0.1:
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


ratioHauteur = 0.8
largeurCanvas = 700
hauteurCanvas = 700
nbParcellesLargeur = 50
nbParcellesHauteur = 50
largeurParcelle = min(largeurCanvas/nbParcellesLargeur,hauteurCanvas/nbParcellesHauteur)
hauteurParcelle = min(largeurCanvas/nbParcellesLargeur,hauteurCanvas/nbParcellesHauteur)
decalageX = (largeurCanvas-nbParcellesLargeur*largeurParcelle)/2
decalageY = (hauteurCanvas-nbParcellesHauteur*hauteurParcelle)/2
print(decalageX,decalageY)
couleurs = ["green","yellow","blue"]
couleursPerso = [get_color(130,200,80),get_color(230,230,100),get_color(0,200,240)]
poidsForet = 20
poidsPrairie = 100
poidsEau = 20
casesModif = []
nouvellesCasesFeu = []
casesNoires = []
dureeFeu = 1
dureeCendre = 0
id = 0
global nbParcellesFeu
global simulation
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
fonte = ("TkDefaultFont",16)

fen = Tk()



fen.title("test")
fen.bind('<space>',lambda e:simuler())
c = Canvas(fen,width=largeurCanvas,height=hauteurCanvas,bg="white")
c.bind('<Button-1>',AllumerClic)
fen.bind('<Right>',lambda e:augmenterVitesse())
fen.bind('<Left>',lambda e:baisserVitesse())
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

labelNbCases.grid(row=0,column=0)
labelNbCasesFeu.grid(row=0,column=2)
labelPrairie.grid(row=0,column=1)
labelForet.grid(row=1,column=1)
labelEau.grid(row=2,column=1)
labelCendresChaudes.grid(row=1,column=2)
labelCendresEteintes.grid(row=2,column=2)

c.grid(row=4,column=0,columnspan=3,rowspan=2)
bouton.grid(row=0,column=3)
boutonSimAuto.grid(row=1,column=3)
labelVitesseSim.grid(row=2,column=3)

for n in range(0,nbParcellesLargeur*nbParcellesHauteur):
    i = n // nbParcellesLargeur
    j = n % nbParcellesLargeur
    couleur = random.choices(couleurs,[poidsForet,poidsPrairie,poidsEau])[0]
    listeCouleurs.append(couleur)
    duree = 0
    id = c.create_rectangle(j*largeurParcelle+decalageX,i*hauteurParcelle+decalageY,j*largeurParcelle+largeurParcelle+decalageX,i*hauteurParcelle+hauteurParcelle+decalageY,fill=couleur,width=0)
    cases.append([id,couleur,duree,i,j])
    #c.create_text(j*hauteurParcelle+hauteurParcelle/2,i*largeurParcelle+largeurParcelle/2,text=(id))
nbCasesPrairie = listeCouleurs.count("yellow")
nbCasesForet = listeCouleurs.count("green")
nbCasesEau = listeCouleurs.count("blue")
labelPrairie.config(text="Prairie: "+str('{: >6}'.format(nbCasesPrairie)))
labelForet.config(text="Forêt: "+str('{: >6}'.format(nbCasesForet)))
labelEau.config(text="Eau: "+str('{: >6}'.format(nbCasesEau)))
print(nbCasesEau)
i,j = 0,0
#print("i,j",j*hauteurParcelle,i*largeurParcelle,j*hauteurParcelle+hauteurParcelle,i*largeurParcelle+largeurParcelle)
#print(cases)
#afficheCarre(cases)
#print(c.find_all())


#afficheCarre(cases)


fen.mainloop()