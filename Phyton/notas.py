nota = float(input("Dis-me una nota\n"))

if (nota < 0 or nota > 10):
    print("ERROR")
elif (nota < 5):
    print("ins")
elif (nota < 6):
    print("suf")
elif (nota < 7):
    print("bé")
elif (nota < 9):
    print("not")
elif (nota <= 10):
    print("exc")