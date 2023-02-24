// Mostra la suma, el producte i la mitjana 
// dels 100 primers números naturals.
Algoritmo calculsNumeros
	suma = 0
	prod = 1 
	para i=1 hasta 100
		suma = suma + i
		prod = prod * i
	FinPara
	mitjana = suma/100
	Escribir "Suma: ", suma
	Escribir "Producte: ", prod
	Escribir "Mitjana: ", mitjana
	
FinAlgoritmo
