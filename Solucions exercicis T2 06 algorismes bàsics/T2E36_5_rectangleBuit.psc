Algoritmo sin_titulo
	Escribir 'Altura del rectangle:'
	Leer altura
	
	Escribir "Ample del rectangle:"
	Leer ample
	
	// PRIMERA LINIA
	para pos=1 hasta ample
		escribir "* " sin saltar
	FinPara
	escribir ""
	
	// MIG	
	para linia = 2 hasta altura-1
		Escribir '* ' sin saltar
		para pos = 2 hasta ample-1
			Escribir '  ' sin saltar
		FinPara
		Escribir '*'
	FinPara	
	
	// ÚLTIMA LINIA
	para pos=1 hasta ample
		escribir "* " sin saltar
	FinPara
	escribir ""
	
		
FinAlgoritmo

