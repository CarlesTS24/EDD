Algoritmo exer52
	
	Repetir
		escribir "Dis-me un número d`Armstrong:"
		leer resposta  // per exemple, 153
		// COMPROVAR SI num ÉS ARMSTRONG O NO
		num = resposta
		sumaCubs = 0
		Mientras num <> 0
			ultDig = num % 10	// Agafem l'ultim digit
			sumaCubs = sumaCubs + (ultDig ^ 3) // Acumulem
			num = trunc(num / 10)  // Li llevem l'ultim digit
			// escribir "Ult dig: ", ultDig, " Suma cubs = ", sumaCubs
		FinMientras
		
		si sumaCubs <> resposta
			escribir "No és Armstrong. Torna a provar"
		FinSi
		
	Hasta Que sumaCubs = resposta
	
	escribir "Sí que és un número Armstrong"
	
FinAlgoritmo
