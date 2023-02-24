#Carles Talens Selfa

import random

num_jug = int(input("Quants jugadors hi han?"))

punt_maxima = 0
punt_total = 0

for i in range(1, num_jug + 1):
    nom = str(input("Com li diuen al jugador"))
    puntuacio = 0
    carta = int(input("Quines cartes tens"))
    while carta != 0:
        if carta == 1:
            puntuacio += 11
            punt_total += 11
        elif carta == 2 or carta == 4 or carta == 5 or carta == 6 or carta == 7 or carta == 8 or carta == 9:
            puntuacio += 0
            punt_total += 0
        elif carta == 3:
            puntuacio += 10
            punt_total += 10
        elif carta == 10:
            puntuacio += 2
            punt_total += 2
        elif carta == 11:
            puntuacio += 3
            punt_total += 3
        elif carta == 12:
            puntuacio += 4
            punt_total += 4
        elif carta == 0:
            print("Aquest jugador no te mes cartes")
        else:
            print("Eixa carta no esta en la baralla")
        carta = int(input("Quines cartes tens"))
        
    print("El jugador " + nom + " ha conseguit una puntuacio de: " ,puntuacio, " punts" )

    if puntuacio > punt_maxima:
        punt_maxima = puntuacio
        nom_guanyador = nom
    elif punt_maxima == puntuacio:
        nom_guanyador = random.choice(nom_guanyador, nom)

if punt_total > 120:
    print("Algú ha fet trampes")
elif punt_total < 120:
    print("Falten cartes")
else:
    print("El jugador " + nom_guanyador + " ha conseguit la maxima puntuacio amb " ,punt_maxima, " punts")
