Algoritmo exer55_PrimersMenorsDe100
	
	Escribir "Estos són els números primers menors de 100:"
	
	para num = 2 hasta 99 con paso 1  // El núm. 1 no és primer per definició
		
		// ----- Este tros de codi és el de l'exercici de vore si 'num' és primer -----
		troDiv = falso // trobat Divisor
		
		i = 2
		mientras i < num y no troDiv
			si num % i = 0
				troDiv = verdadero
			FinSi
			i = i + 1
		FinMientras
		
		si no troDiv
			Escribir num
		FinSi
		// ----------------------------------------------------------------------------
		
	FinPara
	
FinAlgoritmo

