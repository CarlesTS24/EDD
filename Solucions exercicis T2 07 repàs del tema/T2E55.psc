Algoritmo exer55_PrimersMenorsDe100
	
	Escribir "Estos s�n els n�meros primers menors de 100:"
	
	para num = 2 hasta 99 con paso 1  // El n�m. 1 no �s primer per definici�
		
		// ----- Este tros de codi �s el de l'exercici de vore si 'num' �s primer -----
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

