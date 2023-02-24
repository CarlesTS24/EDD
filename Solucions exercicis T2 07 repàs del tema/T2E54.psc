Algoritmo exer54
	escribir "Dis-me un numero perfecte:"
	leer num
	
	suma = 0
	para i = 1 hasta (num-1) con paso 1
		si num % i == 0
			suma = suma + i
		FinSi
	FinPara
	si suma == num
		escribir "El ", num, " sí que és perfecte"
	SiNo
		escribir "El ", num, " NO és perfecte"
	FinSi
	
FinAlgoritmo
