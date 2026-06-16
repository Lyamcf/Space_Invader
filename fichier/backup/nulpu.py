from tkinter import*
from random import*
import time
Mafenetre= Tk()
score=0
coin=0
yAJ =600
xAJ= 450
pasy = 5
yAB=-50
n=0
nbcoin = 0
bg = PhotoImage(file = 'fond.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="ennemi.png")
laser = PhotoImage(file="Laser-PNG-Image.png")
titre=PhotoImage(file="pngegg (2).png")
insert=PhotoImage(file="insert.gif")
canvas1 = Canvas( Mafenetre, width = 850,height = 850)
canevas = Canvas( Mafenetre, width = 850,height = 850)


def jouer():
    JOUER.destroy()
    canevas.destroy()
    canvas1.place(x=25,y=25)
    bouge_avion_enemie(randint(25,875),yAB)
def bouge_avion(evt):
    global xAJ,yAJ, n
    if evt.keysym=="s" :
        yAJ+=40
    if evt.keysym=="z" :
        yAJ-=40
    if evt.keysym=="d" :
        xAJ+=40
    if evt.keysym=="q" :
        xAJ-=40

    canvas1.coords(avion_joueur,xAJ,yAJ)
    
def tire_balle(evt):
    global xAJ,yAJ, n
    if evt.keysym=="e" :
        n+=1
        n=canvas1.create_image(xAJ,yAJ,image=laser)
        mouvement_laser(xAJ,yAJ,n)
    
def bouge_avion_enemie(xAB,yAB):
    global n
    
    yAB+=2
    canvas1.coords(avion_enemie,xAB,yAB)    
    canvas1.after(10,bouge_avion_enemie,xAB,yAB,)
    if canvas1.coords(n,xB,yB) > canvas1.coords(avion_enemie,xAB,yAB -10)  and canvas1.coords(n,xB,yB) > canvas1.coords(avion_enemie,xAB,yAB +10) and
        
def mouvement_laser (xB,yB,n):       
    yB-=5
    canvas1.coords(n,xB,yB)
    canvas1.after(10,mouvement_laser,xB,yB,n)
    
def ic ():
    global nbcoin
    if nbcoin <= 0:
        canevas.create_image( 430, 600, image =insert)
    else :
        jouer()

def coin ():
    global nbcoin
    nbcoin +=1
Mafenetre.geometry("900x900")
Mafenetre.title("world war2 v.2")
canevas.place(x=0,y=0)


canvas1.create_image( 0, 0, image = bg,anchor = "nw")
canevas.create_image( 0, 0, image = bg,anchor = "nw")
canevas.create_image( 430, 300, image = titre)



JOUER=Button(Mafenetre,text="JOUER",command = ic )
COIN=Button(Mafenetre,text="INSERT COIN",command= coin)
COIN.place(x=50,y=780)
JOUER.place(x=400,y=500)


avion_joueur =canvas1.create_image(xAJ,yAJ,image=avion1img)
avion_enemie =canvas1.create_image(xAJ,yAJ,image=avion2img)


Mafenetre.bind_all("<KeyPress>",bouge_avion)
Mafenetre.bind_all("<KeyRelease>",tire_balle)
Mafenetre.mainloop() 