numero=int((input("introduzca un número para calcular el factorial: ")))

def factorial(numero): 
    return 1 if (numero==1 or numero==0) else numero * factorial(numero - 1);  

  

print("El factproal de ",numero,"es", factorial(numero))