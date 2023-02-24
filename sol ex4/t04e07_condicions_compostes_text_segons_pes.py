'''
7. Demana per teclat el pes d'una persona, en quilos. 
Tant si el pes és menor de 10 kg, com si és > 200 kg, ha de mostrar error. 
En cas contrari mostrarà el pes en grams i també un missatge: 
"flac" si és menor de 50 kg, "normal" si està entre 50 i 100 kg, o "sobrepés" en altre cas.
'''

pes = float(input("Quants kg peses? "))
if pes<10 and pes>200:
    print("Error. Pes incorrecte")
else:
    print("Peses", pes * 1000, "grams")

    if pes < 50:
        estat = "Flac"
    elif pes <= 100:
        estat = "Normal"
    else:
        estat = "Sobrepés"

    print("Estat:", estat)

