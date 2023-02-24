'''
1. Fes un programa que calcule les solucions reals de l’equació de 2n grau 
ax2 + bx + c = 0
'''

'''
Nota: és important controlar possibles errors que facen avortar el programa, com:
- Arrel quadrada d'un número negatiu
- Divisions per 0 --> En esta versió controlem també eixa part

Per això s'han fet els controls del programa:
'''

import math
# ENTRADA DE DADES
print("Resolució equació 2n grau: ax2 + bx + c = 0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

# CÀLCULS I MOSTRAR RESULTATS
if (a == 0):
    print("No és de 2n grau, ja que en eixe cas és del tipus: bx + c = 0")
    if (b == 0):
        if (c == 0):
            print("Infinites solucions. L'equació es compleix per a qualsevol valor de la x")
        else:
            print("No té solució ja que per a cap valor de x es compleix que", c, "= 0")
    else:
        print("Solució:", -c/b)
else:
    dinsArrel = b**2-4*a*c  # Ho posem en una variable per no repetir el càlcul 3 voltes
    if dinsArrel < 0 :
        print("No té solució")
    else: 
        x1 = (-b + math.sqrt(dinsArrel)) /  ( 2 * a)
        x2 = (-b - math.sqrt(dinsArrel)) /  ( 2 * a)
        if (x1==x2):
            print("Només té 1 solució:", x1)
        else:
            print("Té 2 solucions:")
            print(x1)
            print(x2)