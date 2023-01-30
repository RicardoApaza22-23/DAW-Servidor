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
    
    #usuarios -> get
    path('usuarios/<int:id_usuario>', views.mostrarUsuarioID),
    path('usuarios', views.mostrarUsuarios),
    #usuarios -> post
    path('usuarios/registrar', views.registrar),
    
    #productos -> get
    path('productos',views.mostrarProductos),
    path('productos/<int:id_producto>',views.mostrarProductoID),
    
    #productos -> post
    path('productos/crear',views.crearProducto),
    path('productos/<int:id_producto>/comentarios/crear',views.crear_comentarios_al_producto),
    
    #comentarios -> get
    path('productos/comentarios', views.mostrar_comentarios),
    path('productos/<int:id_producto>/comentarios', views.mostrarProductoID)
    
]

