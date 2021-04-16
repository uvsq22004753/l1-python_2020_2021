import tkinter as tk

snake = tk.Tk()
snake.title('jeu snake')

WIDTH = 800
HEIGH = 600

parois = tk.PhotoImage(file='muraille_40.gif')
pomme = tk.PhotoImage(file='pomme_40.gif')
tete_serpent_gauche = tk.PhotoImage(file='tete_serpent_gauche_40.gif')
tete_serpent_droite = tk.PhotoImage(file='tete_serpent_droite_40.gif')
tete_serpent_haut = tk.PhotoImage(file='tete_serpent_haut_40.gif')
tete_serpent_bas = tk.PhotoImage(file='tete_serpent_bas_40.gif')
corps_lateral = tk.PhotoImage(file='corps_lateral_40.gif')
corps_vertical = tk.PhotoImage(file='corps_vertical_40.gif')
queue_serpent_gauche = tk.PhotoImage(file='queue_serpent_gauche_40.gif')
queue_serpent_droite = tk.PhotoImage(file='queue_serpent_droite_40.gif')
queue_serpent_haut = tk.PhotoImage(file='queue_serpent_haute_40.gif')
queue_serpent_bas = tk.PhotoImage(file='queue_serpent_bas_40.gif')
tournant_droit_bas = tk.PhotoImage(file='tournant_droit_bas_40.gif')
tournant_gauche_bas = tk.PhotoImage(file='tournant_gauche_bas_40.gif')
tournant_droit_haut = tk.PhotoImage(file='tournant_droite_haut_40.gif') 
tournant_gauche_haut = tk.PhotoImage(file='tournant_gauche_haut_40.gif')


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
            elif case == "T":
                env_jeu.create_image(x, y, image=tete_serpent_gauche, anchor="nw")
            elif case == "Q":
                env_jeu.create_image(x, y, image=queue_serpent_gauche, anchor="nw")
            x += 40
        x = 0
        y += 40
    niveau.close()


snake.geometry('800x600')

env_jeu = tk.Canvas(snake, width=WIDTH, heigh=HEIGH, bg="darkgray")
env_jeu.place(x=0, y=0)

decors()

snake.mainloop()
