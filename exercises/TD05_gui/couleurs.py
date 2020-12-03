import tkinter as tk 
import random as rd 

couleur = tk.Tk()
couleur.title("couleurs")

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def ecran_aleatoire():
    couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]
    for i in range(256):
        for j in range(256):
            draw_pixel(i, j, couleurs[rd.randint(0,5)])

def degrade_gris():
    for i in range(256):
        for j in range(256):
                draw_pixel(i, j, get_color(i,i,i))

def degrade_2D():
    for i in range(256):
        for j in range(256):
                draw_pixel(i, j, get_color(i,0,j))

label1 = tk.Button(couleur, text = "Aléatoire", font=("helvetica","16"), fg = "green", bg = "white",padx = 17, command = ecran_aleatoire)
label2 = tk.Button(couleur, text = "Dégradé gris", font=("helvetica","16"), fg = "green", bg = "white",padx = 17, command = degrade_gris)
label3 = tk.Button(couleur, text = "Dégradé 2D", font=("helvetica","16"), fg = "green", bg = "white",padx = 17, command = degrade_2D)
label4 = tk.Canvas(couleur, width = 255, height = 255, bg = "black")

label1.grid(column = 0, row = 1, rowspan = 4)
label2.grid(column = 0, row = 5, rowspan = 4)
label3.grid(column = 0, row = 9, rowspan = 4)
label4.grid(column = 1, row = 1, columnspan = 12, rowspan = 12)

def draw_pixel(i, j, color):
    return label4.create_line((i,j),((i+1),j), fill = color)

couleur.mainloop()