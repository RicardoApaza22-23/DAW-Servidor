from django.shortcuts import render
from django.http import HttpResponse

def pagina_de_prueba(request):
	return HttpResponse("<h1>hola</h1>")
	
def devolver_juegos(request):
	#lista=tJuegos.objects.all()
	