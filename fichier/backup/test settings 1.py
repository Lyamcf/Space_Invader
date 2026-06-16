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
textnbcoin = "💰:" + str(nbcoin)
bg = PhotoImage(file = 'fond.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="ennemi.png")
laser = PhotoImage(file="Laser-PNG-Image.png")
titre=PhotoImage(file="pngegg (2).png")
insert=PhotoImage(file="insert.gif")
canvas1 = Canvas( Mafenetre, width = 850,height = 850)
canevas = Canvas( Mafenetre, width = 850,height = 850)

settings = Canvas( Mafenetre, width = 850,height = 800)
settings.create_image( 0, 0, image = bg,anchor = "nw")

Tg = "q"
Td = "d"
Tb = "s"
Th = "z"
Tt = "e"
touchepress = "NONE"

def jouer():
    global nbcoin
    JOUER.destroy()
    COIN.destroy()
    canevas.destroy()
    canvas1.place(x=25,y=25)
    nbcoin -=1
    textnbcoin = "💰:" + str(nbcoin)
    icoin=Label(canevas,text=textnbcoin)
    icoin.place(x=800,y=20)
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

    if evt.keysym=="e" :
        n+=1
        n=canvas1.create_image(xAJ,yAJ,image=laser)
        mouvement_laser(xAJ,yAJ,n)
    canvas1.coords(avion_joueur,xAJ,yAJ)
def bouge_avion_enemie(xAB,yAB):
    yAB+=2
    canvas1.coords(avion_enemie,xAB,yAB)    
    canvas1.after(10,bouge_avion_enemie,xAB,yAB,)
   
        
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
    textnbcoin = "💰:" + str(nbcoin)
    icoin=Label(canevas,text=textnbcoin)
    icoin.place(x=800,y=20)
def setting ():
    global Tg,Td,Tb,Th,Tt, touchepress
    
    canevas.destroy()
    
    settings = Canvas( Mafenetre, width = 850,height = 800)
    settings.create_image( 0, 0, image = bg,anchor = "nw")
    gauchebutton = Button(settings,text="changer",font=("Courier", 15),command = buttong)
    droitebutton = Button(settings,text="changer",font=("Courier", 15),command = buttond)
    hautbutton = Button(settings,text="changer",font=("Courier", 15),command = buttonh)
    basbutton = Button(settings,text="changer",font=("Courier", 15),command = buttonb)
    tirerbutton = Button(settings,text="changer",font=("Courier", 15),command = buttont)
    CloseSettings = Button(settings, tesxt = "close",commande = acueil)
    
    TgM = Tg.upper()
    TdM = Td.upper()
    TbM = Tb.upper()
    ThM = Th.upper()
    TtM = Tt.upper()
    
    gauche = Label(settings,text="Gauche touche : "+ TgM,font=("Courier", 15))
    droite = Label(settings,text="Droite touche : "+ TdM,font=("Courier", 15))
    haut = Label(settings,text="Haut touche : "+ ThM,font=("Courier", 15))
    bas = Label(settings,text="Bas touche : "+ TbM,font=("Courier", 15)) 
    tirer = Label(settings,text="tirer touche : "+ TtM,font=("Courier", 15))
    touche = Label(settings,text="touche pressé : "+ touchepress.upper(),font=("Courier", 20))
    Titre = Label(settings,text = " SETTINGS ",font=("Courier", 30))
    STitre = Label(settings,text = "Pressez une touche puis presser le boutoun changer sur la touche que vous voulez changer",font=("Courier",10))
    
    STitre.place(x= 70, y = 150)
    Titre.place(x = 300,y = 100)
    gauche.place(x= 100,y=300)
    droite.place(x= 100,y=350)
    haut.place(x= 100,y=400)
    bas.place(x= 100,y=450)
    tirer.place(x= 100,y=500)
    touche.place(x= 125,y = 200)
     
    gauchebutton.place(x= 350,y=300)
    droitebutton.place(x= 350,y=350)
    hautbutton.place(x= 350,y=400)
    basbutton.place(x= 350,y=450)
    tirerbutton.place(x= 350,y=500)
    settings.place(x=25,y=25)
    settings.destroy
    settings.after(500,setting)
    CloseSettings.place(x=50,y=50)

def buttong():
    global Tg
    Tg = touchepress
   
def buttond():
    global Td
    Td = touchepress
    destroy_setting()
    setting()
def buttonh():
    global Th
    Th = touchepress
    
def buttonb():
    global Tb
    Tb = touchepress
    
def buttont():
    global Tt
    Tt = touchepress

def touche(evt):
    global touchepress
    touchepress = evt.keysym

def destroy_setting():
    settings.destroy()
    
Mafenetre.geometry("900x900")
Mafenetre.title("world war2 v.2")

def acueil():
    bg = PhotoImage(file = 'fond.gif')
    avion1img = PhotoImage(file="pngegg-_1_.gif")
    avion2img =  PhotoImage(file="ennemi.png")
    laser = PhotoImage(file="Laser-PNG-Image.png")
    titre=PhotoImage(file="pngegg (2).png")
    insert=PhotoImage(file="insert.gif")
    
    canvas1 = Canvas( Mafenetre, width = 850,height = 850)
    canevas = Canvas( Mafenetre, width = 850,height = 850)
    canevas.place(x=0,y=0)


    canvas1.create_image( 0, 0, image = bg,anchor = "nw")
    canevas.create_image( 0, 0, image = bg,anchor = "nw")
    canevas.create_image( 430, 300, image = titre)
    icoin=Label(canevas,text=textnbcoin)
    icoin.place(x=800,y=20)


    JOUER=Button(Mafenetre,text="JOUER",command = ic )
    COIN=Button(Mafenetre,text="INSERT COIN",command= coin)
    SETTINGS=Button(Mafenetre,text="SETTINGS",command= settings)
    SETTINGS.place(x=50,y=50)
    COIN.place(x=50,y=780)
    JOUER.place(x=400,y=500)

    balle=canvas1.create_image(xAJ,yAJ,image=laser)
    avion_joueur =canvas1.create_image(xAJ,yAJ,image=avion1img)
    avion_enemie =canvas1.create_image(xAJ,yAJ,image=avion2img)
    
    
acueil()
Mafenetre.bind_all("<Key>",touche)
Mafenetre.bind_all("<Key>",bouge_avion)
Mafenetre.mainloop() 