'''
6. Fes un programa que pregunte quants anys té algú i que mostre per pantalla 
la quantitat d’anys que falten per a la majoria d’edat i per a jubilar-se.
'''

anys = int(input("Quants anys tens?"))
print("Et falten", 18-anys, "per a la majoria d'edat i", 65-anys, "per a jubilar-te.")

'''
Nota: traurà xifres negatives si ja eres major d'edat o estàs jubilat
però això ja ho controlarem quan veiem les condicions (if)
'''