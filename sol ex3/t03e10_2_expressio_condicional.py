'''
2.	Escriu una expressió on s’especifique que una variable numèrica de nom quant 
siga menor o igual que 500 i múltiple de 5 però distinta de 100.
'''
print("Dis-me una quantitat menor o igual que 500 i múltiple de 5 però distinta de 100: ")
quant = int(input())

print(quant<=500 and quant%5==0 and quant!=100)

# Nota: este exercici només demanava l'expressió: quant<=500 and quant%5==0 and quant!=100
# però s'ha fet eixe tros de programa per comprovar que funciona.