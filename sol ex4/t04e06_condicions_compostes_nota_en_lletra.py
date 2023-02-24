'''
6. Demana una nota sense decimals i mostra el text corresponent: 
“ins”, “suf”, “be”, “not” o “exc”. O bé "error" si la nota no està entre 0 i 10.
'''

nota = int(input("Nota: "))

if nota<0 or nota>10:
    print("error")
elif nota <= 4:
    print("ins")
elif nota == 5:
    print("suf")
elif nota == 6:
    print("bé")
elif nota == 7 or nota == 8:
    print("not")
else:
    print("exc")

