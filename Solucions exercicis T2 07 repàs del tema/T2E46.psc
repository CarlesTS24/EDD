Algoritmo A45
	// Entrada de dades
	escribir "Quantes unitats has comprat?"
	leer quantitat
	
	// M�s entrada de dades i c�lculs
	totalFactura = 0
	mientras quantitat <> 0
		escribir "A quin preu?"
		leer preu
		
		// Calculem import
		import = quantitat * preu
		
		// Acumulem tots els imports de la factura
		baseImponible = baseImponible + import
		
		// Tornem a preguntar quantitar per a la seg�ent l�nia de la factura
		escribir "Quantes unitats has comprat?"
		leer quantitat
	FinMientras
	
	// C�lcul IVA
	importIva = baseImponible * 0.16
	importAmbIva = baseImponible + importIva
	
	// C�lcul Dte.
	si importAmbIva > 300
		importDte = importAmbIva * 0.05
	SiNo
		importDte = 0
	FinSi
	importFinal = importAmbIva - importDte
	
	// Eixida de dades
	escribir "Import: ", baseImponible
	escribir "16% d`IVA: ", importIva
	escribir "Import amb IVA: ", importAmbIva
	escribir "5% de dte (si import amb IVA > 300): ", importDte
	escribir "Import final: ", importFinal
	
FinAlgoritmo