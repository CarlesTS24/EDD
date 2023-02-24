Algoritmo triangleDeSumes	
	// ENTRADA DE DADES
	Escribir "Multiplicar sumant"
	Escribir "Dis-me un numero:"
	leer a
	Escribir "Altre numero:"
	leer b
	
	// CALCULS
	acum = 0
	// ojo: el paso1 és necessari. Si no, dona error 0 x (...)
	para i=1 hasta a con paso 1
		acum = acum + b
	//	Escribir "De moment el total es: ", acum n // No cal. Es informatiu
	FinPara
	
	
	// EIXIDA DE DADES
	Escribir a, " x ", b, " = ", acum		
	
	
FinAlgoritmo

