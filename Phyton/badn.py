nom = str(input('Com et diuen?\n'))
edat = int(input('Quina edat tens?\n'))
pes = float(input('Quin pes tens?\n'))

print ("Soc " +nom.ljust(40, " ")+", tinc " +str(edat).rjust(2, " ") " i pese" "%6.2f" %(pes))