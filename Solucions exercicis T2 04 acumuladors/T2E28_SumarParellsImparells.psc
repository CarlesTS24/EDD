Algoritmo sin_titulo
	// ENTRADA DE DADES
	Escribir "Numero inicial:"
	leer ni
	Escribir "Numero final:"
	leer nf
	
	// CALCULS (i eixida de dades)
	ap = 0
	ai = 0
	Para i<-ni Hasta nf Hacer
		si (i>=0)
			Escribir i
		FinSi
		
		si i%2 = 0
			ap = ap + i
		SiNo
			ai = ai + i
		FinSi
	Fin Para
	
	
	// EIXIDA DE DADES
	escribir "Suma dels parells: ", ap
	escribir "Suma dels imparells: ", ai
	
	
	
	
Fin algoritmo
