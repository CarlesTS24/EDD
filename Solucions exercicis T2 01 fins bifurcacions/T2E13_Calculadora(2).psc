Algoritmo sin_titulo
	// ENTRADA DE DADES
	Escribir 'Escriu un numero:'
	Leer n1
	Escribir 'Operacio (s/r/m/d):'
	Leer op
	Escribir 'Escriu un altre numero:'
	Leer n2
	// CALCULS
	
	Si (op=='s') Entonces
		Escribir 'La suma es ', n1+n2
	Sino
		Si (op=='r') Entonces
			Escribir 'La resta es ', n1-n2
		Sino
			Si (op=='m') Entonces
				Escribir 'La multiplicació és ', n1*n2
			Sino
				Si (op=='d') Entonces
					Escribir 'La divisió és ', n1/n2
				Sino
					Escribir 'Error'
				FinSi
			FinSi
		FinSi
	FinSi
	FinAlgoritmo

