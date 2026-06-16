from tkinter import*
from random import*
from time import*
import tkinter.font as font
import pygame
pygame.mixer.init()



Mafenetre= Tk()
score=0
yAJ =600 #position avion joueur
xAJ= 450
av = -1 #position de l'avion enemie dans le tableau
temps_enemie = 5000 #temps entre l'aparition des avions enemies
vitesse_avion_enemie=1
tps_tir_balle=0.5
vitesse_avion= 30
pasy = 5 #?
yAB=-50
nbcoin = 0
dest_av = 0 #cette variable est utiliser pour renvoy l'avion a detruire
TTT= 0 # variable non utiliser pour l'optimisation 
score = 0
meilleur_score = 0
prix_partie = 1 # variable modifiable pour changer le prix d'une partie
nb_av_enmt=10#variable d'optimisation qui donne le nombre d'avion enmie qui peux avoir en meme dans sur l'ecran
volume_effect_sonore = 1
volume_musique=0.5
stage = 0

textnbcoin = "💰:" + str(nbcoin)

##les image inseré##
go = PhotoImage(file = 'game-over.gif')
bg = PhotoImage(file = 'fond.gif')
avion1img = PhotoImage(file="pngegg-_1_.gif")
avion2img =  PhotoImage(file="avion enemie.png")
laser = PhotoImage(file="Laser-PNG-Image.png")
laser2 = PhotoImage(file="Laser-PNG-Image2.png")
laser3 = PhotoImage(file="Laser-PNG-Image3.png")
titre=PhotoImage(file="pngegg (2).png")
insert=PhotoImage(file="insert.gif")
f = font.Font(family='comic sans Ms')
explosion=PhotoImage(file="pngimg.com - explosion_PNG15372.png")


############################################

sett = "false" #donne si les parametres sont ouvert ou nom
insertco="false" # donne si l'image insert coin est ouverte
#creer une parti des fenetre et insert leur fond

canvas1 = Canvas( Mafenetre, width = 850,height = 800)
canevas = Canvas( Mafenetre, width = 850,height = 800)
settings = Canvas( Mafenetre, width = 850,height = 800)
settings.create_image( 0, 0, image = bg,anchor = "nw")
jeu= "false"
#touche initial pour bouger
Tg = "q"
Td = "d"
Tb = "s"
Th = "z"
Tt = "e"
touchepress = "NONE"
llance_balle = "true"

musique_sound = pygame.mixer.Sound("space invader song.wav")
tire_laser_sound = pygame.mixer.Sound("tire lasser.wav")
explosion_sound = pygame.mixer.Sound("sf_explosion_01-_1_.wav")
piece_sound = pygame.mixer.Sound("piece.wav")
letgo_sound = pygame.mixer.Sound("sm64_mario_lets_go.wav")
gameover_sound = pygame.mixer.Sound("sm64_game_over.wav")

pygame.mixer.Sound.set_volume(musique_sound,volume_musique)
pygame.mixer.Sound.set_volume(tire_laser_sound,volume_effect_sonore)
pygame.mixer.Sound.set_volume(explosion_sound,volume_effect_sonore)
pygame.mixer.Sound.set_volume(piece_sound,volume_effect_sonore)
pygame.mixer.Sound.set_volume(letgo_sound,volume_effect_sonore)
pygame.mixer.Sound.set_volume(gameover_sound,volume_effect_sonore)

musique_activate = "true"
effect_activate = "true"
def tableau(n):
    
    '''
    cette fonction renvoie un tableau remplis de 0 avec 3 colone et permetra de stocker les cordonné de l'avion enemie "a"
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
    if evt.keysym==Tb and yAJ+vitesse_avion<800:
        yAJ+=vitesse_avion
    if evt.keysym==Th and yAJ-vitesse_avion > 0:
        yAJ-=vitesse_avion
    if evt.keysym==Td and xAJ+vitesse_avion<850:
        xAJ+=vitesse_avion
    if evt.keysym==Tg and xAJ-vitesse_avion > 0:
        xAJ-=vitesse_avion
    canvas1.coords(avion_joueur,xAJ,yAJ)
def tire_laser(evt):
    global n,Tt,llance_balle,effect_activate,stage
    
    '''
    cette fonction permet de lancer une balle d'avion
    '''
    if evt.keysym==Tt and llance_balle == "true":
        if effect_activate == "true":
            pygame.mixer.Sound.play(tire_laser_sound,0)
        llance_balle = "false"
        timmer = float(time())
        timer_balle(timmer)
        if stage<3 :
            n=canvas1.create_image(xAJ,yAJ-5,image=laser) # creer la munition avec un nom different "n"
            mouvement_laser(xAJ,yAJ,n)
        elif stage >=3 and stage<5 :
            n=canvas1.create_image(xAJ-10,yAJ,image=laser2) # creer la munition avec un nom different "n"
            mouvement_laser(xAJ-22,yAJ,n)
            n=canvas1.create_image(xAJ+10,yAJ,image=laser2) # creer la munition avec un nom different "n"
            mouvement_laser(xAJ+22,yAJ,n)
        else :
            n=canvas1.create_image(xAJ,yAJ-5,image=laser3) # creer la munition avec un nom different "n"
            mouvement_laser(xAJ,yAJ,n)
            n=canvas1.create_image(xAJ-10,yAJ,image=laser3) # creer la munition avec un nom different "n"
            mouvement_laser(xAJ-20,yAJ,n)
            n=canvas1.create_image(xAJ+10,yAJ,image=laser3) # creer la munition avec un nom different "n"
            mouvement_laser(xAJ+20,yAJ,n)
def timer_balle(timmer):
    global tps_tir_balle,llance_balle
    relancer = "true"
    if timmer+tps_tir_balle<time():
        llance_balle = "true"
        relancer="false"
    if relancer =="true":
        canvas1.after(10,timer_balle,timmer)
    
def mouvement_laser (xB,yB,n):
    '''
    fait bouger la munition "n" droit vers le haut
    et regarde si elle touche un avion enemie
    '''
    global nb_av_enmt,TAB_POS_AV,dest_av,jeu
    relancer = "true"
    yB-=5
    
    for e in range (nb_av_enmt+1):
        if (TAB_POS_AV[e][1]>xB+-25 and TAB_POS_AV[e][1]<xB+25)and(TAB_POS_AV[e][2]>yB+-25 and TAB_POS_AV[e][2]<yB+25):
            TAB_POS_AV[e][1] = 0
            TAB_POS_AV[e][2] = 0
            print(TAB_POS_AV[e][0])
            print(TAB_POS_AV)
            dest_av = TAB_POS_AV[e][0]
            xB = -50
            relancer = "false"
            
            
    canvas1.coords(n,xB,yB)
    if jeu == "true" and relancer == "true":
    
        canvas1.after(10,mouvement_laser,xB,yB,n)
    


def lancer_enemie():
    global temps_enemie,av,nb_av_enmt,jeu
    '''
    cette fonction permet de lancer un avion enemie avec un delay definie
    '''
    
    av+=1
    if av > nb_av_enmt:
        av=0
        
    avion_ennemie_creation(randint(25,775),-50,av)
    if jeu == "true":
        
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
    global  TAB_POS_AV,dest_av,TTT,vitesse_avion_enemie,score,jeu
    '''
    permet de faire bouger l'avion enemie 
    '''
    
    yAB+=vitesse_avion_enemie
    print(vitesse_avion_enemie)
    
    
    TAB_POS_AV[av][0] = a
    TAB_POS_AV[av][1] = xAB
    TAB_POS_AV[av][2] = yAB
    
    relancer = "true"
    #if dest_av != TTT :
    if dest_av == a:
          
          relancer = "false"
          score+=1
          print("score",score)
          textscore=str(score)
          SCORE=Label(canvas1,text="score:"+textscore,bg="purple",fg="black",font=f)
          explosiont = canvas1.create_image(xAB,yAB,image=explosion)
          pygame.mixer.Sound.play(explosion_sound)
          timer = time()
          TAB_POS_AV[av][0] = a
          TAB_POS_AV[av][1] = 0
          TAB_POS_AV[av][2] = 0
          SCORE.place(x=40,y=50)
          explosion_fct(xAB,yAB,explosiont,timer)
          xAB = -50
           
         
        #TTT = dest_av
    if jeu == "true":
        canvas1.coords(a,xAB,yAB)
    if jeu == "false":
        relancer =  "false"
    if yAB > 750 :
        perdu()
    if relancer == "true":
        canvas1.after(10,bouge_avion_enemie,xAB,yAB,av,a)
    
def explosion_fct (xAB,yAB,explosiont,timer):
    relancer = "true"
    if timer+0.5<time():
        print(timer)
        canvas1.coords(explosiont,-50,yAB)
        relancer= "false"
    if relancer == "true":
        canvas1.after(10,explosion_fct,xAB,yAB,explosiont,timer)
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
    insertcoin.place(x=800,y=50)
    pygame.mixer.Sound.play(piece_sound)
    

def setting ():
    '''
    les parametre du jeu :
    permette de changer les touche pour se deplacer et tirer
    '''
    global Tg,Td,Tb,Th,Tt, touchepress,sett,settings,musique_activate,effect_activate,volume_musique,volume_effect_sonore
    print(sett)
    
    def accueuil():
        global sett
        sett = "false"
        settings.destroy()
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
    
    def musiquebutt():
        global musique_activate
        musique_activate = "false"
        if sett == "true":
            setting()

            
    def musiquebutt2():
        global musique_activate
        musique_activate = "true"
        if sett == "true" :
            setting()
    
    def effectbutt():
        global effect_activate
        effect_activate = "false"
        if sett == "true":
            setting()

            
    def effectbutt2():
        global effect_activate
        effect_activate = "true"
        if sett == "true" :
            setting()
    
                
    def volume_musique_down():
        global volume_musique
        volume_musique-=0.01
        if volume_musique < 0:
            volume_musique = O
        setting()
        
    def volume_musique_up():
        global volume_musique
        volume_musique+=0.01
        if volume_musique >1:
            volume_musique=1
        setting()
            
            
    def volume_effect_down():
        global volume_effect_sonore
        volume_effect_sonore-=0.01
        if volume_effect_sonore<0:
            volume_effect_sonore=0
        setting()
        
    def volume_effect_up():
        global volume_effect_sonore
        volume_effect_sonore+=0.01
        if volume_effect_sonore > 1 :
            volume_effect_sonore=1
        setting()
            

                   
    if sett == "true":
    
        settings.destroy()

    
    if musique_activate == "true" and sett !="true":
       musiquebutt2()
       print("butt2")
    elif  musique_activate == "false" and sett !="true":
        musiquebutt()
        print("butt")
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
    upvolume_musique = Button(settings,text="▶",bg="blue",fg="black",font=f,command = volume_musique_up)
    downvolume_musique = Button(settings,text="◀",bg="blue",fg="black",font=f,command = volume_musique_down)
    upvolume_effect = Button(settings,text="▶",bg="blue",fg="black",font=f,command = volume_effect_up)
    downvolume_effect = Button(settings,text="◀",bg="blue",fg="black",font=f,command = volume_effect_down)
    
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
    Titre = Label(settings,text = " SETTINGS ",font=(f,50),bg="purple",fg="black")
    STitre = Label(settings,text = "Pressez une touche puis presser le boutoun changer sur la touche que vous voulez changer",font=f,bg="purple",fg="black")
    voluume_musique = Label(settings,text = int(volume_musique*100) ,font=(f,20),bg="purple",fg="black")
    voluume_effect = Label(settings,text = int(volume_effect_sonore*100) ,font=(f,20),bg="purple",fg="black")
    
    if musique_activate == "true" :
        musiquebouton2 = Button(settings,text="🎵",bg="white",fg="black",font=f,command = musiquebutt)
        musiquebouton2.place(x=100,y=600)
    else :
        musiquebouton = Button(settings,text="🎵",bg="purple",fg="black",font=f,command = musiquebutt2)
        musiquebouton.place(x=100,y=600)
    if effect_activate == "true" :
        musiquebouton2 = Button(settings,text="🔊",bg="white",fg="black",font=f,command = effectbutt)
        musiquebouton2.place(x=400,y=600)
    else :
        musiquebouton = Button(settings,text="🔇",bg="purple",fg="black",font=f,command = effectbutt2)
        musiquebouton.place(x=400,y=600)  
    #place tout les boutons et labels
    STitre.place(x= 70, y = 150)
    Titre.place(x = 300,y = 50)
    gauche.place(x= 100,y=300)
    droite.place(x= 100,y=350)
    haut.place(x= 100,y=400)
    bas.place(x= 100,y=450)
    tirer.place(x= 100,y=500)
    touche.place(x= 125,y = 200)
    voluume_musique.place(x=215,y=600)
    voluume_effect.place(x=515,y=600)
    
    CloseSETTINGS.place(x = 50,y = 50)
    gauchebutton.place(x= 350,y=300)
    droitebutton.place(x= 350,y=350)
    hautbutton.place(x= 350,y=400)
    basbutton.place(x= 350,y=450)
    tirerbutton.place(x= 350,y=500)
    upvolume_musique.place(x=275,y=600)
    downvolume_musique.place(x=175,y=600)
    upvolume_effect.place(x=575,y=600)
    downvolume_effect.place(x=475,y=600)
    
    settings.place(x=25,y=25)


 
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
    permet de lancer soit la fonction  pour bouger ou la fonction pour afficher la touche selon si les parametre "sett" sont ouvert
    '''
    global sett,jeu
    if sett == "true":
        touche(evt)
    elif jeu == "true" :
        bouge_avion(evt)
        tire_laser(evt)

def jouer():
    '''
    fonction principal lorsqu'on lance le jeu
    '''
    
    global nbcoin,avion_joueur,TAB_POS_AV,prix_partie,canvas1,jeu,score,meilleur_score,xAJ,yAJ,tmp_de_jeu
    def stage_fct():
        '''
        fonction qui permet d'augmenter la difficulté en changeant des variable selon le score
        '''
        global score,stage,temps_enemie,vitesse_avion_enemie,tps_tir_balle
        if score < 10:
            stage = 0
            temps_enemie = randint(3000,4000) #temps entre l'aparition des avions enemies
            vitesse_avion_enemie=1
            tps_tir_balle=0.5
        elif score >= 10 and score<20:
            stage = 1
            temps_enemie = randint(2000,3000)
            vitesse_avion_enemie = 1.25
        elif score >=20 and score <35:
            stage = 2
            vitesse_avion_enemie = 1.5
            tps_tir_balle=0.4
            temps_enemie = randint(1500,2500)
        elif score >= 35 and score < 50 :
            stage = 3
            temps_enemie = randint(1000,2000)
            vitesse_avion_enemie = 1.75
            tps_tir_balle=0.3
        elif score >= 50 and score < 75:
            stage=4
            temps_enemie = randint(500,1500)
            tps_tir_balle=0.2
            vitesse_avion_enemie = 2
        elif score >= 75 and score <100:
            stage = 5
            vitesse_avion_enemie = 2.25
        else :
            stage = 6
            temps_enemie = randin(200,1000)
            tps_tir_balle=0.1
            vitesse_avion_enemie = 2.5
        canvas1.after(500,stage_fct)
    pygame.mixer.Sound.play(letgo_sound)
    
    textmeilleurscore = "MEILLEUR SCORE : " + str(meilleur_score)
    Lab_meilleur_score= Label(canevas,text=textmeilleurscore,font=f,bg="purple",fg="black")
    score = 60
    stage_fct()
    jeu = "true"
    TAB_POS_AV=tableau(nb_av_enmt)
    canvas1 = Canvas( Mafenetre, width = 850,height = 800)
    canvas1.create_image( 0, 0, image = bg,anchor = "nw")

    
    canvas1.place(x=25,y=25)
    nbcoin -=prix_partie
    textnbcoin = "💰:" + str(nbcoin)
    insertcoin=Label(canvas1,text=textnbcoin,bg="purple",fg="black",font=f)
    
    t=0
    xAJ = 450
    yAJ = 600
    avion_joueur =canvas1.create_image(xAJ,yAJ,image=avion1img)
    lancer_enemie()
    textscore=str(score)
    SCORE=Label(canvas1,text="score:"+textscore,bg="purple",fg="black",font=f)
    SCORE.place(x=40,y=50)
    Lab_meilleur_score.place(x=350,y=20)
    insertcoin.place(x=800,y=50)
    tmp_de_jeu=time()
    
def perdu():
    global nbcoin,score,jeu,canevas1,insertcoin,insertco,prix_partie,meilleur_score,tmp_de_jeu
    def accueil():
        global nbcoin
        canvas2.destroy()
        textnbcoin = "💰:" + str(nbcoin)
        insertcoin=Label(canevas,text=textnbcoin,font=f,bg="purple",fg="black")
        insertcoin.place(x=800,y=50)
        jeu = "false"
    def ic_perdu ():
        global nbcoin,insertcoin,insertco,prix_partie
        
        if nbcoin < prix_partie:
            insertcoin = Label(Mafenetre, image =insert)
            insertcoin.place(x=300,y=625)
            insertco="true"
        else :
            canvas2.destroy()
            jouer()

    def coin_perdu ():
        global nbcoin,insertcoin,insertco
        if insertco == "true":
            insertcoin.destroy()
            insertco = "false"
        nbcoin +=1
        textnbcoin = "💰:" + str(nbcoin)
        insertcoin=Label(canvas2,text=textnbcoin,font=f,bg="purple",fg="black")
        insertcoin.place(x=800,y=50)
        pygame.mixer.Sound.play(piece_sound)
        
    canvas1.destroy()
    pygame.mixer.Sound.play(gameover_sound)
    if score > meilleur_score :
        meilleur_score= score
    print(meilleur_score)
    
    tmp_de_jeu=time()-tmp_de_jeu
    minute = 0
    seconde=tmp_de_jeu
    heure=0
    while seconde>60:
        minute+=1
        seconde-=60
    while minute>60:
        heure+=1
        minute-=60
        
    
    canvas2 = Canvas( Mafenetre, width = 850,height = 800)
    canvas2.create_image( 0, 0, image = bg,anchor = "nw")
    canvas2.create_image(430,300,image=go)
    COIN2=Button(canvas2,text="INSERT COIN",bg="purple",fg="black",font=f,command= coin_perdu)
    REJOUER=Button(canvas2,text="REJOUER",bg="purple",fg="black",font=f,command=ic_perdu)
    ACCEUIL=Button(canvas2,text="Acceuil",bg="purple",fg="black",font=f,command=accueil)
    
    textnbcoin = "💰:" + str(nbcoin)
    icoin2=Label(canvas2,text=textnbcoin,bg="purple",fg="black",font=f)
    textscore=str(score)
    SCORE=Label(canvas2,text="score:"+textscore,bg="purple",fg="black",font=f)
    textmeilleurscore = "MEILLEUR SCORE : " + str(meilleur_score)
    Lab_meilleur_score= Label(canevas,text=textmeilleurscore,font=f,bg="purple",fg="black")
    texttmpjeu = "Temps de jeu : "+ str(heure) +"H " + str(minute) +"M " + str(int(seconde)) + "S"
    temps_de_jeu = Label(canvas2,text=texttmpjeu,font=f,bg="purple",fg="black")
    
    temps_de_jeu.place(x=300,y=100)
    canvas2.place(x=25,y=25)
    REJOUER.place(x=400,y=500)
    ACCEUIL.place(x=700,y=600)
    COIN2.place(x=50,y=600)
    icoin2.place(x=800,y=50)
    SCORE.place(x=40,y=50)
    Lab_meilleur_score.place(x=350,y=20)
def musique (lancer):
    global musique_activate,effect_activate,volume_effect_sonore,volume_musique
    '''
    actualisation de la musique et des effect sonore ainsi que les volumes
    '''
    if (musique_activate == "true" and lancer == "true"):
        lancer = "false"
        pygame.mixer.Sound.play(musique_sound,-1)
        print("lancer musique")
        
    elif musique_activate == "false":
        pygame.mixer.Sound.stop(musique_sound)
        lancer ="true"
        
    pygame.mixer.Sound.set_volume(musique_sound,volume_musique)#actualisation des volume sonore
    print(pygame.mixer.Sound.get_volume(musique_sound))
    pygame.mixer.Sound.set_volume(tire_laser_sound,volume_effect_sonore)
    print(pygame.mixer.Sound.get_volume(tire_laser_sound))
    pygame.mixer.Sound.set_volume(explosion_sound,volume_effect_sonore)
    pygame.mixer.Sound.set_volume(piece_sound,volume_effect_sonore)
    pygame.mixer.Sound.set_volume(letgo_sound,volume_effect_sonore)
    pygame.mixer.Sound.set_volume(gameover_sound,volume_effect_sonore)
    Mafenetre.after(1000,musique,lancer)
    
############# CREATION DE LA FENETRE ET DU MENU PRINCIPAL ###############   
    

Mafenetre.geometry("900x800")
Mafenetre.title("world war2 v.2")
Mafenetre.configure(bg="blue")

canevas = Canvas( Mafenetre, width = 850,height = 800)
#canvas1 = Canvas( Mafenetre, width = 850,height = 800)
#canvas2 = Canvas( Mafenetre, width = 850,height = 800)
canevas.place(x=25,y=25)
textnbcoin = "💰:" + str(nbcoin)
textmeilleurscore = "MEILLEUR SCORE : " + str(meilleur_score)
canevas.create_image( 0, 0, image = bg,anchor = "nw")

canevas.create_image( 430, 300, image = titre)
icoin=Label(canevas,text=textnbcoin,font=f,bg="purple",fg="black")
Lab_meilleur_score= Label(canevas,text=textmeilleurscore,font=f,bg="purple",fg="black")
textprixpartie = "prix de la partie : "+str(prix_partie)+" coin"
prix=Label(canevas,text=textprixpartie,bg="purple",fg="black",font=f)

SETTINGS= Button(canevas,text="SETTINGS",bg="purple",fg="black",font=f,command = setting)
JOUER=Button(canevas,text="JOUER",bg="purple",fg="black",font=f,command = ic )
COIN=Button(canevas,text="INSERT COIN",bg="purple",fg="black",font=f,command= coin)


COIN.place(x=50,y=650)
JOUER.place(x=400,y=550)
SETTINGS.place(x=50,y=50)
prix.place(x=350,y=500)
icoin.place(x=800,y=50)
Lab_meilleur_score.place(x=350,y=20)

musique("true")

Mafenetre.bind_all("<Key>",touchechoix)
Mafenetre.mainloop() 