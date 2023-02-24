'''
3. Calculadora. Fes un programa que llija de teclat 2 números 
i una operació aritmètica (S/R/P/D). 
El programa farà el càlcul i imprimirà el resultat.
'''
print("Calculadora a partir de 2 números i una operació.")
a = float(input("Número:"))
b = float(input("Altre número:"))
op = input("Operació (s, r, p, d):")

ok = True   # De moment, tot OK. És a dir: no hi ha cap error

if op=='s':
    res = a+b
elif op=='r':
    res = a-b
elif op=='p':
    res = a*b
elif op=='d':
    if (b==0):
        ok = False  # Si passem per ací ja no està tot OK. No haurem de mostrar el resultat
        print("No podem dividir per 0")
    else:
        res = a/b
else:  
    ok = False  # Si passem per ací ja no està tot OK. No haurem de mostrar el resultat
    print("Error en el codi d'operació")

if ok:      # És el mateix que fer   if ok==True:
    print("El resultat és", res)

