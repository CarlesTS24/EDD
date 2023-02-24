'''
19.	Programa en Python que ens diga si ha trobat o no 
algun múltiple d'un número determinat en un cert rang de números.
'''
inici = int(input("Des de quin número vols buscar múltiples?"))
limit = int(input("Fins quin número vols buscar múltiples?"))
divisor = int(input("De quin número vols buscar múltiples?"))

for i in range(inici, limit+1):
    print(i)
    if (i % divisor == 0):
        print("En el rang sí que hi ha almenys 1 múltiple de", divisor)
        break

    else:
        print("Encara no he trobat múltiple de", divisor) # Està només per a depurar
 
else: # else del bucle
    print("En tot el rang no hi ha cap múltiple de", divisor)

print("Fi del programa")
