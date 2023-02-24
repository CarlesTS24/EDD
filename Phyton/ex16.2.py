num = int(input("Introdueix el numero que vols factoritzaar: ") )
def factorial(num): 
    if num < 0: 
        print("El factorial de un numero negatiu no existeix")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = 5; 

print("El factorial de",num,"es", factorial(num)) 
