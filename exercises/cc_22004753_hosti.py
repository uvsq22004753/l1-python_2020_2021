import tkinter as tk
import random as rd

dessin = tk.Tk()
dessin.title("Mon dessin")

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

nb_clic = 1
clic_x = []
clic_y = []
objects = []

def Coordonnees(event):
    global nb_clic, clic_x, clic_y, objects 
    clic_x.append(event.x)
    clic_y.append(event.y)
    if nb_clic != 2 and nb_clic != 4 :
        nb_clic +=1 
    elif nb_clic == 2: 
        nb_clic +=1
        ligne_1 = canvas.create_line(clic_x[0],clic_y[0],clic_x[1],clic_y[1], fill="green", width=5)
        objects.append(ligne_1)
        return ligne_1 
    elif nb_clic == 4 :  
        nb_clic +=1
        ligne_2 = canvas.create_line(clic_x[2],clic_y[2],clic_x[3],clic_y[3], fill="yellow", width=5)
        objects.append(ligne_2)
        return ligne_2
    elif nb_clic > 4 : 
        dessin.destroy()
        objects = []
        clic_x = []
        clic_y = []
        nb_clic = 1

canvas = tk.Canvas(dessin, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="black")
bouton_1 = tk.Button(dessin,text="Pause", font=("helvetica","16"), fg="green", bg="white")
canvas.bind("<Button-1>", Coordonnees)

bouton_1.grid(column=0, row = 0, columnspan = 6)
canvas.grid()
dessin.mainloop()