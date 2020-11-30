import tkinter as tk

cible = tk.Tk()
cible.title("cible en couleur")
width, height = 500, 500

label1 = tk.Canvas(cible, bg="black", width = width, height = height)

x = width / 2
y = width / 2
rayon = 0 
couleur = ["blue", "green", "black", "yellow", "magenta", "red"]
couleurs = couleur*10

while 10*rayon < x:
    label1.create_oval(x+(10*rayon)-y, y-(10*rayon)+y, x-(10*rayon)+y, y+(10*rayon)-y, width = 10, outline = couleurs[rayon])
    rayon += 1 
label1.create_oval(x+(10*rayon)-y, y-(10*rayon)+y, x-(10*rayon)+y, y+(10*rayon)-y, width = 10, outline = couleurs[rayon-1])

label1.grid()
cible.mainloop()