Algoritmo exer35_numeroPrimer_sol1
	Escribir "N�mero:"
	leer num

	troDiv = falso   // trobat divisor
	para i= 2 hasta num-1 con paso 1
		si num % i = 0
			troDiv = verdadero
		FinSi
	FinPara
	
	si troDiv = verdadero
		Escribir num, " no �s primer"
	Sino
		Escribir num, " �s primer"
	FinSi
	// Inconvenient: si posem un n�mero molt gran,
	// encara que trobe prompte un divisor, 
	// el programa continuaria comprovant els 
	// altres possibles divisors.
	// Soluci�: podr�em eixir del bucle quan trobem
	// un divisor (en C i Java seria un 'break' per�
	// el Pseint no ho permet. Per tant, haur�em 
	// d'usar un bucle condicional ("mientras" o "repetir")
	// en compte d'un "para"
	
FinAlgoritmo
