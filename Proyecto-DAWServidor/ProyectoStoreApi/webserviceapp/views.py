from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios
from django.shortcuts import render, get_object_or_404


def mostrarUsuarios(request):
    usuarios = Usuarios.objects.all()
    respuesta_final = []
    for data in usuarios:
        listaUsuarios = {}
        listaUsuarios['id'] = data.id
        listaUsuarios['nombre'] = data.nombre
        listaUsuarios['correo'] = data.correo
        listaUsuarios['telefono'] = data.telefono
        listaUsuarios['direccion'] = data.direccion
        listaUsuarios['edad'] = data.edad
        listaUsuarios['rol'] = data.rol

        respuesta_final.append(listaUsuarios)
    return JsonResponse(respuesta_final, safe=False)


def mostrarUsuarioID(request, idUsuario):
    usuariosID = get_object_or_404(Usuarios, pk=idUsuario)
    respuesta_final = []

    respuesta = {}
    respuesta['id'] = usuariosID.id
    respuesta['nombre'] = usuariosID.nombre
    respuesta['correo'] = usuariosID.correo
    respuesta['telefono'] = usuariosID.telefono
    respuesta['direccion'] = usuariosID.direccion
    respuesta['edad'] = usuariosID.edad
    respuesta['rol'] = usuariosID.rol
    respuesta_final.append(respuesta)
    return JsonResponse(respuesta_final,safe=False)
    