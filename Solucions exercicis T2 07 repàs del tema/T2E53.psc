Algoritmo exer53
	
	Escribir "Numeros de 1 a 1000 que son d Armstrong:"
	para posNA = 1 hasta 1000  // posNA --> possible Número Armstrong
		
		// COMPROVAR SI 'posNA' ÉS ARMSTRONG O NO
		num = posNA
		sumaCubs = 0
		Mientras num <> 0
			ultDig = num % 10	// Agafem l'ultim digit
			sumaCubs = sumaCubs + (ultDig * ultDig * ultDig) // Acumulem
			num = trunc(num / 10)  // Li llevem l'ultim digit
			// escribir "Ult dig: ", ultDig, " Suma cubs = ", sumaCubs
		FinMientras
		
		si sumaCubs == posNA
			escribir posNA
		FinSi
	FinPara
	
FinAlgoritmo
