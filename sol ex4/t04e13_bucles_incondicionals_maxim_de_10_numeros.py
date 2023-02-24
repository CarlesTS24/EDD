'''
14.	Programa que calcule el màxim, mínim i mitjana de 10 números entrats per teclat.
'''

print("Dis-me 10 números i et diré quin és el màxim.")

# Necessitem un número màxim inicial per a poder comparar després.
# No podem dir que siga el 0 ja que tots els números introduïts podrien ser negatius.
max = int(input("Número: ")) 

# Demanem 9 números perquè un ja l'hem demanat abans.
for i in range(9):           
    num = int(input("Número: "))
    if num > max:
        max = num

# Mostrem el resultat:
print("El màxim és el", max)
