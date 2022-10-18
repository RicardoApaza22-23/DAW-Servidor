#inicializamos puntuación a 0
puntuacion=0

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
##################
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

#######################
pregunta3=input("""Cuál es el tipo principal de Bulbasur: 
a)bicho
b)planta
c)hada""")
if(pregunta3=='a' or pregunta2=='b' or pregunta3=='c'):
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

print("Tu puntuacion total es: " + str(puntuacion))