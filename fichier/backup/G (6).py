from tkinter import*
from random import*
from time import*
import tkinter.font as font
Mafenetre= Tk()
score=0
coin=0
yAJ =600
xAJ= 450
a = 0
temps_enemie = 5000
pasy = 5
yAB=-50
n=0
nbcoin = 0
textnbcoin = "💰:" + str(nbcoin)
f = font.Font(family='comic sans Ms')
##les image inseré##
bg = PhotoImage(file = 'fond.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="ennemi.png")
laser = PhotoImage(file="Laser-PNG-Image.png")
titre=PhotoImage(file="pngegg (2).png")
insert=PhotoImage(file="insert.gif")
############################################

sett = "false" #donne si les parametres sont ouvert ou nom
insertco="false" # donne si l'image insert coin est ouverte
#creer une parti des fenetre et insert leur fond

canvas1 = Canvas( Mafenetre, width = 850,height = 800)
canevas = Canvas( Mafenetre, width = 850,height = 800)
settings = Canvas( Mafenetre, width = 850,height = 800)
settings.create_image( 0, 0, image = bg,anchor = "nw")

#touche initial pour bouger
Tg = "q"
Td = "d"
Tb = "s"
Th = "z"
Tt = "e"
touchepress = "NONE"


def bouge_avion(evt):
    '''
    cette fonction permet de deplacer l'avion lorsque on apuie sur une touche
    '''
    
    global xAJ,yAJ
    print("avion")
    if evt.keysym=="s" :
        yAJ+=40
    if evt.keysym=="z" :
        yAJ-=40
    if evt.keysym=="d" :
        xAJ+=40
    if evt.keysym=="q" :
        xAJ-=40
    canvas1.coords(avion_joueur,xAJ,yAJ)
def tire_laser(evt):
    '''
    cette fonction permet de lancer une balle d'avion
    '''
    n=0
    if evt.keysym=="e" :
        n+=1 
        n=canvas1.create_image(xAJ,yAJ,image=laser) # creer la munition avec un nom different "n"
        mouvement_laser(xAJ,yAJ,n)
        
def mouvement_laser (xB,yB,n):
    '''
    fait bouger la munition "n" droit vers le haut
    '''
    yB-=5
    canvas1.coords(n,xB,yB)
    canvas1.after(10,mouvement_laser,xB,yB,n)
    
    
def lancer_enemie():
    global temps_enemie
    '''
    cette fonction permet de lancer un avion enemie avec un delay definie
    '''
    avion_ennemie_creation(randint(25,775),yAB)
    canvas1.after(temps_enemie,lancer_enemie)

def avion_ennemie_creation(xAB,yAB):
    global avion_enemie, a
    '''
    permet de creer une avion enemie avec un nom different corespondant a un chiffre entre 1 et 20 : "a"
    '''
    a+=1
    if a > 20:
        a=0
    
    a =canvas1.create_image(xAB,yAB,image=avion2img)
    bouge_avion_enemie(xAB,yAB,a)
    
    
def bouge_avion_enemie(xAB,yAB,a):
    '''
    permet de faire bouger l'avion enemie "a"
    '''
    yAB+=2
    canvas1.coords(a,xAB,yAB)
    print(canvas1.find_overlapping(canvas1.coords(a)[0],canvas1.coords(a)[1],canvas1.coords(a)[2],canvas1.coords(a)[3]))
    canvas1.after(10,bouge_avion_enemie,xAB,yAB,a)
   

    
def ic ():
    global nbcoin,insertcoin,insertco
    
    if nbcoin <= 0:
        insertcoin = Label(Mafenetre, image =insert)
        insertcoin.place(x=300,y=625)
        insertco="true"
    else :
        jouer()

def coin ():
    global nbcoin,insertcoin,insertco
    if insertco == "true":
        insertcoin.destroy()
        insertco = "false"
    nbcoin +=1
    textnbcoin = "💰:" + str(nbcoin)
    icoin=Label(canevas,text=textnbcoin,font=f,bg="purple",fg="black")
    icoin.place(x=800,y=20)
    

def setting ():
    '''
    les parametre du jeu :
    permette de changer les touche pour se deplacer et tirer
    '''
    global Tg,Td,Tb,Th,Tt, touchepress,sett,settings
    print(sett)
    
    def accueuil():
        global sett
        sett = "false"
        settings.destroy()
        print(sett)
    
    if sett == "true":
        print(sett)
        settings.destroy()

    sett = "true"
    print(sett)
    
    #création des button
    settings = Canvas( Mafenetre, width = 850,height = 800)
    settings.create_image( 0, 0, image = bg,anchor = "nw")
    gauchebutton = Button(settings,text="changer",bg="purple",fg="black",font=f,command = buttong)
    droitebutton = Button(settings,text="changer",bg="purple",fg="black",font=f,command = buttond)
    hautbutton = Button(settings,text="changer",bg="purple",fg="black",font=f,command = buttonh)
    basbutton = Button(settings,text="changer",bg="purple",fg="black",font=f,command = buttonb)
    tirerbutton = Button(settings,text="changer",bg="purple",fg="black",font=f,command = buttont)
    CloseSETTINGS = Button(settings,text="CLOSE",bg="purple",fg="black",font=f,command = accueuil)
    
    #permet de mettre en maj les touche
    TgM = Tg.upper()
    TdM = Td.upper()
    TbM = Tb.upper()
    ThM = Th.upper()
    TtM = Tt.upper()
    
    # montre les touche selectioner

    gauche = Label(settings,text="Gauche touche : "+ TgM,font=f,bg="purple",fg="black")
    droite = Label(settings,text="Droite touche : "+ TdM,font=f,bg="purple",fg="black")
    haut = Label(settings,text="Haut touche : "+ ThM,font=f,bg="purple",fg="black")
    bas = Label(settings,text="Bas touche : "+ TbM,font=f,bg="purple",fg="black") 
    tirer = Label(settings,text="tirer touche : "+ TtM,font=f,bg="purple",fg="black")
    touche = Label(settings,text="touche pressé : "+ touchepress.upper(),font=f,bg="purple",fg="black")
    Titre = Label(settings,text = " SETTINGS ",font=f,bg="purple",fg="black")
    STitre = Label(settings,text = "Pressez une touche puis presser le boutoun changer sur la touche que vous voulez changer",font=f,bg="purple",fg="black")
    
    
    #place tout les boutons et labels
    STitre.place(x= 70, y = 150)
    Titre.place(x = 300,y = 100)
    gauche.place(x= 100,y=300)
    droite.place(x= 100,y=350)
    haut.place(x= 100,y=400)
    bas.place(x= 100,y=450)
    tirer.place(x= 100,y=500)
    touche.place(x= 125,y = 200)
    
    CloseSETTINGS.place(x = 50,y = 50)
    gauchebutton.place(x= 350,y=300)
    droitebutton.place(x= 350,y=350)
    hautbutton.place(x= 350,y=400)
    basbutton.place(x= 350,y=450)
    tirerbutton.place(x= 350,y=500)
    settings.place(x=25,y=25)

# permet lorsque qu'on change une touche : apuyer sur le bouton changer ,changhe la valeur de la variable sur la touche presser 
def buttong():
    global Tg,touchepress
    Tg = touchepress

    setting()
def buttond():
    global Td,touchepress
    Td = touchepress

    setting()
def buttonh():
    global Th,touchepress
    Th = touchepress
    
    setting()
def buttonb():
    global Tb,touchepress
    Tb = touchepress
   
    setting()
def buttont():
    global Tt,touchepress
    Tt = touchepress
  
    setting()
    
 
def touche(evt):
    '''
    permet que la touche presser soit afficher dans les parmettre
    '''
    global touchepress
    touchepress = evt.keysym
    print("touche")
    if sett =="true" :
        
        setting()

def touchechoix(evt):
    '''
    permet de lancer soit la fonction  pour boujer ou la fonction pour afficher la touche selojn si les parametre "sett" sont ouvert
    '''
    global sett
    if sett == "true":
        touche(evt)
    else :
        bouge_avion(evt)

def jouer():
    '''
    fonction principal lorsqu'on lance le jeu
    '''
    global nbcoin,avion_joueur
    
    
    canvas1.create_image( 0, 0, image = bg,anchor = "nw")

    
    canvas1.place(x=25,y=25)
    nbcoin -=1
    textnbcoin = "💰:" + str(nbcoin)
    icoin=Label(canvas1,text=textnbcoin,bg="purple",fg="black",font=f)
    icoin.place(x=800,y=20)
    t=0
    avion_joueur =canvas1.create_image(xAJ,yAJ,image=avion1img)
    lancer_enemie()
        
        
    
        


############# CREATION DE LA FENETRE ET DU MENU PRINCIPAL ###############   
    

Mafenetre.geometry("900x800")
Mafenetre.title("world war2 v.2")
Mafenetre.configure(bg="blue")

canevas = Canvas( Mafenetre, width = 850,height = 800)
canvas1 = Canvas( Mafenetre, width = 850,height = 800)
canevas.place(x=25,y=25)
textnbcoin = "💰:" + str(nbcoin)
 
canevas.create_image( 0, 0, image = bg,anchor = "nw")

canevas.create_image( 430, 300, image = titre)
icoin=Label(canevas,text=textnbcoin,font=f,bg="purple",fg="black")
icoin.place(x=800,y=20)
SETTINGS= Button(canevas,text="SETTINGS",bg="purple",fg="black",font=f,command = setting)
JOUER=Button(canevas,text="JOUER",bg="purple",fg="black",font=f,command = ic )
COIN=Button(canevas,text="INSERT COIN",bg="purple",fg="black",font=f,command= coin)

SETTINGS['font'] = f
JOUER['font'] = f
COIN['font'] = f

COIN.place(x=50,y=650)
JOUER.place(x=400,y=550)
SETTINGS.place(x=50,y=50)


Mafenetre.bind_all("<KeyRelease>",tire_laser)
#Mafenetre.bind_all("<KeyPress>",bouge_avion)
Mafenetre.bind_all("<Key>",touchechoix)
Mafenetre.mainloop() 