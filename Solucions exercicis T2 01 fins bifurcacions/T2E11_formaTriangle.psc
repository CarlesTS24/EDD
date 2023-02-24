Algoritmo sin_titulo
	// ENTRADA DE DADES
	Escribir 'Dis-me 3 costats del triangle:'
	Leer n1
	Leer n2
	Leer n3
	// CALCULS
	Si n1>=n2 Y n1>=n3 Entonces
		maxim = n1
		menor1 = n2
		menor2 = n3
	Sino
		Si n2>=n3 Entonces
			maxim = n2
			menor1 = n1
			menor2 = n3
		Sino
			maxim = n3
			menor1 = n1
			menor2 = n2
		FinSi
	FinSi
	// EIXIDA DE RESULTATS
	si (menor1 + menor2) > maxim
		Escribir "Si triangle"
	Sino
		Escribir "No triangle"
	FinSi
FinAlgoritmo

