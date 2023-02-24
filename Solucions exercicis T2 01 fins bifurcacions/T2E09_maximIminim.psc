Algoritmo sin_titulo
	Escribir 'Dis-me dos numeros:'
	Leer n1
	Leer n2
	Leer n3
	Si n1>=n2 Y n1>=n3 Entonces
		maxim <- n1
	Sino
		Si n2>=n3 Entonces
			maxim = n2
		Sino
			maxim = n3
		FinSi
	FinSi
	Si n1<=n2 Y n1<=n3 Entonces
		minim <- n1
	Sino
		Si n2<=n3 Entonces
			minim = n2
		Sino
			minim = n3
		FinSi
	FinSi
	Escribir 'El maxim es ',maxim
	Escribir 'El minim es ',minim
FinAlgoritmo

