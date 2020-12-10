import tkinter as tk 

clic = tk.Tk()
clic.title("exercice 6")

def Coordonnees(event):
    x = event.x
    y = event.y
    if x < 250 : 
        return label1.create_oval((x-25,y+25),(x+25,y-25), fill="blue")
    else : 
        return label1.create_oval((x-25,y+25),(x+25,y-25), fill="red")

label1 = tk.Canvas(clic, heigh=500, width=500, bg="black")
ligne = label1.create_line((250,0),(250,500), fill="white")
label1.bind("<Button-1>", Coordonnees)

label1.grid()

clic.mainloop()