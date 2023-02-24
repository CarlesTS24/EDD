Algoritmo exer38
	// Dades que ens venen donades (en cèntims)
	preuH = 200
	preuM = 4
	
	// Entrada de dades
	Escribir "Minuts totals de parquing:"
	leer minutsTotals
	
	// Càlcul del temps en hores i minuts
	hores = trunc(minutsTotals/60)
	minuts = minutsTotals % 60
	
	// Càlcul dels imports
	importH = hores * preuH
	importM = minuts * preuM
	
	si importM > preuH
		importM = preuH
	FinSi
	importT = importM + importH
	
	// Eixida de dades
	escribir "Total a pagar: ", importT
	
FinAlgoritmo
