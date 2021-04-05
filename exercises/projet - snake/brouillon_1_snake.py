import tkinter as tk

snake = tk.Tk()
snake.title('jeu snake')

#########VARIABLES#############

WIDTH = 800
HEIGH = 600

############fonctions#############


def decors():
    x, y = 0, 0
    niveau = open('niveau_1.txt')
    for ligne in niveau:
        for i in range(20):
            case = ligne[i]
            if case == "X":
                env_jeu.create_rectangle(x, y, x+40, y+40, fill='black')
            elif case == "P":
                env_jeu.create_rectangle(x, y, x+40, y+40, fill='red')
            elif case == "S":
                env_jeu.create_rectangle(x, y, x+40, y+40, fill='green')
            x += 40
        x = 0
        y += 40
    niveau.close()

######code#######################


snake.geometry('800x600')

env_jeu = tk.Canvas(snake, width=WIDTH, heigh=HEIGH, bg="olive drab")
env_jeu.place(x=0, y=0)

decors()

snake.mainloop()
