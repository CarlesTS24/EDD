num = int(input("Introdueix el numero que vols factoritzaar: ") )
def factorial(num): 
    if num < 0: 
        print("El factorial de un numero negatiu no existeix")

    elif num == 0: 
        return 1
        
    else: 
        for fact in range (1 , num + 1):
            fact *= num 
            num -= 1
num = 5; 

print("Factorial of",num,"is", factorial(num)) 
