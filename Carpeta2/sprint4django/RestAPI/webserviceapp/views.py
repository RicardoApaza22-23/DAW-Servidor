from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tjuegos


def pagina_de_prueba(request):
	return HttpResponse("<h1>hola</h1>")
	#return lista

def devolver_juegos(request):
	lista = Tjuegos.objects.all()
	arrayLista = []
	for fila_sql in lista:
		diccionario={}
		diccionario['id'] = fila_sql.id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['foto'] = fila_sql.url_image
		diccionario['categoria'] = fila_sql.categoria
		diccionario['PEGI'] = fila_sql.pegi
		arrayLista.append(diccionario)
	return JsonResponse(arrayLista,safe=False)

