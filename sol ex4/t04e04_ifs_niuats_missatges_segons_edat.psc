// Estes exercici està pensat per a resoldre'l
// en mode ordinograma (no pseudocodi) 
// a partir del programa en Python dels apunts
// (per vore si s'entenen bé els ifs niuats.

Algoritmo sin_titulo
	Escribir 'Anys:'
	Leer edat
	Si edat<0 Entonces
		Escribir "E3rror"
	SiNo
		Escribir "Edat correcta"
		Si edat<12 Entonces
			Escribir "No has fet ESO"
			Si edat<6 Entonces
				Escribir "No has fet primària"
			SiNo
				Escribir "Estàs en primària"
			FinSi
			Escribir "Has de fer ESO"
		SiNo
			Si edat<16 Entonces
				Escribir "Estàs en ESO"
			SiNo
				Si edat<65 Entonces
					Escribir "Estàs en edat de treballar"
				SiNo
					Escribir "Xe, jubila`t"
				FinSi
			FinSi
		FinSi
		Escribir "T`he dit coses sobre l`edat"
	FinSi
	Escribir "Adéu"
FinAlgoritmo