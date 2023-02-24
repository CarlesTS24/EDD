'''
3. Calculadora. Fes un programa que llija de teclat 2 números 
i una operació aritmètica (S/R/P/D). 
El programa farà el càlcul i imprimirà el resultat.
'''
print("Calculadora a partir de 2 números i una operació.")
a = float(input("Número:"))
b = float(input("Altre número:"))
op = input("Operació (s, r, p, d):")

ok = True
if op=='s':
    print("El resultat de l'operació és", a+b)
elif op=='r':
    print("El resultat de l'operació és", a-b)
elif op=='p':
    print("El resultat de l'operació és", a*b)
elif op=='d':
    if (b==0):
        print("No podem dividir per 0")
    else:
        print("El resultat de l'operació és", a/b)
else:  
    print("Error en el codi d'operació")

'''
Nota: 
No convé repetir tantes voltes el mateix missatge (El resultat de l'operació és...)
Millor guardar el resultat en una variable i mostrar al final el missatge amb eixa variable.
Està resolt en la versió v2.
'''