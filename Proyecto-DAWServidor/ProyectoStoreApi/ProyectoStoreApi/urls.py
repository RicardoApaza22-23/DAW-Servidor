"""ProyectoStoreApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webserviceapp import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #pruebas
    path('prueba/existe', views.usuario_existe_en_bd),
    
    #login
    path('login',views.login),
    
    
    #usuarios -> get
    path('usuarios/<int:id_usuario>', views.mostrarUsuarioID),
    path('usuarios', views.mostrarUsuarios),
    #usuarios -> post
    path('usuarios/registrar', views.registrar),
    path('usuarios/<int:id_usuario>/borrar', views.delete_user),
    path('usuarios/<int:id_usuario>/modificar', views.mod_usuario),
    #productos -> get
    path('productos',views.mostrarProductos),
    path('productos/<int:id_producto>',views.mostrarProductoID),
    
    #productos -> post
    path('productos/crear',views.crearProducto),
    
    
    
    path('productos/<int:id_producto>/comentarios/crear',views.crear_comentarios_al_producto),
    
    #comentarios -> get
    #path('productos/comentarios', views.mostrar_comentarios),
    path('productos/<int:id_prod>/comentarios', views.mostrar_comentarios_por_id),
    
    #favoritos -> get
    path('favoritos',views.mostrar_favoritos),
    path('favoritos/<int:favorito_id>',views.mostrar_favoritoID),
    path('usuario/<int:id_user>/favoritos',views.mostrar_favoritos_de_usuario),
    
    #favoritos -> post
    path('favoritos/producto/<int:producto_id>/añadir', views.añadir_favorito),
    path('favoritos/producto/<int:producto_id>/eliminar', views.delete_favorito),
    
    #compra -> get
    path('compra/mostrar', views.mostrar_compras),
    
    #compra -> post
    path('compra/crear', views.crear_compra)
    


]

