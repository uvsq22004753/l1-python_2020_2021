import tkinter as tk 
 
dessin = tk.Tk()
dessin.title("Mon dessin")

label1 = tk.Button(dessin, text="Cercle", font=("helvetica","16"))
label2 = tk.Button(dessin, text="Carré", font=("helvetica","16"))
label3 = tk.Button(dessin, text="Croix", font=("helvetica","16"))
label4 = tk.Button(dessin, text="Choisir une couleur", font=("helvetica","16"))
label5 = tk.Canvas(dessin, bg="black", width = 500, height = 500)

label1.grid(column = 0, row = 1, rowspan = 4)
label2.grid(column = 0, row = 5, rowspan = 4)
label3.grid(column = 0, row = 9, rowspan = 4)
label4.grid(column = 1, row = 0, columnspan = 12)
label5.grid(column = 1, row = 1, columnspan = 12, rowspan = 12)

dessin.mainloop()

