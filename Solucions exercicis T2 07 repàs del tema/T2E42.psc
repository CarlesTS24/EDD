Algoritmo exer42
	escribir "Quantes hores ha treballat?"
	leer hores
	
	escribir "A com es paga l hora normal?"
	leer preuHN
	
	si hores > 40
		horesN = 40
		horesE = hores - 40
	SiNo
		horesN = hores
		horesE = 0
	FinSi
	
	preuHE = preuHN * 1.5
	sou = (horesN * preuHN) + (horesE * preuHE)
	escribir "Sou: ", sou
	
FinAlgoritmo
