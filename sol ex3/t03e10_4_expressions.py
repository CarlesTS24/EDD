'''
4. Sense executar el programa, digues què mostrarà per pantalla:
'''

# Nota: L'objectiu d'este exercici era saber què mostraria però sense executar el programa

a=10
b=3
c = a/b             # c = 3.333333...
d = a<b and b<c     # d = False and ... --> d = False
a += a + b          # a = a + (a + b)   --> a = 10 + (10 + 3)   --> a = 23
b = float(a//b)     # b = float(23//3)  --> b = float(7)        --> b = 7.0
print(a, b, c, d)   # 23 7.0 3.3333333333333335 False