import tkinter as tk

est_rouge = 1


def recommencer():
    """Recommence du début"""
    global est_rouge
    canvas.itemconfigure(rectangle, fill="red")
    est_rouge = 1


def change_couleur(event):
    """Change la couleur du rectangle"""
    global est_rouge
    x = event.x
    y = event.y
    if 100 < x < 300 and 100 < y < 300:
        if est_rouge == 1:
            canvas.itemconfigure(rectangle, fill="blue")
        elif est_rouge == 0:
            canvas.itemconfigure(rectangle, fill="red")
        est_rouge = 1 - est_rouge
    else:
        est_rouge = -1


racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=500, height=500)
canvas.grid(row=0)
bouton = tk.Button(racine, text="Recommencer", command=recommencer)
bouton.grid(row=1)
rectangle = canvas.create_rectangle(100, 100, 300, 300, fill="red")
canvas.bind('<Button-1>', change_couleur)
racine.mainloop()
