Algoritmo numeroPrimer
	Escribir "Numero:"
	leer num

	troDiv = falso
	i = 2
	mientras (!troDiv y i<num) hacer
		Escribir i
		si num % i = 0
			troDiv = verdadero
		FinSi
		i = i + 1
	FinMientras
	
	si troDiv = verdadero
		Escribir num, " no es primer"
	Sino
		Escribir num, " es primer"
	FinSi
	// Nota: este algorisme millora l'altre 
	// ja que només troba un divisor, se n'ix del bucle
	// sense haver de comprovar tots els altres
	// possibles divisors.
	
FinAlgoritmo
