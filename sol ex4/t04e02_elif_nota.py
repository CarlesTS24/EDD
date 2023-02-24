'''
2. Demana una nota amb decimals i mostra el text corresponent: 
“ins”, “suf”, “bé”, “not” o “exc”. O bé "error" si la nota no està entre 0 i 10.
'''

nota = float(input("Nota:"))

if nota<0 or nota>10:
    print("error")
elif nota<5:
    print("ins")
elif nota<6:
    print("suf")
elif nota<7:
    print("bé")
elif nota<9:
    print("not")
else:
    print("exc")