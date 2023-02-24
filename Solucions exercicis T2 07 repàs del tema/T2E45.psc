Algoritmo A45
	// Entrada de dades
	escribir "Quantes unitats has comprat?"
	leer quantitat
	escribir "A quin preu?"
	leer preu
	
	// Calculem import
	import = quantitat * preu
	
	// Càlcul IVA
	importIva = import * 0.16
	importAmbIva = import + importIva
	
	// Càlcul Dte.
	si importAmbIva > 300
		importDte = importAmbIva * 0.05
	SiNo
		importDte = 0
	FinSi
	importFinal = importAmbIva - importDte
	
	// Eixida de dades
	escribir "Import: ", import
	escribir "IVA: ", importIva
	escribir "Import amb IVA: ", importAmbIva
	escribir "Dte: ", importDte
	escribir "Import final: ", importFinal
	
FinAlgoritmo