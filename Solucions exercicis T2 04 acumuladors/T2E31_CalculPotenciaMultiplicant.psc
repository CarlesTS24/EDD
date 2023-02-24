Algoritmo triangleDeSumes	
	// ENTRADA DE DADES
	Escribir "Potencies multiplicant"
	Escribir "Dis-me la base:"
	leer base
	Escribir "Dis-me exponent:"
	leer exp
	
	// CALCULS
	acum = 1
	// ojo: el paso1 és necessari. Si no, dona error (...) ^0
	para i=1 hasta exp con paso 1
		acum = acum * base
	 	Escribir "De moment el total es: ", acum n // No cal. Es informatiu
	FinPara
	
	
	// EIXIDA DE DADES
	Escribir base, "^", exp, "=", acum		
	
	
FinAlgoritmo

