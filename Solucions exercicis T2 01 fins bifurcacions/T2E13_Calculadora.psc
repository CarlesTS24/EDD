Algoritmo sin_titulo
	// ENTRADA DE DADES
	Escribir 'Escriu un numero:'
	Leer n1
	Escribir 'Operacio (s/r/m/d):'
	Leer op
	Escribir 'Escriu un altre numero:'
	Leer n2
	// CALCULS
	err <- falso
	Si (op=='s') Entonces
		resultat <- n1+n2
	Sino
		Si (op=='r') Entonces
			resultat <- n1-n2
		Sino
			Si (op=='m') Entonces
				resultat <- n1*n2
			Sino
				Si (op=='d') Entonces
					resultat <- n1/n2
				Sino
					err <- verdadero
				FinSi
			FinSi
		FinSi
	FinSi
	// MOSTRAR RESULTATS
	Si err == verdadero Entonces
		Escribir 'Operacio incorrecta'
	Sino
		Escribir 'El resultat es : ',resultat
	FinSi
FinAlgoritmo

