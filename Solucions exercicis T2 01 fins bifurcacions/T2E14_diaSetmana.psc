Algoritmo sin_titulo
	Escribir 'Numero dia setmana:'
	Leer numDia
	Segun numDia  Hacer
		1:
			nom <- 'Dilluns'
		2:
			nom <- 'Dimarts'
		3:
			nom <- 'Dimecres'
		4:
			nom <- 'Dijous'
		5:
			nom <- 'Divendres'
		6:
			nom <- 'Dissabte'
		7:
			nom <- 'Diumenge'
		De Otro Modo:
			nom <- 'Error'
	FinSegun
	Si nom = 'Error' Entonces
		Escribir 'Nœmero de dia incorrecte'
	Sino
		Escribir 'Hui estem a ', nom
	FinSi
FinAlgoritmo

