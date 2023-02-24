Algoritmo sin_titulo
	Escribir "Quants alumnes?"
	Leer q_alumnes
	
	a_notes = 0
	Para alumne=1 hasta q_alumnes 
		repetir
			Escribir "Dis-me la nota de l alumne ", alumne, ":"
			Leer nota
		hasta que nota >=0 y nota <= 10
		
		a_notes = a_notes + nota 
		
	FinPara
	
	Escribir "La nota mitja es " a_notes / q_alumnes
	Fin algoritmo
