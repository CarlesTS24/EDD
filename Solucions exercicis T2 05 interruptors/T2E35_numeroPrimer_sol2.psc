Algoritmo exer35_numeroPrimer_sol2
	Escribir "Número:"
	leer num

	troDiv = falso // trobat Divisor
	
	i = 2
	mientras i < num y no troDiv
		si num % i = 0
			troDiv = verdadero
		FinSi
		i = i + 1
	FinMientras
	
	si troDiv = verdadero
		Escribir num, " no és primer"
	Sino
		Escribir num, " és primer"
	FinSi
		
FinAlgoritmo

// En esta versió s'ha optat per un "mientras" en compte d'un "para"
// per a poder eixir del bucle si trobem un divisor,
// ja que no caldrà que continuem comprovant altres divisors.
// Els llenguatges de programació per a poder eixir del bucle si es compleix 
// una determinada condició, tenen la instrucció break.
