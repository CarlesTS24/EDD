Algoritmo exer35_numeroPrimer_sol2
	Escribir "N�mero:"
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
		Escribir num, " no �s primer"
	Sino
		Escribir num, " �s primer"
	FinSi
		
FinAlgoritmo

// En esta versi� s'ha optat per un "mientras" en compte d'un "para"
// per a poder eixir del bucle si trobem un divisor,
// ja que no caldr� que continuem comprovant altres divisors.
// Els llenguatges de programaci� per a poder eixir del bucle si es compleix 
// una determinada condici�, tenen la instrucci� break.
