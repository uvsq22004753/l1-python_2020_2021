import tkinter as tk  

graphique = tk.Tk()
graphique.title('Khôlle')

def creer_balle(LARGEUR, HAUTEUR):
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canevas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill='red')
    return [cercle, dx, dy]

def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]

def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)

def division(event):
    """ divise le canvas en trois parties égales dans lesquelles bougent des balles"""
    x, y = event.x, event.y
    balles = []
    zone_1 = canevas.create_rectangle(0, 0, x, y, fill='red')
    zone_2 = canevas.create_rectangle(0, y, x, 400, fill='white')
    zone_3 = canevas.create_rectangle(x, 0, 600, y, fill='white')
    zone_4 = canevas.create_rectangle(x,y, 600, 400, fill='red')
    zone = [zone_1, zone_2, zone_3, zone_4]
    for i in zone:
        a, b, c, d = canevas.coords(i)
        if (b==0 and a==0) or (c==600 and d==400): 
            balle_liste = creer_balle(a+(c-a), b+(d-b))
            canevas.itemconfigure(balle_liste[0], fill='white')
            balles.append(balle_liste)
        else: 
            balle_liste = creer_balle(a+(c-a), b+(d-b))
            balles.append(balle_liste)
            

canevas = tk.Canvas(graphique, heigh=400, width=600, bg='black')
canevas.pack()

canevas.bind('<Button-1>', division)

graphique.mainloop()
