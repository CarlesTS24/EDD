Algoritmo parquing
	
	// ENTRADA DE DADES
	Escribir "Quants minuts en total has usat el parquing?"
	leer minuts_t
	
	// CËLCULS
	
	// Preus
	p_hora = 2
	p_minut = 0.04
	
	// Quantitats
	q_hores = trunc(minuts_t / 60)
	q_minuts = minuts_t % 60
	
	// Imports
	i_hores = q_hores * p_hora
	i_minuts = q_minuts * p_minut
	si i_minuts > p_hora entonces
		i_minuts = p_hora
	FinSi
	i_total = i_hores + i_minuts
	
	// EIXIDA DE RESULTATS
	Escribir "Cal pagar ", i_total, " euros."
				
FinAlgoritmo
