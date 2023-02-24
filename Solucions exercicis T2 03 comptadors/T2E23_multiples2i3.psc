Algoritmo multiples2i3
	cm2=0
	cm3=0
	cm2i3=0
	para i=1 hasta 100
		si i%2=0 
			cm2=cm2+1			
		FinSi
		si i%3=0 
			cm3=cm3+1			
		FinSi
		si i%2=0 y i%3=0
			cm2i3=cm2i3+1			
		FinSi		
	FinPara
	Escribir "Entre 1 i 100 hi ha:"
	Escribir "   ", cm2, " mult de 2"
	Escribir "   ", cm3, " mult de 3"
	Escribir "   ", cm2i3, " mult de 2 i de 3"	
FinAlgoritmo
