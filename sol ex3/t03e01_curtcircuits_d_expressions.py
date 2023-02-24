sumaNotes = 50
quantAlumnes = 0

'''
a) No donaria error la divisió per 0 ja que no s'executaria
la part dreta de l'and perquè la part esquerra ja és falsa.
''' 
if (quantAlumnes>0) and (sumaNotes/quantAlumnes >= 5):
    print("Nota mitja aprovada") 
else:
    print("Nota mitja no aprovada")

'''
b) Sí que donaria error la divisió per 0 ja que sí que s'executarà
la part esquerra de l'and (ja que sempre s'avalua d'esquerra a dreta)
''' 
if (sumaNotes/quantAlumnes >= 5) and (quantAlumnes>0):
    print("Nota mitja aprovada") 
else:
    print("Nota mitja no aprovada")