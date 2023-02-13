from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Producto, Comentario, Favoritos, Compra
from django.shortcuts import render, get_object_or_404
import json
from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password
import jwt

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
        listaUsuarios['pass'] = data.contraseña
        listaUsuarios['token'] = data.token
        
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
    
def campo_vacio_de_usuarios(nombre,correo,telefono,direccion,edad,rol):
    if len(nombre)  == 0 or len(correo) == 0 or len(telefono) == 0 or len(direccion) == 0 or (edad) == "" or (rol) == "":    
        return True
    else:
        return False
    
def campo_sin_espacio(request,campo):
    campo_sin_espacio = campo.strip()
    if campo_sin_espacio == 0 or campo_sin_espacio == "":
        return True
    
def usuario_existe_en_bd(request,usuario_nombre):   

    user_exist=Usuarios.objects.filter(nombre = usuario_nombre).exists()
    if user_exist:
        return True
    else:
        return False



@csrf_exempt
def login(request):
    json_peticion = json.loads(request.body)
    username = json_peticion['username']
    password = json_peticion['password']
    token_header = request.headers.get('Auth-Token')
    
    if usuario_existe_en_bd(request,username) == True:
        user = Usuarios.objects.get(nombre = username)
        pass
        if check_password(password,user.contraseña):
            pass
            if user.token == token_header:
               return JsonResponse({"status" : "login succesfully"}) 
            else:
                return JsonResponse({"status" : "token invalido"})

        else: 
            return JsonResponse({"status" : "contraseña incorrecta"})
    else:
        return JsonResponse({"status" : "usuario no coincide"})

        
@csrf_exempt
#falta: validar cada campo
def registrar(request):
    if(request.method != 'POST'):
        return None
    
    json_peticion = json.loads(request.body)
    if usuario_existe_en_bd(request,json_peticion['nombre']) == False:
        nombre_usuario = json_peticion['nombre']
    if usuario_existe_en_bd(request,json_peticion['correo']) == False:
        correo_usuario = json_peticion['correo']
    telefono_usuario = json_peticion['telefono']
    direccion_usuario = json_peticion['direccion']
    edad_usuario = json_peticion['edad']
    rol_usuario = json_peticion['rol']
    pass_usuario = json_peticion['password']
    
    pass_hash = make_password(pass_usuario)
    if campo_vacio_de_usuarios(nombre_usuario,correo_usuario,telefono_usuario,direccion_usuario,edad_usuario,rol_usuario) == False:
        
        nuevo_usuario = Usuarios()
        
        nuevo_usuario.nombre = nombre_usuario
        nuevo_usuario.correo = correo_usuario 
        nuevo_usuario.telefono = telefono_usuario 
        nuevo_usuario.direccion = direccion_usuario 
        nuevo_usuario.edad = edad_usuario 
        nuevo_usuario.rol = rol_usuario
        nuevo_usuario.contraseña = pass_hash
        secret = 'secreto_word'
        payload = {
            'user_id':nuevo_usuario.id,
            'username' : nuevo_usuario.nombre
        }
        token = jwt.encode(payload,secret,algorithm='HS256')
        nuevo_usuario.token = token
        nuevo_usuario.save()
        
        

        return JsonResponse({"status": "usuario registrado"})
        
@csrf_exempt
#falta: implementar valicadiones a los cmapos
def mod_usuario(request,id_usuario):
    
    json_peticion = json.loads(request.body)
    
    usuario = get_object_or_404(Usuarios,id=id_usuario)
    if "nombre" in json_peticion:
        usuario.nombre = json_peticion['nombre']
        
    if "correo" in json_peticion:
        usuario.correo = json_peticion['correo']
    if "telefono" in json_peticion:
        usuario.telefono = (json_peticion['telefono'])
    if "direccion" in json_peticion:
        usuario.direccion = (json_peticion['direccion'])
    if "edad" in json_peticion:
        usuario.edad = (json_peticion['edad'])
    if "rol" in json_peticion:
        usuario.rol = (json_peticion['rol'])


    return JsonResponse({"status": "ok"})    

        
@csrf_exempt            
def delete_user(request,id_usuario):
    usuario = Usuarios.objects.get(id = id_usuario)
    usuario.delete()
    
    return JsonResponse({"status": "usuario eliminado"})


 
def mostrarProductos(request):
    producto = Producto.objects.all()
    mostrar_productos = []
    
    for data in producto:
        respuesta={}
        respuesta['id'] = data.id 
        respuesta['nombre'] = data.nombre
        respuesta['estado'] = data.estado     
        
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


def campo_vacio_de_productos(nombre,estado,estacion,precio,color,talla,categoria,fecha):
    if len(nombre) == 0 or len(estado) == 0 or len(estacion) == 0 or precio == "" or len(color) == 0 or talla == "" or len(categoria) == 0 or len(fecha) == 0:
        return True
    else:
        return False
    
@csrf_exempt   
#falta: validar estos campos
def crearProducto(request):
    
    json_peticion = json.loads(request.body)
    nombre = json_peticion['nombre']
    estado = json_peticion['estado']
    estacion = json_peticion['estacion']
    precio = json_peticion['precio']
    color = json_peticion['color']
    talla = json_peticion['talla']
    categoria = json_peticion['categoria']
    fecha = json_peticion['fecha']
    vendedor = json_peticion['vendedor']
    usuario = get_object_or_404(Usuarios,id = vendedor)
    if campo_vacio_de_productos(nombre,estado,estacion,precio,color,talla,categoria,fecha):
        nuevo_producto = Producto()
        nuevo_producto.nombre = nombre
        nuevo_producto.estado = estado
        nuevo_producto.vendedor = usuario 
        nuevo_producto.estacion = estacion 
        nuevo_producto.precio = precio
        nuevo_producto.color = color 
        nuevo_producto.talla = talla  
        nuevo_producto.categoria = categoria
        nuevo_producto.fecha_de_subida = fecha
        nuevo_producto.save()
    return JsonResponse({"status": "ok"})

@csrf_exempt  
def delete_producto(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    producto.delete()
    return JsonResponse({"status": "producto eliminado"})

@csrf_exempt  
#falta: hacer un post en vez de ser hardocdeado
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
    return JsonResponse(resultado,safe=False)


def mostrar_favoritos_de_usuario(request, id_user):
    usuario = get_object_or_404(Usuarios, pk = id_user)
    favoritos = Favoritos.objects.filter(id_usuarios = usuario)
    lista_favoritos = []
    for data in favoritos:
        diccionario = {}
        diccionario['id'] = data.id
        diccionario['id_producto'] = data.id_producto.id
        diccionario['nombre_producto'] = data.id_producto.nombre
        diccionario['fecha'] = data.fecha
        lista_favoritos.append(diccionario)
    return JsonResponse(lista_favoritos,safe=False)
    
    

#falta(o no ): hacer un post
def añadir_favorito(request,producto_id):
    producto = get_object_or_404(Producto,pk = producto_id)
    #usuario harcodeado
    usuarioHC = get_object_or_404(Usuarios,pk = 48)
    nuevo_favorito = Favoritos()
    nuevo_favorito.id_usuarios = usuarioHC
    nuevo_favorito.id_producto = producto
    nuevo_favorito.fecha = datetime.now()
    nuevo_favorito.save()
    return JsonResponse({"status":"ok"})
    

@csrf_exempt 
def delete_favorito(request,producto_id):
    token_header = request.headers.get("Auth-Token")
    usuario = Usuarios.objects.get(token = token_header)
    favorito = Favoritos.objects.get(id_producto = producto_id, id_usuarios = usuario.id)
    favorito.delete()
    return JsonResponse({"status" : "producto eliminado"})




#falta: mostrar los datos de los productos y usuarios
def mostrar_compras(request):
    compras = Compra.objects.all()
    
    lista_compras = []
    for data in compras:
        diccionario = {}
        diccionario['id'] = data.id 
        diccionario['fecha'] = data.fecha
        lista_compras.append(diccionario)
    return JsonResponse(lista_compras, safe=False)


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
    
    return JsonResponse({"status" : "compra creada"})

def eliminar_compra(request, id_compra):
    compra = Compra.objects.get(id = id_compra)
    compra.delete()
    return JsonResponse({"status" : "compra eliminada"})


#falta hacer la cabecera