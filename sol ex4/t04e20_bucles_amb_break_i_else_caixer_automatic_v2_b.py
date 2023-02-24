'''
20.	Fes un programa en Python que simule un caixer automàtic. 
Es demana per teclat la clau contínuament mentre no siga correcta (1234). 
Però com a molt són 5 intents. 
Després del bucle caldrà indicar si s'han superat els intents o si s'ha encertat la clau. 
a) Fes el programa usant un while amb break i l'else del bucle.
b) Fes el programa usant un for amb break i l'else del bucle.
c) Fes el programa usant un while sense break ni l'else del bucle.
'''

# b) Fes el programa usant un for

for i in range(1, 6):
    comb = input("Clau secreta: ")
    if comb == "1234":
        print("Exacte! Ho has encertat en", i, "intents.")
        break  # Com ja s'ha encertat, eixim del bucle (sense esperar els 5 intents)

else:   # Este "else" és del "for", no de l'"if"
    print("No ho has encertat.")
    
print("Adéu")
