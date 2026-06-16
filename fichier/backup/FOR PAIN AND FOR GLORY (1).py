from tkinter import*
from random import*
Mafenetre= Tk()
score=0
yAJ =600
xAJ= 450
pasy = 5
yAB=-50
bg = PhotoImage(file = 'jj.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="ennemi.png")
laser = PhotoImage(file="Laser-PNG-Image.png")

    
    

def jouer():
    label.destroy()
    bouton.destroy()
    canvas1.place(x=25,y=25)
    bouge_avion_enemie(randint(25,875),yAB)
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
coin=Button(Mafenetre, text="insert coin:",bg ="#FFA200")

canevas = Canvas( Mafenetre, width = 850,height = 850)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")




canevas = Canvas( Mafenetre, width = 850,height = 850)
bouton=Button(Mafenetre,text="joue frrr",command=jouer)
label.place(x=200,y=100)

bouton.place(x=380,y=150)



canvas1 = Canvas( Mafenetre, width = 850,height = 850)

canvas1.create_image( 0, 0, image = bg,anchor = "nw")
#canvas1.pack(fill = "both", expand = True)
balle=canvas1.create_image(xAJ,yAJ,image=laser)
avion_joueur =canvas1.create_image(xAJ,yAJ,image=avion1img)
avion_enemie =canvas1.create_image(xAJ,yAJ,image=avion2img)


Mafenetre.bind_all("<Key>",bouge_avion)
Mafenetre.mainloop() 