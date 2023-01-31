from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Producto, Comentario
from django.shortcuts import render, get_object_or_404
import json
from datetime import datetime


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
    

def mostrarUsuarioID(request, id_usuario):
    usuariosID = get_object_or_404(Usuarios, pk=id_usuario)
    try:
        respuesta_final = []
    except: (KeyError, Usuarios.DoesNotExist)

    else:
        respuesta = {}
        respuesta['id'] = usuariosID.id
        respuesta['nombre'] = usuariosID.nombre
        respuesta['correo'] = usuariosID.correo
        respuesta['telefono'] = usuariosID.telefono
        respuesta['direccion'] = usuariosID.direccion
        respuesta['edad'] = usuariosID.edad
        respuesta['rol'] = usuariosID.rol
        respuesta_final.append(respuesta)
        return JsonResponse(respuesta_final, safe=False)
    
@csrf_exempt
def registrar(request):
    #if(request.method != 'POST'):
    #    return None
    
    json_peticion = json.loads(request.body)
    nuevo_usuario = Usuarios()
    nuevo_usuario.nombre = json_peticion['nombre']
    nuevo_usuario.correo = "pruebacorreo"#json_peticion['correo']
    nuevo_usuario.telefono = "123123123" #json_peticion['direccion'
    nuevo_usuario.direccion = "direccionprueba"
    nuevo_usuario.edad = "19" #json_peticion['edad']
    nuevo_usuario.rol = "0" #json_peticion['rol']
    #cmnuevo_usuario. = "passwordprueba" #json_peticion['password']
    nuevo_usuario.save()
    return JsonResponse({"status": "ok"})
    #return JsonResponse(json_peticion['nombre'])         
            
            
def mostrarProductos(request):
    producto = Producto.objects.all()
    
    mostrar_productos = []
    for data in producto:
        respuesta={}
        respuesta['nombre'] = data.nombre
        respuesta['estado'] = data.estado    
       
        #usuario = Usuarios.objects.filter(producto__vendedor=1)
        respuesta['vendedor'] = 1#1#corregir      
        
        respuesta['estacion'] = data.estacion
        respuesta['precio'] = data.precio
        respuesta['color'] = data.color
        respuesta['talla'] = data.talla
        respuesta['categoría'] = data.categoria
        respuesta['fecha_de_subida'] = data.fecha_de_subida
        mostrar_productos.append(respuesta)
    
    return JsonResponse(mostrar_productos, safe=False)


def mostrarProductoID(request,id_producto):
    productos = Producto.objects.get(id = id_producto)
    #usuario = Producto.objects.filter(usuarios__id=1)
    usuario = Usuarios.objects.filter(id = productos.vendedor)
    lista_producto = []
    resultado = {
        'id' : productos.id,
        'nombre' : productos.nombre,
        'estado' : productos.estado,
        'estacion' : productos.estacion,
        'precio' : productos.precio,
        'color' : productos.color,
        'talla' : productos.talla,
        'categoría' : productos.categoria,
        'fecha de subida' : productos.fecha_de_subida,
        'vendedor' : usuario.id
        
    }
    
    return JsonResponse(resultado,safe=False)

    """
    for productoID in productos:
        producto_objeto = {}
        producto_objeto["id"] = productoID.id
        producto_objeto["nombre"] = productoID.nombre
        producto_objeto["estado"] = productoID.estado
        usuario = Usuarios.objects.filter(id = productoID.vendedor)
        producto_objeto["estacion"] = productoID.estacion
        producto_objeto["precio"] = productoID.precio
        producto_objeto["color"] = productoID.color
        producto_objeto["talla"] = productoID.talla
        producto_objeto["categoría"] = productoID.categoria
        producto_objeto["fecha_de_subida"] = productoID.fecha_de_subida
    for data in usuario:
        vendedor = data.id #vendedor['id'] #1#corregir
        
    """
    

    
    
def crearProducto(request):
    usuario = get_object_or_404(Usuarios,pk=1)
    
    nuevo_producto = Producto()
    nuevo_producto.nombre = "jordan 2"
    nuevo_producto.estado = "nuevo"
    nuevo_producto.vendedor = 1 #vendedor
    nuevo_producto.estacion = "primavera"
    nuevo_producto.precio = 222
    nuevo_producto.color = "blanco y morado"
    nuevo_producto.talla = "22"
    nuevo_producto.categoria = "sneaker"
    nuevo_producto.fecha_de_subida = datetime.now()
    nuevo_producto.save()
    return JsonResponse({"status": "ok"})
""" 
def crear_comentarios_al_producto(request,id_producto):
    productoID = get_object_or_404(Producto, pk = id_producto)
    #esto será innecesario si se usa el id del usuario guardado en la session
    usuarioID = get_object_or_404(Usuarios, pk=1)
    nuevo_comentario = Comentario()
    nuevo_comentario.id_usuario = usuarioID
    nuevo_comentario.id_producto = productoID
    nuevo_comentario.comentario = "esto es un comentario de prueba hardcodeadooooaooooasdoasdo"
    nuevo_comentario.valoracion = 5
    nuevo_comentario.fecha = datetime.now()
    nuevo_comentario.save()
    return JsonResponse({"status" : "ok"})
  """
def mostrar_comentarios_por_id(request,id_prod):
    producto = Producto.objects.get(id = id_prod)
    comentarios = Comentario.objects.filter(id_producto = id_prod)
    lista_comentario = []
    for data in comentarios:
        diccionario={}
        diccionario['id'] = data.id
        diccionario['comentarios'] = data.comentario
        lista_comentario.append(diccionario)
    resultado = {
        'id' : producto.id,
        'nombre' : producto.nombre,
        'fecha' : producto.fecha_de_subida,
        'comentario' : lista_comentario
    }
    
    return JsonResponse(resultado,safe=False)
        
       