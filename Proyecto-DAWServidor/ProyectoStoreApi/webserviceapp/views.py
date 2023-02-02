from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Producto, Comentario, Favoritos, Compra
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
    nuevo_usuario.correo = json_peticion['correo'] #"pruebacorreo"#json_peticion['correo']
    nuevo_usuario.telefono = json_peticion['telefono'] #"123123123" #json_peticion['direccion'
    nuevo_usuario.direccion = json_peticion['direccion']#"direccionprueba"
    nuevo_usuario.edad = json_peticion['edad'] #"19" #json_peticion['edad']
    nuevo_usuario.rol = json_peticion['rol']#"0" #json_peticion['rol']
    #cmnuevo_usuario. = "passwordprueba" #json_peticion['password']
    nuevo_usuario.save()
    return JsonResponse({"status": "ok"})
    #return JsonResponse(json_peticion['nombre'])         
   
@csrf_exempt            
def delete_user(request,id_usuario):
    usuario = Usuarios.objects.get(id = id_usuario)
    usuario.delete()
    
    return JsonResponse({"status": "ok"})


 
def mostrarProductos(request):
    producto = Producto.objects.all()
    mostrar_productos = []
    
    for data in producto:
        respuesta={}
        respuesta['nombre'] = data.nombre
        respuesta['estado'] = data.estado     
        #usuario = Usuarios.objects.filter(producto__vendedor=1)
        usuarios = Usuarios.objects.get(id = data.vendedor.id)
        diccionario = {}
        diccionario['id'] = usuarios.id
        diccionario['nombre'] = usuarios.nombre    
        respuesta['vendedor'] = diccionario              
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

    usuario = Usuarios.objects.get(id = productos.vendedor.id)
    lista_producto = []
    diccionario = {}
    diccionario['id'] = usuario.id
    diccionario['nombre'] = usuario.nombre
    lista_producto.append(diccionario)
    
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
        'vendedor' : lista_producto
        
    }
    
    return JsonResponse(resultado,safe=False)
    
@csrf_exempt   
def crearProducto(request):
    usuario = get_object_or_404(Usuarios,id = 1)
    
    nuevo_producto = Producto()
    nuevo_producto.nombre = "jordan 3"
    nuevo_producto.estado = "segunda mano"
    nuevo_producto.vendedor = usuario #vendedor
    nuevo_producto.estacion = "invierno"
    nuevo_producto.precio = 222
    nuevo_producto.color = "verde y morado"
    nuevo_producto.talla = "40"
    nuevo_producto.categoria = "sneaker"
    nuevo_producto.fecha_de_subida = datetime.now()
    nuevo_producto.save()
    return JsonResponse({"status": "ok"})

@csrf_exempt  
def delete_producto(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    producto.delete()
    return JsonResponse({"status": "ok"})

@csrf_exempt  
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
        
def mostrar_favoritos(request):
    favoritos = Favoritos.objects.all()
    
    lista_favoritos = []
    for data in favoritos:
        diccionario = {}
        diccionario['id_producto'] = data.id_producto.id
        diccionario['id_usuarios'] = data.id_usuarios.id
        diccionario['fecha'] = datetime.now()
        
        usuario = Usuarios.objects.get(id = data.id_usuarios.id)
        diccionario['nombre_usuario'] = usuario.nombre
        producto = Producto.objects.get(id = data.id_producto.id)
        diccionario['nombre_producto'] = producto.nombre
        lista_favoritos.append(diccionario)
        
    return JsonResponse(lista_favoritos,safe=False)

def mostrar_favoritoID(request, favorito_id):
    favorito = Favoritos.objects.get(id=favorito_id)
    producto = Producto.objects.filter(id = favorito.id_producto.id)
    usuario = Usuarios.objects.filter(id = favorito.id_usuarios.id)
    lista_favorito = []
    lista_favorito2 = []
    for data in usuario:
        diccionario = {}
        diccionario['id'] = data.id
        diccionario['nombre_usuario'] = data.nombre
        lista_favorito.append(diccionario)
    for data in producto:
        diccionario2={}
        diccionario2['id'] = data.id
        diccionario2['nombre'] = data.nombre
        lista_favorito2.append(diccionario2)
    resultado = {
        'id' : favorito.id,
        'id_usuario' : favorito.id_usuarios.id,
        'id_producto' : favorito.id_producto.id,
        'fecha' : favorito.fecha,
        'usuario' : lista_favorito,
        'producto' : lista_favorito2
        
    }
    #lista_favorito.append(resultado)
    
    return JsonResponse(resultado,safe=False)

def añadir_favorito(request,producto_id):
    producto = get_object_or_404(Producto,pk = producto_id)
    #usuario harcodeado
    usuarioHC = get_object_or_404(Usuarios,pk = 1)
    nuevo_favorito = Favoritos()
    nuevo_favorito.id_usuarios = usuarioHC
    nuevo_favorito.id_producto = producto
    nuevo_favorito.fecha = datetime.now()
    nuevo_favorito.save()
    return JsonResponse({"status":"ok"})
    
    #error: eliminar todas los registros dependiedno del producto_id
    #posible solucin = agregar una condición más al filter y ponerle que reciba el id_producto
    #y además un usuario en concreto, para que elimine ciertos campos y no todos con el mismo producto_id
def delete_favorito(request,producto_id):
    favorito = Favoritos.objects.filter(id_producto = producto_id)
    favorito.delete()
    return JsonResponse({"status" : "ok"})

def mostrar_compras(request):
    compras = Compra.objects.all()
    #usuario = Usuarios.objects.all()
    lista_compras = []
    for data in compras:
        diccionario = {}
        diccionario['id'] = data.id 
        diccionario['fecha'] = data.fecha
        lista_compras.append(diccionario)
    
        

    return JsonResponse({"status" : "ok"})


@csrf_exempt 
def crear_compra(request):
    nueva_compra = Compra()
    #datos harcodeados
    usuario = get_object_or_404(Usuarios,pk=2)
    producto = get_object_or_404(Producto,pk=1)
    
    nueva_compra.id_comprador = usuario
    nueva_compra.id_producto = producto
    nueva_compra.fecha = datetime.now()
    nueva_compra.save()
    
    return JsonResponse({"status" : "ok"})