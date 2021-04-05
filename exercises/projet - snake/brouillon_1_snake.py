import tkinter as tk

snake = tk.Tk()
snake.title('jeu snake')

#########VARIABLES#############

WIDTH = 800
HEIGH = 600

#########images##################

parois = tk.PhotoImage(file='muraille_40.gif')
pomme = tk.PhotoImage(file='pomme_40.gif')
tete_serpent = tk.PhotoImage(file='tete_serpent_40.gif')
corps_serpent = tk.PhotoImage(file='corps_serpent_40.gif')

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
            elif case == "S":
                env_jeu.create_image(x, y, image=tete_serpent, anchor="nw")
            x += 40
        x = 0
        y += 40
    niveau.close()

######code#######################


snake.geometry('800x600')

env_jeu = tk.Canvas(snake, width=WIDTH, heigh=HEIGH, bg="darkgray")
env_jeu.place(x=0, y=0)

decors()

snake.mainloop()
