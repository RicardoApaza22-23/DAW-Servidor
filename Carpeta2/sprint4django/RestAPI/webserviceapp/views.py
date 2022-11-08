from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tjuegos, Tcomentarios
from django.views.decorators.csrf  import csrf_exempt
import json
from datetime import date
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

@csrf_exempt
def devolver_juegos_por_id(request,id_solicitado):
	juego = Tjuegos.objects.get(id=id_solicitado)
	comentarios = juego.tcomentarios_set.all()
	lista_comentarios=[]
	for fila_comentarios_sql in comentarios:
		diccionario={}
		diccionario['id'] = fila_comentarios_sql.id
		diccionario['comentarios'] = fila_comentarios_sql.comentarios
		lista_comentarios.append(diccionario)
		resultado = {
			'id': juego.id,
			'nombre': juego.nombre,
			'foto': juego.url_image,
			'categoria': juego.categoria,
			'PEGI': juego.pegi
		}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii':False})

@csrf_exempt
def agregar_comentario(request,juego_id):
	if request.method !='POST':
		return None
	json_peticion = json.loads(request.body)
	comentario = Tcomentarios()
	comentario.comentarios = json_peticion['nuevo_comentario']
	comentario.juegos = Tjuegos.objects.get(id=juego_id)
	comentario.fecha = date.today()
	comentario.save()
	return JsonResponse({"status":"ok"})
