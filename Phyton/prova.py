print ('Este es el resultado de la quiniela. ¡Seguro que acierto!')

import random 

for i in range(1,16):
    numero=random.randint(1,3)
    if numero ==1:
        resultado='1'
    if numero ==2:
        resultado='2'
    if numero ==3:
        resultado='X'
    print('Partido '+ str(i)+'. El resultado será '+resultado)