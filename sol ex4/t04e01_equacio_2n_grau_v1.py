'''
1. Fes un programa que calcule les solucions reals de l’equació de 2n grau 
ax2 + bx + c = 0
'''

'''
Nota: és important controlar possibles errors que facen avortar el programa, com:
- Arrel quadrada d'un número negatiu
- Divisions per 0 --> Ho controlarem en altra versió del programa (v2)

Per això s'han fet els controls del programa:
'''

import math
# ENTRADA DE DADES
print("Resolució equació 2n grau: ax2 + bx + c = 0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

# CÀLCULS I MOSTRAR RESULTATS

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
    
'''
Nota:
A més, sempre s'ha de tindre en compte que no hi haja divisions per 0
ja que farien avortar el programa.
En altre fitxer hi ha una versió ampliada que contempla este cas i 
com seria la solució (requerix un poc de coneixement matemàtic).
'''