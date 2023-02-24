Algoritmo exer44
	// ENTRADA DE DADES -----------------------------------------
	escribir "Quantes notes té l`alumne?"
	leer quaNotes
	
	// CÀLCULS --------------------------------------------------
	
	// Comptadors (quantitat de notes aprovades o suspeses)
	quaNotesApr = 0
	quaNotesSus = 0
	
	// Acumuladors (suma de notes aprovades o suspeses)
	sumNotesApr = 0
	sumNotesSus = 0
	
	// Preguntem les notes de cada assignatura i acumulem
	para ass=1 hasta quaNotes con paso 1
		escribir "Quina nota ha tret en l`assignatura ", ass, ":"
		leer nota
		si nota < 5
			quaNotesSus = quaNotesSus + 1
			sumNotesSus = sumNotesSus + nota
		SiNo
			quaNotesApr = quaNotesApr + 1
			sumNotesApr = sumNotesApr + nota
		FinSi
	FinPara
	
	// EIXIDA DE RESULTATS -----------------------------------------
	escribir "Quantes aprovades: ", quaNotesApr
	escribir "Quantes suspeses: ", quaNotesSus
	// Per a les divisions evitarem possibles divisions per zero:
	si quaNotes <> 0
		escribir "Nota mitja: ", (sumNotesApr+sumNotesSus)/quaNotes
		si quaNotesApr <> 0
			escribir "Nota mitja de les aprovades: ", sumNotesApr/quaNotesApr
		FinSi
		si quaNotesSus <> 0
			escribir "Nota mitja de les suspeses: ", sumNotesSus/quaNotesSus
		FinSi
	FinSi
	
FinAlgoritmo
