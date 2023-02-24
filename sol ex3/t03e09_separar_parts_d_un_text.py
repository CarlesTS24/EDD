'''
9. Demana per teclat la data de hui (separat amb el caràcter / ). 
Després escriu la data amb el format d'este exemple: "4 del 8 de 2020".
'''
data = input("Escriu la data de hui en format dd/mm/yyyy: ")
dia, mes, any = data.split('/')
print("Hui és", dia, "del", mes, "del", any)

'''
Nota:
dia, mes i any seran de tipus cadena. Per tant, si hem introduït 08/07/1970
eixirà en pantalla:
08 del 07 del 1970
Si volguérem que no eixira el 0 (del mes i de l'any) caldria tractar eixes variables
com a números, no com a text. Per tant, després de la instrucció de l'split, caldria fer:
dia = int(dia)
mes = int(mes)
any = int(any)

Ara eixirà:
8 del 7 del 1970
'''

