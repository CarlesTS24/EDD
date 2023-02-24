pin = 0
conta = 0

while pin != 1234 and conta <= 4:
    pin = float(input("Introdueix el numero que vols factoritzaar:"))
    conta = conta + 1
    if pin == 1234:
        print("La clave es correcta")
        break
    else:
        print("Vuelve a intentra-lo")

if conta == 5:
    print("Demasiados intentos")
