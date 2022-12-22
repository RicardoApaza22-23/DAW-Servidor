from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Usuarios


def mostrarUsuarios(request):
    usuarios = Usuarios.objects.all()
    respuesta_final = []
    for data in usuarios:
        listaUsuarios={}
        listaUsuarios['id'] = data.id
        listaUsuarios['nombre'] = data.nombre
        listaUsuarios['telefono'] = data.telefono
        listaUsuarios['direccion'] = data.direccion
        listaUsuarios['edad'] = data.edad
        listaUsuarios['rol'] = data.rol

        respuesta_final.append(listaUsuarios)
    return JsonResponse(respuesta_final, safe=False)
 