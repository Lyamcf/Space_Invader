from tkinter import*
from random import*
Mafenetre= Tk()
score=0
coin=0
yAJ =600
xAJ= 450
pasy = 5
yAB=-50
bg = PhotoImage(file = 'fond.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="ennemi.png")
laser = PhotoImage(file="Laser-PNG-Image.png")
titre=PhotoImage(file="pngegg (2).png")
insert=PhotoImage(file="insert.gif")


def jouer():    
    bouton.destroy()
    canevas.destroy()
    canvas1.place(x=25,y=25)
    bouge_avion_enemie(randint(25,875),yAB)
        
def icoin():
    global coin
    coin+=1
def bouge_avion(evt):
    global xAJ,yAJ
    if evt.keysym=="s" :
        yAJ+=40
    if evt.keysym=="z" :
        yAJ-=40
    if evt.keysym=="d" :
        xAJ+=40
    if evt.keysym=="q" :
        xAJ-=40

    if evt.keysym=="e" :

        mouvement_balle(xAJ,yAJ)

    canvas1.coords(avion_joueur,xAJ,yAJ)
def bouge_avion_enemie(xAB,yAB):
    yAB+=2


    canvas1.coords(avion_enemie,xAB,yAB)

    canvas1.after(10,bouge_avion_enemie,xAB,yAB,)
def mouvement_balle (xB,yB):



    yB-=5


    canvas1.coords(balle,xB,yB)

    canvas1.after(10,mouvement_balle,xB,yB,)

Mafenetre.geometry("900x900")
Mafenetre.title("world war2 v.2")
canvas1 = Canvas( Mafenetre, width = 850,height = 850)
canevas = Canvas( Mafenetre, width = 850,height = 850)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")



entry=Entry(canevas,width=34)
canevas = Canvas( Mafenetre, width = 850,height = 850)
bouton=Button(Mafenetre,text="inser frrr",command=jouer)
canevas.place(x=0,y=0)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
bouton.place(x=380,y=520)


canevas.create_image( 0, 0, image = bg,anchor = "nw")
canevas.create_image( 430, 300, image = titre)
canevas.create_image( 430, 600, image =insert)
#canvas1.pack(fill = "both", expand = True)
balle=canvas1.create_image(xAJ,yAJ,image=laser)
avion_joueur =canvas1.create_image(xAJ,yAJ,image=avion1img)
avion_enemie =canvas1.create_image(xAJ,yAJ,image=avion2img)


Mafenetre.bind_all("<Key>",bouge_avion)
Mafenetre.mainloop() 