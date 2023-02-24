Algoritmo sin_titulo
	Escribir 'Dis-me dos numeros:'
	Leer n1
	Leer n2
	Leer n3
	Si n1>=n2 Y n1>=n3 Entonces
		menor1 = n2
		menor2 = n3
	Sino
		Si n2>=n3 Entonces
			menor1 = n1
			menor2 = n3
		Sino
			menor1 = n1
			menor2 = n2
		FinSi
	FinSi
	Escribir 'Els menors son ',menor1, " i ", menor2
FinAlgoritmo

