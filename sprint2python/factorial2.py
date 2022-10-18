numero=int(input("Introduce un número para calcular su factorial: "))
def factorial2(numero):
    factorial=1
    while(numero>1):
        factorial*=numero
        numero-=1
    return factorial

print("El factorial de ",numero,"es", factorial2(numero))
    
        