Algoritmo exempleAcumulador
	// INICIALITZAR L'ACUMULADOR, JUST ABANS DEL BUCLE
	total <- 0
	
	// Bucle
	Repetir
		
		Escribir 'Quantitat:'
		Leer q
		Si q<>0 Entonces
			Escribir 'Preu:'
			Leer p
			// ACUMULAR QUANTITAT
			total <- total+(q*p)
		FinSi
	Hasta Que q=0
	
	// Mostrar acumulador
	Escribir total
FinAlgoritmo

