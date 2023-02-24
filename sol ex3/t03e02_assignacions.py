'''
2. En el següent programa Python, què valdrà cada 
variable després de cada assignació?
'''

# Nota: la idea de l'exercici és saber el resultat sense fer el programa

a=6
b=3
b=1+b       # a=6       b=4 
print("a=", a, "\tb=", b)
a=a/b       # a=1.5     b=4 
print("a=", a, "\tb=", b)
b=6//b+b    # a=1.5     b=6//4 + 4  --> b =1 + 4 --> b = 5
print("a=", a, "\tb=", b)

