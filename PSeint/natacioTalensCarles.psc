Algoritmo sin_titulo
	// CARLES TALENS SELFA
	nota=0
	paisos=0
	not_tot=0
	Escribir "Quants jutges tenim"
	Leer jutges
	Repetir
		paisos=paisos+1
		Escribir "Quin es el nom del pais?"
		Leer pais
		Para i<-1 Hasta jutges Con Paso 1
			Escribir "Quina nota ha donat el jutge(0-10)?"
			Leer nota1
			nota=nota+nota1
			si nota1=10
				Escribir "Este pais si ha conseguit un 10"
			FinSi
		FinPara
		not_mig=nota/jutges
		not_tot=not_mig_tot+not_mig
		Escribir "Hi han mes paisos?"
		Leer a
	Hasta Que a="no"	
	Escribir "Han paricipat " paisos " països"
	not_mig_tot=not_tot/paisos
	Escribir "La nota mitja de tots els paisos es: " not_mig_tot
FinAlgoritmo
