'''
15.	Programa que mostre les taules de multiplicar del 2 al 9.
'''
for taula in range(2, 10):
    print("\n- TAULA DEL", taula, "-")
    for i in range(1, 11): 
        print(taula, "x", i, "=", taula*i)