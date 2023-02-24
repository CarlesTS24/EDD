from math import sqrt

A = int(input("Ingrese el numero que hara de A\n"))
B = int(input("Ingrese el numero que hara de B\n"))
C = int(input("Ingrese el numero que hara de C\n"))

if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)