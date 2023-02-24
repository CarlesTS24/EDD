Algoritmo anysViscutsOK
	Escribir "Any naixement:"
	Leer aNai
	Escribir "Any defuncio:"
	Leer aDef
	Mientras aDef < aNai
		Escribir "Dades incorrectes:"
		Escribir "Any naixement:"
		Leer aNai
		Escribir "Any defuncio:"
		Leer aDef
	FinMientras
	Escribir "Ha viscut ", aDef - aNai, " anys."
	
FinAlgoritmo

