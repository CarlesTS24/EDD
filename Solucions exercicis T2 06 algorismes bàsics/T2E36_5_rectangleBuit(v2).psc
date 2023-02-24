Algoritmo sin_titulo
	Escribir 'Altura del rectangle:'
	Leer altura
	
	Escribir "Ample del rectangle:"
	Leer ample

	para linia = 1 hasta altura
		
		para pos = 1 hasta ample
			si linia == altura o pos == ample o linia == 1 o pos == 1			
				Escribir "* " sin saltar
			sino
				Escribir "  " sin saltar
				
			FinSi
			
		FinPara
		Escribir ''
	FinPara	

		
FinAlgoritmo

