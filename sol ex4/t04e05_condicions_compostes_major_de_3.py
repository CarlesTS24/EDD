'''
5. Fes un programa que mostre el màxim de 3 números introduïts per teclat.
'''
print("Dis-me 3 números i et diré el major")
a = int(input("Número: "))
b = int(input("Número: "))
c = int(input("Número: "))

if (a>b and a>c):
    major = a
elif (b>c):
    major = b
else:
    major = c

print("El major és el", major)