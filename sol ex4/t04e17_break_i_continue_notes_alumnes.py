'''
17.	Programa en Python que demane les notes dels alumnes 
(números enters i positius entre 0 i 10) 
i que després mostre quantes notes s'han introduït i la nota mitjana. 
Per a parar d'introduir notes caldrà posar la nota 11, 
que no es tindrà en compte per als càlculs.
'''

'''
Nota: El programa es podria fer sense break ni continue, 
però ho farem així per a vore el seu funcionament.
'''

# Inicialització de comptador i acumulador
notes = 0
suma = 0

# Demanar dades i fer càlculs
while True:
    # Introducció de la nota per teclat
    nota = input("Dis-me una nota (11 per a eixir):")

    # Comprovacions de nota OK
    if not nota.isnumeric():
        print("Han de ser números enters positius. Torna a provar.")
        continue   # No executa la part "que queda" del bucle i torna "dalt" (al while)

    nota = int(nota) 
    if nota > 11:
        print("La nota màxima és 10. Torna a provar.")
        continue   # No executa la part "que queda" del bucle i torna "dalt" (al while)

    # Si volem acabar 
    if nota == 11:
        print("Ja no et demane més notes. Vaig a eixir del bucle.")
        break      # Se n'ix del bucle (va a la següent instrucció del final del bucle)

    # Si tot ha anat bé, farem els càlculs 
    print("Nota introduïda ok:", nota)
    notes += 1
    suma += nota
## Fi del bucle

# Mostrem els resultats
print(notes, "notes introduïdes.")
print("Nota mitja:", suma/notes)
