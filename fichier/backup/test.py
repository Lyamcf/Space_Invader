from tkinter import *
from random import randrange

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

logo = PhotoImage(file="téléchargement (2).png")

for i in range(5):
    centre= (randrange(SIDE),randrange(SIDE))
    cnv.create_image(centre, image=logo)

root.mainloop()