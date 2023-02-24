Algoritmo exer40
	Escribir "Minuts totals:"
	leer minutsTotals
	
	dies = trunc(minutsTotals / 1440)   //(60*24)
	minutsSobren = minutsTotals % 1440
	
	hores = trunc(minutsSobren / 60)
	minutsSobren = minutsSobren % 60
	
	escribir "Dies:  ", dies
	escribir "Hores: ", hores
	escribir "Minuts:", minutsSobren
FinAlgoritmo
