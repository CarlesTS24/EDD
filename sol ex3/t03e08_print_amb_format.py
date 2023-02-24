'''
8. Demana per teclat les dades de 3 llibres: títol, autor i preu (permet decimals). 
Després cal mostrar les dades en forma de taula: 30 caràcters per al títol, 
20 per a l'autor i 10 per al preu (incloent 2 decimals). Per exemple:
		Diccionari per a ociosos      Joan Fuster              10.40
		L'home manuscrit              Manuel Baixauli          14.25   
		Un nu                         Josep Palàcios            9.50
'''

# ENTRADA DE DADES
print("Dis-me les dades de 3 llibres:")

titol1 = input("\nTítol:")
autor1 = input("Autor:")
preu1  = float(input("Preu:"))

titol2 = input("\nTítol:")
autor2 = input("Autor:")
preu2  = float(input("Preu:"))

titol3 = input("\nTítol:")
autor3 = input("Autor:")
preu3  = float(input("Preu:"))

# EIXIDA DE RESULTATS
print(titol1.ljust(30), autor1.ljust(20), "%10.2f" % preu1)
print(titol2.ljust(30), autor2.ljust(20), "%10.2f" % preu2)
print(titol3.ljust(30), autor3.ljust(20), "%10.2f" % preu3)

'''
Nota: si introduírem un títol de més de 30 caràcters o un títol de més de 20
ens desquadraria. Per a evitar això, podem mostrar només els 30 primers caràcters del títol
introduït i els 20 primers de l'autor. Es faria així:
print(titol1.ljust(30)[0:30], autor1.ljust(20)[0:20], "%10.2f" % preu1)
'''
