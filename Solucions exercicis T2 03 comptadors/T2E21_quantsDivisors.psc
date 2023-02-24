Algoritmo quantsDivisors
	Escribir "Numero:"
	leer n
	
	cDiv = 0
	para posDiv = 1 hasta n
		si n % posDiv = 0
			cDiv = CDiv + 1			
		FinSi				
	FinPara
	
	Escribir "El ", n, " te ", cDiv " divisors"
	
FinAlgoritmo
