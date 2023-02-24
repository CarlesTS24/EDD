'''
3.	Troba els errors en el següent programa que calcula l’àrea d’un cercle a partir del radi. 
Després copia'l amb les correccions, compila’l i executa’l.
'''

'''
Solució:
- Cal definir pi abans d'usar-lo (2a instrucció hauria d'anar la 1a)
- El 3,14 ha d'anar amb punt: 3.14
- Tot el text del print hauria d'anar entre cometes. En este cas, dobles, 
ja que dins té un apòstrof (cometa simple) i hi hauria confusió.
- El punt i coma no està mal (Python el permet) però està de més i sobraria.
- El valor arreplegat amb l'input hauria de convertir-se a número (int o float)
ja que després farem operacions matemàtiques amb ell.
- El comentari amb 3 cometes caldria tancar-lo amb altres 3 cometes (o posar # davant)
- La variable radio hauria de dir-se radi, i PI en minúscules (ja que estaven definides així).
- L'últim print hauria d'anar entre cometes dobles (simples no perquè hi ha un apòstrof).
- La variable area hauria de dir-se area.
- Falta el % davant la variable 'area' en el print

'''

# Programa corregit:

pi = 3.14
print("pi=", pi)
print("Programa de càlcul de l’àrea d’un cercle") 
radi = float(input('Dis-me el radi: '))
# Calcular i imprimir l’àrea
area = pi * radi**2
print("\n\nL'àrea del cercle és: %.2f\n" % area)

