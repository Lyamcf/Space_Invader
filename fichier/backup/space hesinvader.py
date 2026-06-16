from tkinter import *
yAJ =200
xAJ= 200
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
        
    moncaneva.coords(avion_joueur,xAJ,yAJ)
    
    
    
    





avion1img = PhotoImage(file="pngegg (1).png")

avion_joueur =moncaneva.create_image(xAJ,yAJ,image=avion1img)
moncaneva.place(x=40,y=65)





mafenetre.bind_all("<Key>",bouge_avion)
mafenetre.mainloop()


