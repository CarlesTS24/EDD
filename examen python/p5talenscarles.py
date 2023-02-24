#Carles Talens Selfa

import random

caselles = int(input("Quantes caselles hi han en el tauler"))
posicio = 0
tirs = 0
rebot = 0

while caselles<10 or caselles>100:
    if caselles<10:
        print('Hi han molt poques caselles tenen que hi haure mes de 10')
        caselles = int(input("Quantes caselles hi han en el tauler"))
    elif caselles>100:
        print('Hi han massa caselles tenen que hi haure menys de 100')
        caselles = int(input("Quantes caselles hi han en el tauler"))

print('Estic en la posició ' , posicio)

while caselles != posicio:
    numero = random.randint(1, 6)
    posicio = posicio + numero
    tirs += 1
    if caselles == posicio:
        break
    if posicio > caselles:
        rebot = posicio - caselles
        posicio = caselles - rebot
        print('He tret un ' , numero , ' i vaig a la casella ' , posicio)
    else:
        print('He tret un ' , numero , ' i vaig a la casella ' , posicio)
    if posicio % 5 == 0:
        posicio = posicio + 5
        print("D'oca a oca i tire perquè em toca. Estic en la casells " , posicio)

print("He guanyat amb " , tirs , " vegades de tirar el dau")