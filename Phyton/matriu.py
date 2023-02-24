QALU = 3
QASS = 4
QAVA = 2

notes = [None]*QALU

for alu in range(QALU):
    notes[alu] = [None]*QASS
    for ass in range(QASS):
        notes[alu][ass] = [None]*QAVA



# Omplint la matriu amb notes
# ​
for alu in range(QALU):
    print("NOTES DE L'ALUMNE", alu)
    for ass in range( QASS): 
        print("    ASSIG", ass)
        for ava in range(QAVA):
            notes[alu][ass] = input(f"       Dis-me la nota de l'ava {ava}:")


# Mostrem la matriu amb este format:
'''
NOTES DE L'ALUMNE 0
    ASSIG 0
       Dis-me la nota de l'ava 0:3
       Dis-me la nota de l'ava 1:4
    ASSIG 1
       Dis-me la nota de l'ava 0:5
       Dis-me la nota de l'ava 1:5
'''

# Mostra la nota mitja de totes les notes

'''
for alu in range(QALU):
    print("Notas media alumno",alu,":")
    for ass in range(QASS):
        mediaNota = 0
        print("    ASSIG",ass)
        for ava in range(QAVA):
            mediaNota += int(notes[alu][ass])
        mediaNota = mediaNota / QAVA
        print("Nota media :",mediaNota)
'''


# Mostra la nota mitja de cada alumne (mostra número alumne i la seua mitja)
for alu in range(QALU):
    mediaAlumno = 0
    mediaAva = 0
    print("Nota media alumno",alu,":", end=" ")
    for ass in range(QASS):
        mediaNota = 0
        for ava in range(QAVA):
            mediaNota += int(notes[alu][ass])
        mediaAva += mediaNota / QAVA
    mediaAlumno += mediaAva / QASS
    print(mediaAlumno)