factor = int(input("Introdueix el numero del qeu vols mostrar la taula de multiplicar: ") )
desde = int(input("Introdueix el numero per el que comensaras a multiplicar: "))
hasta = int(input("Introdueix el numero fins al que multiplicaras: "))

for f in range (desde, hasta + 1):
    print(f'{factor} x {f} = {factor * f} ')