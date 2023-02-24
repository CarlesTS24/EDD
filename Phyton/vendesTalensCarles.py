# Carles Talens Selfa
noms = []
preus = []
qVendes = []

while True:
    prod_trobat = False

    print("""
        Dis-me que vols fer

        0) Dades per defecte
        1) Introduir un article nou
        2) Fer una venda
        3) Mostrar informació
        4) Esborrar un article
        5) Esborrar tots els articles
        6) Eixir
    """)

    opcio = int(input("Tria una opció: ") )

    if opcio == 0:
        noms.extend(["ratoli","teclat","estoreta","monitor"])
        preus.extend([10,15,1.5,120])
        qVendes.extend([10,10,3,5])

    elif opcio == 1:
        print(" ")
        nou_article = str(input("Quin article vols introduir?"))
        noms.append(nou_article)
        preu_article = float(input("Quin es el preu del article?"))
        preus.append(preu_article)
        qVendes.append(0)
        print(noms)

    elif opcio == 2:
        print(" ")
        prod_busqueda = input("Quin article estas buscant?")
        for i in range(len(noms)):
            if noms[i] == prod_busqueda:
                num_vendes = int(input("Quants " + nou_article + " has comprat?"))
                qVendes[i] = num_vendes
                prod_trobat = True
                break
        if prod_trobat == False:
            print("No s'ha trobat el producte")

    elif opcio == 3:
        importe_total = 0
        importe_max = 0
        mes_venut = 0
        mes_venut_nom = 0
        max_benef = 0

        print("NOM".ljust(10, " "), "QUANT".rjust(4, " "), "PREU".rjust(8, " "), "IMPORT".rjust(10, " "))

        for i in range(len(noms)):
            importe = qVendes[i]*preus[i]
            if qVendes[i] > mes_venut:
                mes_venut_nom = noms[i]
                mes_venut = qVendes[i]
            if importe > importe_max:
                importe_max = importe
                max_benef = noms[i]
            importe_total += importe
            print(noms[i].ljust(10, " "), "%4d %8.2f %10.2f"%(qVendes[i], preus[i], importe))
            
        print (" ".ljust(14, " "), "TOTAL: ".rjust(8, " "), "%6.2f"%(importe_total))
        print("Article més venut: " ,mes_venut_nom, ", amb " ,mes_venut, " unitats")
        print("Article amb més ingressos: " ,max_benef, ", amb " ,importe_max, " euros")

    elif opcio == 4:
        print(noms)
        eliminar = int(input("En quina posicio esta el article que vols eliminar"))
        noms.pop(eliminar)
        preus.pop(eliminar)
        qVendes.pop(eliminar)
        print("El article ha sigut eliminat")

    elif opcio == 5:
        noms.clear()
        preus.clear()
        qVendes.clear()
        print("Tots els articles estan eliminats")

    elif opcio == 6:
        ixir = input("Segur (s/n)")
        if ixir == "s":
            break