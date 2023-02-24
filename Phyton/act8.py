llibre_1 = input("Dis-me el títol, el autor i el preu de llibre(en format títol,autor,preu)")
titol, autor, preu = llibre_1.split(",")

llibre_2 = input("Dis-me el títol, el autor i el preu del segon llibre(en format títol,autor,preu)")
titol2, autor2, preu2 = llibre_2.split(",")

llibre_3 = input("Dis-me el títol, el autor i el preu del tercer llibre(en format títol,autor,preu)")
titol3, autor3, preu3 = llibre_3.split(",")

print (titol.ljust(30, " "), autor.ljust(20, " "), preu.ljust(10, " "))
print (titol2.ljust(30, " "), autor2.ljust(20, " "), preu2.ljust(10, " "))
print (titol3.ljust(30, " "), autor3.ljust(20, " "), preu3.ljust(10, " "))