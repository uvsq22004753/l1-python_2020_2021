import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = CANVAS_WIDTH / 2
y = 100 
y1 = CANVAS_HEIGHT - 100
canvas.create_line(x0, y, x0, y1)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x0 - 50, y1 + 50, x0 + 50, y1 - 50)
canvas.create_oval(x0 + 50, (y + y1) / 2 - 50, x0 - 50, (y + y1) / 2 + 50)
    
# Fin de votre code

canvas.grid()
root.mainloop()