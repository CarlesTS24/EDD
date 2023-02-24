Algoritmo sin_titulo
	alu=24
	Para alu<-1 hasta 24
		not_mig=0
		Escribir "Disme la primera nota"
		Leer not1
		Escribir "Disme la segona nota"
		Leer not2
		Escribir "Disme la tercera nota"
		Leer not3
		Escribir "Disme la quarta nota"
		Leer not4
		Escribir "Disme la quinta nota"
		Leer not5
		Escribir "Disme la sexta nota"
		Leer not6
		Escribir "Disme la septima nota"
		Leer not7
		not_mig = (not1+not2+not3+not4+not5+not6+not7)/7
		Escribir "La nota mitja del alumne es: " not_mig
		tot_clas= tot_clas+not_mig
	FinPara
	not_mig_clas= tot_clas/alu
	Escribir "La nota mitja de la clase es: " not_mig_clas
FinAlgoritmo