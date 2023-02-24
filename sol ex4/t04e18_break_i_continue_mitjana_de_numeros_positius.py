'''
18.	Programa que demane 10 números (positius i/o negatius) 
i mostre la mitjana només dels positius. 
Fes-ho a l'estil de l'exercici resolt anterior, per a fer ús del continue.
'''

print("Dis-me 10 números (positius i/o negatius) i et diré la mitjana dels positius.")
sumaPos = 0
comptPos = 0
for i in range(10):
    num = float(input("Número: "))

    if (num<0):
        continue   
        # Si és menor que 0 no s'executen les instruccions de baix 
        # i tornarà a "pujar al for", on la 'i' agafarà el següent valor.

    sumaPos += num
    comptPos += 1 

# Recordem que sempre cal evitar divisions per 0 per a que el programa no avorte.
if (comptPos == 0):
    print("No puc calcular la mitjana dels positius perquè no hi ha cap número positiu.")
else:
    print("Mitjana dels positius:", sumaPos / comptPos)

'''
Nota: s'haguera pogut resoldre sense el "continue", usant este if en compte de l'altre:

for i in range(10):
    num = float(input("Número: "))

    if (num>=0):
        sumaPos += num
        comptPos += 1 
'''