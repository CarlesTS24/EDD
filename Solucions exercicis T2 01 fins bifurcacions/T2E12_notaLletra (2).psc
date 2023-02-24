Algoritmo sin_titulo
	Escribir 'Nota:'
	Leer n
	Si n<0 O n>10 Entonces
		Escribir "Nota incorrecta"
	Sino
		Si n<4 Entonces
			nll <- 'md'
		Sino
			Si n<5 Entonces
				nll <- 'ins'
			Sino
				Si n<6 Entonces
					nll <- 'suf'
				Sino
					Si n<7 Entonces
						nll <- 'be'
					Sino
						Si n<9 Entonces
							nll <- 'not'
						Sino
							nll <- 'Exc'
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		Escribir 'Estimat alumne: has tret un ',nll
	FinSi
	
FinAlgoritmo

