import tkinter as tk
import random as rd 

dessin = tk.Tk()
dessin.title("Mon dessin")

choix = "blue"

def Cercle():
    x = rd.randint(55,445)
    y = rd.randint(55,445)
    return label5.create_oval(x-50,y+50,x+50,y-50, fill= choix)

def Carre():
    x = rd.randint(10,400)
    y = rd.randint(10,400)
    return label5.create_rectangle(x,y,x+100,y+100, fill = choix)

def Croix():
    x = rd.randint(10,400)
    y = rd.randint(10,400)
    return label5.create_line(x,y,x+90,y+90, fill = choix, width = 10), label5.create_line(x+90,y,x,y+90, fill = choix, width = 10)

def Couleur():
    global choix 
    choix = input("choisir une couleur entre white, black, red, green, blue, cyan, yellow")
    return choix

label1 = tk.Button(dessin, text="Cercle", font=("helvetica","16"), fg = "green", bg = "white",padx = 17, command = Cercle)
label2 = tk.Button(dessin, text="Carré", font=("helvetica","16"), fg = "green", bg = "white",padx = 20, command = Carre)
label3 = tk.Button(dessin, text="Croix", font=("helvetica","16"), fg = "green", bg = "white",padx = 22, command = Croix)
label4 = tk.Button(dessin, text="Choisir une couleur", font=("helvetica","16"), fg = "green", bg = "white", command = Couleur)
label5 = tk.Canvas(dessin, bg="black", width = 500, height = 500, relief = "groove", borderwidth = 10)

label1.grid(column = 0, row = 1, rowspan = 4)
label2.grid(column = 0, row = 5, rowspan = 4)
label3.grid(column = 0, row = 9, rowspan = 4)
label4.grid(column = 1, row = 0, columnspan = 12)
label5.grid(column = 1, row = 1, columnspan = 12, rowspan = 12)

dessin.mainloop()

