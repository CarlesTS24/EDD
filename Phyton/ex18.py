suma = 0
cont = 0
mitja = 0
positiu = 0

while True:
    num = float(input("Dis-me un numero"))
    if num < 0:
        cont = cont + 1
    if num > 0:
        suma = suma + num
        cont = cont + 1
        positiu = positiu +1
    if num == 0:
        continue
    if cont == 10:
        break

mitja = suma / positiu

print("La mitjana es: " ,mitja)