Algoritmo exer39_sol1
	// Entrada de dades per teclat
	escribir "Quants segons en total?"
	leer segonsTotals 
	
	// Càlculs
	segonsSobrants = segonsTotals % 60
	segonsQueFalten = 60 - segonsSobrants
	
	// Eixida de dades per pantalla
	escribir "Falten ", segonsQueFalten, " segons per a minuts sencers"
	
FinAlgoritmo
