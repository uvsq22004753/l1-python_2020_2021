import tkinter as tk
import random as rd

dessin = tk.Tk()
dessin.title("Mon dessin")

choix = "blue"
objets = []

def Cercle():
    global objets
    x = rd.randint(55, 445)
    y = rd.randint(55, 445)
    cercle = label5.create_oval(x-50, y+50, x+50, y-50, fill=choix)
    objets.append(cercle)
    return cercle


def Carre():
    global objets
    x = rd.randint(10, 400)
    y = rd.randint(10, 400)
    carre = label5.create_rectangle(x, y, x+100, y+100, fill=choix)
    objets.append(carre)
    return carre


def Croix():
    global objets
    x = rd.randint(10, 400)
    y = rd.randint(10, 400)
    croix1 = label5.create_line(x, y, x+90, y+90, fill=choix, width=10)
    croix2 = label5.create_line(x+90, y, x, y+90, fill=choix, width = 10)
    objets.extend([croix1,croix2])
    return croix1, croix2


def Couleur():
    global choix
    choix = input("choisir une couleur entre white, black, red, green, blue, cyan, yellow")
    return choix


def Undo():
    global objets
    if objets == []:
        pass
    else : 
        supprimer = objets.pop()
        if label5.type(supprimer) == 'line':
            supprimer2 = objets.pop()
            label5.delete(supprimer)
            label5.delete(supprimer2)
        else :
            label5.delete(supprimer)

label1 = tk.Button(dessin, text="Cercle", font=("helvetica","16"), fg = "green", bg = "white",padx = 17, command = Cercle)
label2 = tk.Button(dessin, text="Carré", font=("helvetica","16"), fg = "green", bg = "white",padx = 20, command = Carre)
label3 = tk.Button(dessin, text="Croix", font=("helvetica","16"), fg = "green", bg = "white",padx = 22, command = Croix)
label4 = tk.Button(dessin, text="Choisir une couleur", font=("helvetica","16"), fg = "green", bg = "white", command = Couleur)
label6 = tk.Button(dessin, text="Undo", font=("helvetica","16"), fg = "green", bg = "white", command = Undo)
label5 = tk.Canvas(dessin, bg="black", width=500, height=500, relief="groove", borderwidth=10)

label1.grid(column = 0, row = 1, rowspan = 4)
label2.grid(column = 0, row = 5, rowspan = 4)
label3.grid(column = 0, row = 9, rowspan = 4)
label4.grid(column = 1, row = 0, columnspan = 8)
label6.grid(column = 8, row = 0, columnspan = 8)
label5.grid(column = 1, row = 1, columnspan = 12, rowspan = 12)

dessin.mainloop()