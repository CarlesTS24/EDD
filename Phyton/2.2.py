# a)
v1 = []
v2 = []
v3 = []

# b)
num_dades = int(input("Quantes dades vols introduir?"))

# c)
v1 = [0]*num_dades
print(len(v1))

# d)
for i in range(0, len(v1)):
    v1[i]= int(input("Quina es la dada a añadir"))
    print(v1)

# e)
v2 = v1
print(v2)

# f)
v3 = [0]*num_dades
for i in range(0, len(v3)):
    v3[i] = v1[i]
    print(v3)

# g)
print(v1 == v2)
print(v1 == v3)

# h)
for i in range(0, len(v1)):
    print(v1[i])
    print(v3[i])
    print(v1[i] == v3[i])

# i)
print(v1)
print(v2)
print(v3)