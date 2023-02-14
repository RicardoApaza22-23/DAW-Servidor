from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Producto, Comentario, Favoritos, Compra
from django.shortcuts import render, get_object_or_404
import json
from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password
import jwt

#vista para mostrar todos los usuarios
def mostrarUsuarios(request):
    #reunimos todos los objetos de usuarios de la BD en la variable usuario
    usuarios = Usuarios.objects.all()
    #inicializamos array vacio
    respuesta_final = []
    for data in usuarios:
        #recorremos los datos de usuarios de la bd
        #guardamos cada clave->registro en listaUsuarios
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
        #concatena la lista en el array
        respuesta_final.append(listaUsuarios)
        
    return JsonResponse(respuesta_final, safe=False)
    
#método para mostrar un usuario en concreto
def mostrarUsuarioID(request, id_usuario):
    #el usuario lo encontramos a partir del id_usuario que se pasará por url
    usuariosID = get_object_or_404(Usuarios, pk=id_usuario)
    try:
        #inicializamos array vacio
        respuesta_final = []
    except: (KeyError, Usuarios.DoesNotExist)

    else:
        #guardamos cada clave->registro en la lista respuesta
        respuesta = {}
        respuesta['id'] = usuariosID.id
        respuesta['nombre'] = usuariosID.nombre
        respuesta['correo'] = usuariosID.correo
        respuesta['telefono'] = usuariosID.telefono
        respuesta['direccion'] = usuariosID.direccion
        respuesta['edad'] = usuariosID.edad
        respuesta['rol'] = usuariosID.rol
        #concatenamos 
        respuesta_final.append(respuesta)
        return JsonResponse(respuesta_final, safe=False)
    
#metodo para verificar que al registrarse, no contiene nigún campo vacío
def campo_vacio_de_usuarios(nombre,correo,telefono,direccion,edad,rol):
    if len(nombre)  == 0 or len(correo) == 0 or len(telefono) == 0 or len(direccion) == 0 or (edad) == "" or (rol) == "":    
        return True
    else:
        return False
    
#método para eliminar espacios en blanco
def campo_sin_espacio(request,campo):
    campo_sin_espacio = campo.strip()
    if campo_sin_espacio == 0 or campo_sin_espacio == "":
        return True
  
#método para verificar si el nickname o correo ya existe en la BD  
def usuario_existe_en_bd(request,usuario_nombre):   

    user_exist=Usuarios.objects.filter(nombre = usuario_nombre).exists()
    if user_exist:
        return True
    else:
        return False



@csrf_exempt
#POST: curl -X POST http://localhost:8000/login -H "Auth-Token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJ1c2VybmFtZSI6InJpY2FyZG8ifQ.IUHsO5s8BK0oI46zzFg2aSQ-QkZgoTC_OnqefESkiiA" -d "{\"username\" : \"ricardo123456\" , \"password\" : \"abc1\"}"
def login(request):
    #declaramos la variable json_peticion para reunir los vvalores entregados por cuerpo de la peticion
    json_peticion = json.loads(request.body)
    #declaramos variables para estas peticiones
    username = json_peticion['username']
    password = json_peticion['password']
    token_header = request.headers.get('Auth-Token')
    #primero se compara el nickname, si no coincide ya no hace falta pasaro popr los demás parámetros
    if usuario_existe_en_bd(request,username) == True:
        user = Usuarios.objects.get(nombre = username)
        pass
    #si el nickname coinicde, comparamos el passwrod hasheado con check_password
        if check_password(password,user.contraseña):
            pass
        #si todo los anterior está bien, se compara el token 
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
#POST: curl -X POST http://localhost:8000/usuarios/registrar -d "{\"nombre\" : \"usuario3\", \"correo\" : \"usuario3@gmail.com\", \"telefono\" : \"123123123\", \"direccion\" : \"direccion usuario3\", \"edad\" : \"29\",\"rol\":\"0\",\"password\":\"abc123\"}"
def registrar(request):
    #verificar si la petición es POST
    if(request.method != 'POST'):
        return None
    #variable que contiene todas las peticiones del cuerpo
    json_peticion = json.loads(request.body)
    #al registrar no se puede tener un nickname repetido y un correo tampoco
    if usuario_existe_en_bd(request,json_peticion['nombre']) == False:
        nombre_usuario = json_peticion['nombre']
    if usuario_existe_en_bd(request,json_peticion['correo']) == False:
        correo_usuario = json_peticion['correo']
    telefono_usuario = json_peticion['telefono']
    direccion_usuario = json_peticion['direccion']
    edad_usuario = json_peticion['edad']
    rol_usuario = json_peticion['rol']
    pass_usuario = json_peticion['password']
    #hasheamos la contraseña para guardarla en la base de datos
    pass_hash = make_password(pass_usuario)
    #verificamos si algun campo esta vacio
    if campo_vacio_de_usuarios(nombre_usuario,correo_usuario,telefono_usuario,direccion_usuario,edad_usuario,rol_usuario) == False:
        
        nuevo_usuario = Usuarios()
        
        nuevo_usuario.nombre = nombre_usuario
        nuevo_usuario.correo = correo_usuario 
        nuevo_usuario.telefono = telefono_usuario 
        nuevo_usuario.direccion = direccion_usuario 
        nuevo_usuario.edad = edad_usuario 
        nuevo_usuario.rol = rol_usuario
        nuevo_usuario.contraseña = pass_hash
        #elaboracion del token
        secret = 'secreto_word'
        payload = {
            'user_id':nuevo_usuario.id,
            'username' : nuevo_usuario.nombre
        }
        token = jwt.encode(payload,secret,algorithm='HS256')
        nuevo_usuario.token = token
        #guardamos el registro
        nuevo_usuario.save()
        return JsonResponse({"status": "usuario registrado"})
        
@csrf_exempt
#falta: implementar valicadiones a los cmapos
#método para modificar usuarios
#POST: curl -X PATCH http://localhost:8000/usuarios/52/modificar -d "{\"nombre\" : \"usuario modificado\"}"
def mod_usuario(request,id_usuario):
    #guardamos las peticiones
    json_peticion = json.loads(request.body)
    #hallamos el usuario en cuestion a partir de la id en la url
    usuario = get_object_or_404(Usuarios,id=id_usuario)
    #si existe el parametro a modificar en la peticion, entonces se modificara
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
        #por ultimo, guardamos los registros modificados
    usuario.save()

    return JsonResponse({"status": "ok"})    


@csrf_exempt            
#metodo para eliminar un usuario en concreto que será pasado por url
#POST: curl -X POST http://localhost:8000/usuarios/54/borrar
def delete_user(request,id_usuario):
    #hallamos dicho usuario
    usuario = Usuarios.objects.get(id = id_usuario)
    #funcion para eliminar:
    usuario.delete()
    
    return JsonResponse({"status": "usuario eliminado"})


#metodo para mostrar todos los productos de la base de datos
def mostrarProductos(request):
    #guardamos todos los ojetos en producto
    producto = Producto.objects.all()
    #ininicalizamos rray vacio que contendrá todos los registros
    mostrar_productos = []
    #recorremos la variable producto
    for data in producto:
        #guardamos todos los campos->registro en la lista respuesta
        respuesta={}
        respuesta['id'] = data.id 
        respuesta['nombre'] = data.nombre
        respuesta['estado'] = data.estado     
        #la variable usuarios contendrá el los datos de los vendedores de cada producto
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
        #concatenacion
        mostrar_productos.append(respuesta)
    
    return JsonResponse(mostrar_productos, safe=False)

#metodo para mostrar un producto en concreto
def mostrarProductoID(request,id_producto):
    #esta variable guarda los datos del producto en cuestion
    productos = Producto.objects.get(id = id_producto)
    #en esta variable guardamos los datos de los vendedores
    usuario = Usuarios.objects.get(id = productos.vendedor.id)
    #inicializamos array vacío y luego lo concatenamos con la lista diccionario
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

#metodo para verificar si algun campo a la hora de registrar un producto está vacio
def campo_vacio_de_productos(nombre,estado,estacion,precio,color,talla,categoria,fecha):
    if len(nombre) == 0 or len(estado) == 0 or len(estacion) == 0 or precio == "" or len(color) == 0 or talla == "" or len(categoria) == 0 or len(fecha) == 0:
        return True
    else:
        return False
    
@csrf_exempt   
#falta: validar estos campos
#POST: curl -X POST http://localhost:8000/productos/crear -d "{\"nombre\" : \"jordan2\", \"estado\" : \"nuevo\", \"estacion\" : \"verano\", \"precio\" : \"298.99\", \"color\" : \"rojo\",\"talla\":\"43\",\"categoria\" : \"sneaker\", \"fecha\" : \"2022-01-01\" , \"vendedor\" : \"51\"}"
def crearProducto(request):
    #guardamos las peticiones en josn_peticion y asignamos un valor a cada una
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
    #hallamos los datos del vendedor
    #verigicamos  si los campos estan vacios
    usuario = get_object_or_404(Usuarios,id = vendedor)
    if campo_vacio_de_productos(nombre,estado,estacion,precio,color,talla,categoria,fecha) == False:
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
        #si todo etá bien, guardamos registros
        nuevo_producto.save()
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status" : "error"})

@csrf_exempt  
#metodo para eliminar un producto en concreto pasado por url
#POST: curl -X POST http://localhost:8000/productos/2/eliminar
def delete_producto(request, id_producto):
    #hallamos dicho producto
    producto = Producto.objects.get(id = id_producto)
    #mfucnion para eliminar
    producto.delete()
    return JsonResponse({"status": "producto eliminado"})

@csrf_exempt  
#falta: hacer un post en vez de ser hardocdeado
#POST: curl -X POST http://localhost:8000/productos/2/comentarios/crear -H "Auth-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJ1c2VybmFtZSI6InJpY2FyZG8ifQ.IUHsO5s8BK0oI46zzFg2aSQ-QkZgoTC_OnqefESkiiA" -d "{\"comentario\" : \"comentario por curl\", \"valoracion\" : \"5\"}"
def crear_comentarios_al_producto(request,id_producto):
    #guardamos el producto en concreto para crearle un comentario
    productoID = get_object_or_404(Producto, pk = id_producto)
    #guardamos el token que recibira opr cabecera para identificar al usuario
    token_header = request.headers.get("Auth-Token")
    #guardaoms las peticiones
    json_peticion = json.loads(request.body)
    comentario = json_peticion['comentario']
    valoracion = json_peticion['valoracion']
    #hallamos dicho usuario a partir del token
    usuarioID = Usuarios.objects.get(token = token_header)
    #guardamos los registros
    nuevo_comentario = Comentario()
    nuevo_comentario.id_usuario = usuarioID
    nuevo_comentario.id_producto = productoID
    nuevo_comentario.comentario = comentario
    nuevo_comentario.valoracion = valoracion
    nuevo_comentario.fecha = datetime.now()
    nuevo_comentario.save()
    return JsonResponse({"status" : "ok"})

#metodo para mostrar todos los comentarios de un producto
def mostrar_comentarios_por_id(request,id_prod):
    #hallamos dicho producto a partir del id pasado por url
    producto = Producto.objects.get(id = id_prod)
    #guardamos los registros que contengan el mismo id del prducto de la tabla comentarios
    comentarios = Comentario.objects.filter(id_producto = id_prod)
    #inicializamos array vacio
    lista_comentario = []
    #recorremos los comentarios
    for data in comentarios:
        diccionario={}
        diccionario['id'] = data.id
        diccionario['comentarios'] = data.comentario
        diccionario['fecha_creacion'] = data.fecha
        #concatensmoa la lista
        lista_comentario.append(diccionario)
        #resultado final:
    resultado = {
        'id' : producto.id,
        'nombre' : producto.nombre,
        'fecha' : producto.fecha_de_subida,
        'comentario' : lista_comentario
    }
    
    return JsonResponse(resultado,safe=False)

@csrf_exempt 
#falta(o no ): hacer un post
#POST: curl -X POST http://localhost:8000/favoritos/producto/2/anadir -H "Auth-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJ1c2VybmFtZSI6InVzdWFyaW8yIn0.mjHlliE8bjaE1vHXC6YK7a3MrK-lfD_KQUSAj4srURs"
def anadir_favorito(request,producto_id):
    #guardamos el producto en concreto a partir de la id en la url
    producto = get_object_or_404(Producto,pk = producto_id)
    #guardamos el token de la cabecera
    token_header = request.headers.get("Auth-Token")
    #hallamos el usuario a partir del token
    usuario = Usuarios.objects.get(token = token_header)
    #guardamos el registro
    nuevo_favorito = Favoritos()
    nuevo_favorito.id_usuarios = usuario
    nuevo_favorito.id_producto = producto
    nuevo_favorito.fecha = datetime.now()
    nuevo_favorito.save()
    return JsonResponse({"status":"favorito añadido"})

    
#metodo para mostrar los productos favoritos
def mostrar_favoritos(request):
    #recogemos todos los datos de la tabla favoritos
    favoritos = Favoritos.objects.all()
    #iniciallizamos array vacio
    lista_favoritos = []
    #recorremos los objectos guardados en favoritos
    for data in favoritos:
        #los guardamos en una lista/diccionario
        diccionario = {}
        diccionario['id'] = data.id
        diccionario['id_producto'] = data.id_producto.id
        diccionario['id_usuarios'] = data.id_usuarios.id
        diccionario['fecha'] = datetime.now()
        #guardamos el nombre del usuario y el producto en cuestion
        usuario = Usuarios.objects.get(id = data.id_usuarios.id)
        diccionario['nombre_usuario'] = usuario.nombre
        producto = Producto.objects.get(id = data.id_producto.id)
        diccionario['nombre_producto'] = producto.nombre
        #concatenamos
        lista_favoritos.append(diccionario)
        
    return JsonResponse(lista_favoritos,safe=False)

#metodo para mostrar un favorto en concreto a partird de una id que sera pasada por url
def mostrar_favoritoID(request, favorito_id):
    #guardamos el producto favorito en concreto a partid de la id
    favorito = Favoritos.objects.get(id=favorito_id)
    #guardamos el producto que coincida con con el id_producto de la tabla favoritos
    producto = Producto.objects.filter(id = favorito.id_producto.id)
    #guardamos el usuario que concida con el id_usuarios de la tabla favoritos
    usuario = Usuarios.objects.filter(id = favorito.id_usuarios.id)
    #inicializamos 2 arrays vacios para guardar usuarios y productos
    lista_favorito = []
    lista_favorito2 = []
    for data in usuario:
        diccionario = {}
        diccionario['id'] = data.id
        diccionario['nombre_usuario'] = data.nombre
        #concatenamos
        lista_favorito.append(diccionario)
    for data in producto:
        diccionario2={}
        diccionario2['id'] = data.id
        diccionario2['nombre'] = data.nombre
        #conctanemos
        lista_favorito2.append(diccionario2)
        #resultado:
    resultado = {
        'id' : favorito.id,
        'id_usuario' : favorito.id_usuarios.id,
        'id_producto' : favorito.id_producto.id,
        'fecha' : favorito.fecha,
        'usuario' : lista_favorito,
        'producto' : lista_favorito2
        
    }
    
    return JsonResponse(resultado,safe=False)

#metodo para mostrar los productos favoritos de un usuario en concreto que le pasara por url
#error

def mostrar_favoritos_de_usuario(request, id_user):
    """
    #guardamos el usuario que coicnida con el id de la url
    usuario = Usuarios.objects.get(id = id_user)
    #guardamos los favoritos que coincidan con id_usuarios de la tabla favoritos
    favoritos = Favoritos.objects.get(id_usuarios = usuario)
    
    lista_favoritos = []
    for data in favoritos:
        diccionario = {}
        diccionario['id'] = data.id
        diccionario['id_producto'] = data.id_producto.nombre
        diccionario['nombre_producto'] = data.id_producto.nombre
        diccionario['fecha'] = data.fecha
        lista_favoritos.append(diccionario)
        
    return JsonResponse(lista_favoritos,safe=False)
    """
    


    

@csrf_exempt 
#metodo para eliminar un producto favorito que corresponde a un usuario que se le pasara por cabcera
#POST: curl -X POST http://localhost:8000/favoritos/producto/2/eliminar -H "Auth-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJ1c2VybmFtZSI6IjFyaWNhcmRvMTIzMTIzIn0.GE2jYAurfdX92h-Iqvo-EcdvIHRDpbDwgG8Y308JYwo"
def delete_favorito(request,producto_id):
    #guardamos el token que se pasa por cabecera    
    token_header = request.headers.get("Auth-Token")
    #hallamos el usuario a partir del token
    usuario = Usuarios.objects.get(token = token_header)
    #filtramos un favorito para que guarde solo los que coincidan con e id_usuarios e id_producto
    favorito = Favoritos.objects.get(id_producto = producto_id, id_usuarios = usuario.id)
    #funcion par aeliminar 
    favorito.delete()
    return JsonResponse({"status" : "producto eliminado"})



@csrf_exempt 
#POST: curl -X POST http://localhost:8000/compra/2 -H "Auth-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJ1c2VybmFtZSI6InJpY2FyZG8ifQ.IUHsO5s8BK0oI46zzFg2aSQ-QkZgoTC_OnqefESkiiA"
def crear_compra(request,producto_id):
    token_header = request.headers.get("Auth-Token")
    usuario = Usuarios.objects.get(token = token_header)
    producto = Producto.objects.get(id = producto_id)
    nueva_compra = Compra()
    nueva_compra.id_comprador = usuario
    nueva_compra.id_producto = producto
    nueva_compra.fecha = datetime.now()
    nueva_compra.save()
    
    return JsonResponse({"status" : "compra creada"})


#falta: mostrar los datos de los productos y usuarios
def mostrar_compras(request):
    compras = Compra.objects.all()
    
    lista_compras = []
    for data in compras:
        diccionario = {}
        diccionario['id'] = data.id 
        diccionario['fecha'] = data.fecha
        usuario = Usuarios.objects.get(id = data.id_comprador.id)
        diccionario['nombre_comprador'] = usuario.nombre
        diccionario['direccion_comprador'] = usuario.direccion
        diccionario['correo_comprado'] = usuario.correo
        producto = Producto.objects.get(id = data.id_producto.id)
        diccionario['nombre_producto'] = producto.nombre
        diccionario['estado_producto'] = producto.estado
        diccionario['precio_comprador'] = producto.precio
        lista_compras.append(diccionario)
    return JsonResponse(lista_compras, safe=False)




def eliminar_compra(request, id_compra):
    compra = Compra.objects.get(id = id_compra)
    compra.delete()
    return JsonResponse({"status" : "compra eliminada"})


#falta hacer la cabecera