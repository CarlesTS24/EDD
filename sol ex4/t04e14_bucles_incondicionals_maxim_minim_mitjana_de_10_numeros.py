'''
14.	Programa que calcule el màxim, mínim i mitjana de 10 números entrats per teclat.
'''

print("Dis-me 10 números i et diré quin és el màxim, el mínim i la mitjana.")

# Necessitem un número màxim inicial per a poder comparar després.
# No podem dir que siga el 0 ja que tots els números introduïts podrien ser negatius.
max = int(input("Número: ")) 

# Iniciem també el mínim. El primer valor que ens donen de moment és el màxim i el mínim.
min = max  

# Iniciem l'acumulador de sumes per a calcular la mijana:
sum = 0

# Demanem 9 números perquè un ja l'hem demanat abans.
for i in range(9):           
    num = int(input("Número: "))
    if num > max:
        max = num
    elif num < min:
        min = num
    sum += num
    

# Mostrem el resultat:
print("\nRESULTATS:")
print("Màxim:", max)
print("Mínim:", min)
print("Mitjana:", sum/10)
