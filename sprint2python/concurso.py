from array import array
from calendar import c
import random 
from random import sample

#inicializamos puntuación a 0
puntuacion=0

def pregunta1(puntuacion):
   
    pregunta=input("""Cuál es el tipo principal de Charizard: 
    a)aire
    b)agua
    c)fuego
    """) 
    if(pregunta=='a' or pregunta=='b' or pregunta=='c'):
        print("tu respuesta es " + pregunta)
        if(pregunta=='c'):
            print("Tu respuesta es correcta")
        #si acierta, la puntuación suma 10
            puntuacion=+10
            
        else:
            print("Tu respuesta es incorrecta")
            if(puntuacion>=5):
                puntuacion-=5
            else:
                puntuacion=0
            
    else:
        
        print('solo hay 3 opciones: a, b y c')    

    #print(puntuacion)
    
    return puntuacion
##############################
def pregunta2(puntuacion):
    pregunta2=input("""Cuál es el tipo principal de Pikachu: 
a)aire
b)eléctrico
c)hada""")
    if(pregunta2=='a' or pregunta2=='b' or pregunta2=='c'):
        print("Tu respuesta 2 es: " + pregunta2)
        if(pregunta2=='b'):
            print("Tu respuesta es correcta")
            puntuacion+=10
        else:
            print("tu respuesta es incorrecta")
            if(puntuacion>=5):
                puntuacion-=5
            else:
                puntuacion=0
    #print(puntuacion)
    return(puntuacion)
#############################33
def preg3(puntuacion):
    pregunta3=input("""Cuál es el tipo principal de Bulbasur: 
a)bicho
b)planta
c)hada""")
    if(pregunta3=='a' or pregunta3=='b' or pregunta3=='c'):
        print("Tu respuesta 2 es: " + pregunta3)
        if(pregunta3=='b'):
            print("Tu respuesta es correcta")
            puntuacion+=10
        else:
            print("tu respuesta es incorrecta")
            if(puntuacion>=5):
                puntuacion-=5
            else:
                puntuacion=0
    #print(puntuacion)
    return puntuacion


#como solo tenemos dos pregunta y queremos coger 2 de esas 3 aleatoriamente, asignamos cada pregunta a un valor poscional dentro de la lista "list1"
list1 = [1,2,3]
#cuando se selecciones esas 2 preguntas, las metemos en una lista diferente para que no se repitan
lista2items=sample(list1,2)

if 1 in lista2items:
    puntuacion=pregunta1(puntuacion)
    
if 2 in lista2items:
    puntuacion+=pregunta2(puntuacion)

if 3 in lista2items:
    puntuacion+=preg3(puntuacion)

print("Tu puntuacion total es: " + str(puntuacion))

