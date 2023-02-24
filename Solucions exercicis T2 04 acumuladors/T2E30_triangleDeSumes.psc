Algoritmo triangleDeSumes	
	Escribir "Numero:"
	leer n
	
	para linia=1 hasta n
		
		totalLinia=0

		para posicio=1 hasta linia			
			escribir sin saltar posicio
			totalLinia = totalLinia + posicio
			
			si posicio < linia
				escribir sin saltar "+"
			FinSi			
		FinPara
		
		escribir sin saltar "="
		escribir totalLinia
		
	FinPara
	
FinAlgoritmo

