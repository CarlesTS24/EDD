'''
16.	Programa que calcule el factorial d’un número introduït per teclat ( n! ) 
tenint en compte que:
		0! = 1
    	n! = n * (n-1) * (n-2) * ... * 2 * 1     (sent n > 1)
	Feu-ho amb diferents solucions: 
a) Amb un for recorrent els números des de l'1 fins n
b) Amb un for recorrent els números des d'n fins a 1
c) Amb un while recorrent els números des de l'1 fins n
d) Amb un while recorrent els números des d'n fins a 1
'''

num = int(input("Dis-me un número i et calcularé el seu factorial: "))

print("\na) Amb un for recorrent els números des de l'1 fins n: ", end="")
fac = 1
for i in range(1, num+1):
    fac *= i
print(fac)

print("\nb) Amb un for recorrent els números des d'n fins a 1: ", end="")
fac = 1
for i in range(num, 1, -1):
    fac *= i
print(fac)

print("\nc) Amb un while recorrent els números des de l'1 fins n: ", end="")
fac = 1
i = 1
while i<= num:
    fac *= i
    i += 1
print(fac)

print("\nd) Amb un while recorrent els números des d'n fins a 1: ", end="")
fac = 1
i = num
while i >=1 :
    fac *= i
    i -= 1
print(fac)