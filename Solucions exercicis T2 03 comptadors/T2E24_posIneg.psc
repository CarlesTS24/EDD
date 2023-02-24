Algoritmo Positius_i_negatius
	cp = 0
	cn = 0
	c0 = 0
	Repetir
		leer num
		
		si num <> 0		
				si num > 0
					cp = cp + 1
				SiNo
					cn = cn + 1		
				FinSi
				si num mod 10 = 0
					c0 = c0 + 1
				FinSi
		finsi
	Hasta Que num = 0
	
	Escribir cp, " positius"
	Escribir cn, " negatius"
	Escribir c0, " acaben en 0"
	
	
	
FinAlgoritmo
