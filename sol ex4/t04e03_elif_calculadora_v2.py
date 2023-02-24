'''
3. Calculadora. Fes un programa que llija de teclat 2 números 
i una operació aritmètica (S/R/P/D). 
El programa farà el càlcul i imprimirà el resultat.
'''
print("Calculadora a partir de 2 números i una operació.")
a = float(input("Número:"))
b = float(input("Altre número:"))
op = input("Operació (s, r, p, d):")

if op=='s':
    res = a+b
elif op=='r':
    res = a-b
elif op=='p':
    res = a*b
elif op=='d':
    if (b==0):
        res = "error"
        print("No podem dividir per 0")
    else:
        res = a/b
else:  
    res = "error"   
    print("Error en el codi d'operació")

if res != "error":
    print("El resultat és", res)

'''
Hem agafat la variable 'res' tant per a guardar un número (el resultat de l'operació)
com per a guardar un text ("error").

Això ho podem fer en Python perquè el tipificat és dinàmic: una mateixa variable pot
ser entera en un moment del programa i de tipus cadena en altre moment.

Però no es podria fer en llenguatges com Java, de tipificat estàtic,
on una variable es declara d'un tipus determinat i ja no pot canviar de tipus 
al llarg del programa.

En la versió v3 està resolt usant:
- una variable entera per al resultat: num
- una altra variable (booleana) per a indicar si ha anat bé l'operació: ok
'''
