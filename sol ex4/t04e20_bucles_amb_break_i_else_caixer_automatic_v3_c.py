'''
20.	Fes un programa en Python que simule un caixer automàtic. 
Es demana per teclat la clau contínuament mentre no siga correcta (1234). 
Però com a molt són 5 intents. 
Després del bucle caldrà indicar si s'han superat els intents o si s'ha encertat la clau. 
a) Fes el programa usant un while amb break i l'else del while.
b) Fes el programa usant un for
c) Fes el programa usant un while sense break (ni l'else del while, clar).
'''

# c) Fes el programa usant un while sense break (ni l'else del while, clar).

i = 0       # La 'i' compta els intents d'encertar la clau.
comb = ""   # Li posem un valor inicial per a que entre al bucle.

# Bucle demanant la clau mentre no se superen els intents i no s'encerte la clau.
while i < 5 and comb != "1234":
    comb = input("Clau secreta: ")
    i += 1

# Quan eixim del bucle mostrem un missatge o altre depenent del motiu d'haver eixit del bucle.
# Compte en no posar la condició de i==5, ja que potser s'ha encertat en l'últim intent.
if comb == "1234":
    print("Exacte! Ho has encertat en", i, "intents.")
else:   # Este "else" és del "for", no de l'"if"
    print("No ho has encertat.")
    
print("Adéu")