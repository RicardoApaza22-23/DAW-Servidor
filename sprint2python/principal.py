import time
opcion=input("""Introduce la opción que quiere utilizar: 
a)factorial con recursividad
b)factorial sin recursividad
""")

if(opcion=="a"):
    start_time=time.time()
    from factorial import factorial
    end_time=time.time()
    print('El tiempo de ejecución ha sido :' + str(end_time-start_time) + ' s')
elif(opcion=="b"):
    start_time=time.time()
    from factorial2 import factorial2
    end_time=time.time()
    print('El tiempo de ejecución ha sido :' + str(end_time-start_time) + ' s')
    #tarda más la función con sin recursividad
else:
    print("Opción incorrecta")
