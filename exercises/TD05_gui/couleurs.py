import tkinter as tk 

couleur = tk.Tk()
couleur.title("couleurs")

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    

label1 = tk.Button(couleur, text = "Aléatoire", font=("helvetica","16"), fg = "green", bg = "white",padx = 17)
label2 = tk.Button(couleur, text = "Dégradé gris", font=("helvetica","16"), fg = "green", bg = "white",padx = 17)
label3 = tk.Button(couleur, text = "Dégradé 2D", font=("helvetica","16"), fg = "green", bg = "white",padx = 17)
label4 = tk.Canvas(couleur, width = 256, height = 256, bg = "black")

label1.grid(column = 0, row = 1, rowspan = 4)
label2.grid(column = 0, row = 5, rowspan = 4)
label3.grid(column = 0, row = 9, rowspan = 4)
label4.grid(column = 1, row = 1, columnspan = 12, rowspan = 12)

couleur.mainloop()