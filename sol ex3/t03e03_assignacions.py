'''
3. En el següent programa Python, què valdrà cada 
variable després de cada assignació?
'''

# Nota: la idea de l'exercici és saber el resultat sense fer el programa

a=4
b = 20
b += 23     #a= 4    b= 43
print("a=", a, "\tb=", b)
b //= 2     # a= 4    b= 21
print("a=", a, "\tb=", b)
a -= 2      # a= 2    b= 21
print("a=", a, "\tb=", b)
a *= b + 2  # a= 46   b= 21
print("a=", a, "\tb=", b)
a %= b      # a= 4    b= 21
print("a=", a, "\tb=", b)
a**= b-19   # a= 16   b= 21
print("a=", a, "\tb=", b)
