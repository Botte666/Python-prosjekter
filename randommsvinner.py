from tkinter import *
from random import randint


root = Tk()
root.title("Tilfeldig poengvinner")
root.iconbitmap(r"C:\Users\joaki\OneDrive\Skrivebord\MS\canna_4er_icon.ico")
root.geometry("500x500")



def velg():
    #deltagere 6.
    deltagere = ['Fisketryne ' , 'Korean Dragon', '', 'Waldemar', 'Catty ', 'Zodiac ', 'Vinni Knuckle', 'Lucent ', 'Vagrant ', 'Steg ', 'keksegodt  ', 'Developer', 'Bugzy']

    #konvertere til set, dette for å unngå at samme navn dukker opp flere ganger i lista. set har ikke indexnummere men list har, så vi må konvertere tilbake til liste.
    deltagere_set = set(deltagere)
    #konvertere tilbake til liste - 6 deltagere i første lista, etter denne har blitt kjørt er det tilbake til 4.
    unike_deltagere = list(deltagere_set)

    # lage list size variabel, denne er fin å bruke i stedenfor å skrive randint(0, 1000) kan man bytte 1000 med vart_tall. Den er fin gitt at det er mange flere deltagere. #
    # vart_tall er variabelen med tall hvor vi igjen tar i fra lista med deltagere. -1 bak fordi lista starter på 0.
    vart_tall = len(unike_deltagere) -1
    # lage ett random nummer fra 0 - 3
    tilfeldig = randint(0, vart_tall)

    vinnerLabel = Label(root, text=unike_deltagere[tilfeldig], font=("Helvetica", 18))
    vinnerLabel.pack(pady=20)




topLabel = Label(root, text="Dagens cannabis-konge", font=("Helvetica", 24))
topLabel.pack(pady=20)

vinnKnapp = Button(root, text="Velg vinner", font=("Helvetica", 24), command=velg)
vinnKnapp.pack(pady=20)

root.mainloop()