Algoritmo exer43
	escribir "A com es paga l hora normal?"
	leer preuHN
	preuHE = preuHN * 1.5
	
	suma = 0
	repetir
	
		escribir "Quantes hores ha treballat?"
		leer hores
		
		si hores > 0
			si hores > 40
				horesN = 40
				horesE = hores - 40
			SiNo
				horesN = hores
				horesE = 0
			FinSi
			
			sou = (horesN * preuHN) + (horesE * preuHE)
			escribir "Sou: ", sou
			suma = suma + sou
		FinSi
		
	Hasta Que hores == 0
	escribir "Suma dels sous dels treballadors és: ", suma
	
FinAlgoritmo
