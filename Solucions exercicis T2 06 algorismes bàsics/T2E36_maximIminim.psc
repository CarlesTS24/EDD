Algoritmo maximIminim
	Escribir "Numero:"
	
	// INTRODUCCIO DE DADES I CALCULS
	leer num
	// El primer numero sera max i min
	min = num
	max = num
	
	// Busquem els altres numeros
	mientras num!=0
		Escribir "Numero:"
		leer num
		si num != 0
			si num>max
				max = num
			sino
				si num<min
					min = num
				FinSi			
			FinSi
		FinSi
		
		
	FinMientras
	
	// MOSTRAR RESULTATS
	Escribir "Maxim: ", max
	Escribir "Minim: ", min

	
	
FinAlgoritmo
