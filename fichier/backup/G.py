from tkinter import*
from random import*
from time import*
import tkinter.font as font
Mafenetre= Tk()
score=0
coin=0
yAJ =600
xAJ= 450
av = -1
temps_enemie = 5000 #temps entre l'aparition des avions enemies
vittesse_avion_enemie=2
vitesse_avion= 30
pasy = 5
yAB=-50
n=0
nbcoin = 0
dest_av = 0
TTT= 0 # variable non utiliser pour l'optimisation 
score = 0
prix_partie = 1 # variable modifiable pour changer le prix d'une partie
textnbcoin = "💰:" + str(nbcoin)
##les image inseré##
bg = PhotoImage(file = 'fond.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="avion enemie.png")
laser = PhotoImage(file="Laser-PNG-Image.png")
titre=PhotoImage(file="pngegg (2).png")
insert=PhotoImage(file="insert.gif")
f = font.Font(family='comic sans Ms')

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

nb_av_enmt=7

def tableau(n):
    
    '''
    postcondition :
    cette fonction renvoie un tableau remplis de 0 avec n list rempli de n 0
    '''
    L=[]
    for e in range (n+1) :
        L.append([])
        for i in range (3):
            L[e].append(0)
    return L

def bouge_avion(evt):
    '''
    cette fonction permet de deplacer l'avion lorsque on apuie sur une touche
    '''
    
    global xAJ,yAJ,vitesse_avion,Tg,Td,Tb,Th
    if evt.keysym==Tb :
        yAJ+=vitesse_avion
    if evt.keysym==Th :
        yAJ-=vitesse_avion
    if evt.keysym==Td :
        xAJ+=vitesse_avion
    if evt.keysym==Tg :
        xAJ-=vitesse_avion
    canvas1.coords(avion_joueur,xAJ,yAJ)
def tire_laser(evt):
    global n,Tt
    
    '''
    cette fonction permet de lancer une balle d'avion
    '''
    
    if evt.keysym==Tt :
        
       
        n=canvas1.create_image(xAJ,yAJ,image=laser) # creer la munition avec un nom different "n"
        
        print("n",n)
        mouvement_laser(xAJ,yAJ,n)
        
def mouvement_laser (xB,yB,n):
    '''
    fait bouger la munition "n" droit vers le haut
    et regarde si elle touche un avion enemie
    '''
    global nb_av_enmt,TAB_POS_AV,dest_av
    yB-=5
    canvas1.coords(n,xB,yB)
    for e in range (nb_av_enmt+1):
        if (TAB_POS_AV[e][1]>xB+-25 and TAB_POS_AV[e][1]<xB+25)and(TAB_POS_AV[e][2]>yB+-25 and TAB_POS_AV[e][2]<yB+25):
            print(TAB_POS_AV[e][0])
            print(TAB_POS_AV)
            dest_av = TAB_POS_AV[e][0]
    canvas1.after(10,mouvement_laser,xB,yB,n)
    
    
def lancer_enemie():
    global temps_enemie,av,nb_av_enmt
    '''
    cette fonction permet de lancer un avion enemie avec un delay definie
    '''
    
    av+=1
    if av > nb_av_enmt:
        av=0
        
    avion_ennemie_creation(randint(25,775),-50,av)
    canvas1.after(temps_enemie,lancer_enemie)

def avion_ennemie_creation(xAB,yAB,av):
    global avion_enemie,nb_av_enmt,TAB_POS_AV
    '''
    permet de creer une avion enemie 
    '''
    
    
    
    a = canvas1.create_image(xAB,yAB,image=avion2img)
    # avec le modul tkinter lors qu'on creer en objet il prend une valeur croissante a partire de 3 2 par 2
    
    
    bouge_avion_enemie(xAB,yAB,av,a)

    
def bouge_avion_enemie(xAB,yAB,av,a):
    global  TAB_POS_AV,dest_av,TTT,vittesse_avion_enemie,score
    '''
    permet de faire bouger l'avion enemie 
    '''
    yAB+=vittesse_avion_enemie
    
    
    
    TAB_POS_AV[av][0] = a
    TAB_POS_AV[av][1] = xAB
    TAB_POS_AV[av][2] = yAB
    
    relancer = "true"
    #if dest_av != TTT :
    if dest_av == a:
          xAB = -50
          relancer = "false"
          score+=1
          print("score",score)
        #TTT = dest_av
    canvas1.coords(a,xAB,yAB)
    if yAB > 750 :
        print("perdue")
    if relancer == "true":
        canvas1.after(10,bouge_avion_enemie,xAB,yAB,av,a)
    

    
def ic ():
    global nbcoin,insertcoin,insertco,prix_partie
    
    if nbcoin < prix_partie:
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
    insertcoin=Label(canevas,text=textnbcoin,font=f,bg="purple",fg="black")
    insertcoin.place(x=800,y=20)
    

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
        
    
    if sett == "true":
    
        settings.destroy()

    sett = "true"
   
    
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
    global nbcoin,avion_joueur,TAB_POS_AV,prix_partie
    
    TAB_POS_AV=tableau(nb_av_enmt)
    canvas1.create_image( 0, 0, image = bg,anchor = "nw")

    
    canvas1.place(x=25,y=25)
    nbcoin -=prix_partie
    textnbcoin = "💰:" + str(nbcoin)
    insertcoin=Label(canvas1,text=textnbcoin,bg="purple",fg="black",font=f)
    insertcoin.place(x=800,y=20)
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