opcio = 0
contador = 0
paso = False
while True:
    print("""
        Dis-me que vols fer

        1) Donar una temperatura
        2) Pujar un grau a la temperatura
        3) Baixar un grau a la temperatura
        4) Eixir
    """)
    opcio = int(input("Tria una opció: ") )

    if opcio == 1:
        print (" ")
        temperatura = float(input("Introdueix la temperatura: ") )
        print (temperatura)
        contador = contador + 1
        paso = True
    elif opcio == 2:
        if paso == True:
            print (" ")
            temperatura +=  1
            print (temperatura)
            contador = contador + 1
        else:
            print ("ERROR")
    elif opcio == 3:
        if paso == True:
            print (" ")
            temperatura = temperatura - 1
            print (temperatura)
            contador = contador + 1
        else:
            print ("ERROR")
    elif opcio == 4:
        print (contador)
        break
    else:
        print ("Opció incorrecta")


#Programa que, repetidament, mostre un menú amb 4 opcions (Demanar
#temperatura / Pujar 1 grau / Baixar 1 grau / Eixir), que demane per teclat una opció i
#l'execute. Cada vegada que s'augmente o disminuïsca, també es mostrarà la nova
#temperatura. Després del bucle es mostrarà quantes vegades s'ha canviat la
#temperatura.