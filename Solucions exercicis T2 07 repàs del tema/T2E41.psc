Algoritmo exer41
	Repetir
		escribir "Dis-me arrel quadrada de 225:"
		leer resposta
		si resposta * resposta <> 225
		// O bé: si resposta <> raiz(225)  
		// O bé: si resposta <> 15
			escribir "Error, torna a provar"
		FinSi
		
	Hasta Que resposta * resposta == 225
	escribir "Correcte"
	
FinAlgoritmo
