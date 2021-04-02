import tkinter as tk

snake = tk.Tk()
snake.title('jeu snake')

#########VARIABLES#############

WIDTH = 800
HEIGH = 600

#########images##################

parois = tk.PhotoImage(file='contour.gif')
pomme = tk.PhotoImage(file='pomme4.gif')

############fonctions#############

def decors():
    x, y = 0, 0
    niveau = open('niveau_1.txt')
    for ligne in niveau:
        for i in range(20):
            case = ligne[i]
            if case == "X":
                env_jeu.create_image(x, y, image=parois, anchor="nw")
            elif case == "P":
                env_jeu.create_image(x, y, image=pomme, anchor="nw")
            x += 40
        x = 0
        y += 40
    niveau.close()

######code#######################


snake.geometry('800x600')

env_jeu = tk.Canvas(snake, width=WIDTH, heigh=HEIGH, bg="green")
env_jeu.place(x=0, y=0)

decors()

snake.mainloop()
