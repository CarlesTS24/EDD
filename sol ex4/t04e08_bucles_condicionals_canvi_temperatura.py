'''
8. Programa que, repetidament, mostre un menú amb 4 opcions 
(Demanar temperatura / Pujar 1 grau / Baixar 1 grau / Eixir), 
que demane per teclat una opció i l'execute. 
Cada vegada que s'augmente o disminuïsca, també es mostrarà la nova temperatura. 
Després del bucle es mostrarà quantes vegades s'ha canviat la temperatura.
'''
qMod = 0    # Quantitat de Modificacions de la temperatura

exisTempInicial = False # Per a no modificar la temperatura si encara no se n'havia posat cap

opcio = -1  # Truquet per a entrar al bucle la 1a vegada

while (opcio != 4):

    print("MENÚ D'OPCIONS")
    print("1. Introduir temperatura nova")
    print("2. Pujar temperatura")
    print("3. Baixar temperatura")
    print("4. Eixir")

    opcio = int(input("Opció: "))

    if opcio==1:
        temp=int(input("Quants graus vols? "))
        qMod += 1
        exisTempInicial = True

    elif opcio==2 or opcio==3:
        if not exisTempInicial:
            print("Primer has de posar una temperatura. ")
        else:
            if opcio==2:
                temp += 1
            else:
                temp -= 1
            qMod += 1
            print("Ara fa", temp, "graus.")
    
    elif opcio==4:
        pass 
        # Es posa el 'pass' en els llocs on Python ens obliga a posar una acció
        # però no en volem posar cap (El 'pass' no fa absolutament res).
    else:
        print("Opció incorrecta.")

if qMod > 0:
    print("Han hagut", qMod, "canvis en la temperatura.")
else:
    print("No han hagut canvis en la temperatura.")