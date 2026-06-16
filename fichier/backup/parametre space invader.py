from tkinter import*
Mafenetre= Tk()
Mafenetre.geometry("900x850")
Mafenetre.title("world war2 v.2")
bg = PhotoImage(file = 'fond.gif')




settings = Canvas( Mafenetre, width = 850,height = 800)
settings.create_image( 0, 0, image = bg,anchor = "nw")

Tg = "q"
Td = "d"
Tb = "s"
Th = "z"
Tt = "e"
touchepress = "NONE"


def setting ():
    global Tg,Td,Tb,Th,Tt, touchepress
    
    
    settings = Canvas( Mafenetre, width = 850,height = 800)
    settings.create_image( 0, 0, image = bg,anchor = "nw")
    gauchebutton = Button(settings,text="changer",font=("Courier", 15),command = buttong)
    droitebutton = Button(settings,text="changer",font=("Courier", 15),command = buttond)
    hautbutton = Button(settings,text="changer",font=("Courier", 15),command = buttonh)
    basbutton = Button(settings,text="changer",font=("Courier", 15),command = buttonb)
    tirerbutton = Button(settings,text="changer",font=("Courier", 15),command = buttont)
    
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
setting()
Mafenetre.bind_all("<Key>",touche)
Mafenetre.mainloop() 