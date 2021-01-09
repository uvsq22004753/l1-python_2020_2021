import tkinter as tk 

clic = tk.Tk()
clic.title("exercice 6")

nb_clic = 0
clic_x = []
clic_y = []

def Coordonnees(event):
    global nb_cliq, clic_x, clic_y
    clic_x.append(event.x)
    clic_y.append(event.y)
    if nb_clic != 2 and nb_clic != 4 :
        nb_clic +=1 
    elif nb_clic == 2: 
        nb_clic +=1
        return canvas.create_line(clic_x[0],clic_y[0],clic_x[1],clic_y[1], fill="green")
    elif nb_clic == 4 :  
        nb_clic +=1
        return canvas.create_line(clic_x[2],clic_y[2],clic_x[3],clic_y[3], fill="yellow")

label1 = tk.Canvas(clic, heigh=500, width=500, bg="black")
ligne = label1.create_line((250,0),(250,500), fill="white")
label1.bind("<Button-1>", Coordonnees)

label1.grid()

clic.mainloop()