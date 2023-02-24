text = input("Escriu un text")
text_separat = text.split(" ")
llarga = ""
llargaria = 0
llargaria_nova = 0

for i in range (len(text_separat)):
    print("La paraula " ,text_separat[i], " te " ,len(text_separat[i]), " lletres")
    llargaria_nova = len(text_separat[i])
    if text_separat[i] == text_separat[i].lower():
        print("La paraula esta en minuscula")
    elif text_separat[i] == text_separat[i].upper():
        print("La paraula esta en mayuscula")
    else:
        print("La paraula conte majuscules i minuscules")

    if llargaria_nova > llargaria:
        llargaria = llargaria_nova
        llarga = text_separat[i]
print(llarga)