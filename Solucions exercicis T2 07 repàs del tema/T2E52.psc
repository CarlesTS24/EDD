Algoritmo exer52
	
	Repetir
		escribir "Dis-me un n�mero d`Armstrong:"
		leer resposta  // per exemple, 153
		// COMPROVAR SI num �S ARMSTRONG O NO
		num = resposta
		sumaCubs = 0
		Mientras num <> 0
			ultDig = num % 10	// Agafem l'ultim digit
			sumaCubs = sumaCubs + (ultDig ^ 3) // Acumulem
			num = trunc(num / 10)  // Li llevem l'ultim digit
			// escribir "Ult dig: ", ultDig, " Suma cubs = ", sumaCubs
		FinMientras
		
		si sumaCubs <> resposta
			escribir "No �s Armstrong. Torna a provar"
		FinSi
		
	Hasta Que sumaCubs = resposta
	
	escribir "S� que �s un n�mero Armstrong"
	
FinAlgoritmo
