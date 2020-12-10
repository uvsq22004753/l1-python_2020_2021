import tkinter as tk 

clic = tk.Tk()
clic.title("exercice 6")

def Coordonnees(event):
    x = event.x
    y = event.y
    return label1.create_line((x,y),((x+1),y), fill="red")

label1 = tk.Canvas(clic, heigh=500, width=500, bg="black")
label1.create_line((250,0),(250,500), fill="white")
label1.bind("<Button-1>", Coordonnees)

label1.grid()

clic.mainloop()

