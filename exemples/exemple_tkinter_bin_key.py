from tkinter import *
from tkinter import ttk

def afficheCarac(event): # 1 paramètre (événement)
    print(event.char)

jeu = Tk()
jeu.focus_force()

jeu.bind("<Z>", afficheCarac) 
# L'événement est transmis à la fonction 
# de façon implicite (invisible dans le code)

jeu.bind("<a>", afficheCarac) 
# L'événement est transmis à la fonction 
# de façon implicite (invisible dans le code)

jeu.mainloop()