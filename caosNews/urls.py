from django.contrib import admin
from django.urls import path
from .views import index, galeria, autores, registro, nosotros, contacto, iniciar, registrarse,noti, filtro_categoria, filtro_autor, cerrar_sesion, eliminar

urlpatterns = [
    path('',index,name='IND'),
    path('gale/',galeria,name='GALE'),
    path('autores/',autores,name='AUTOR'),
    path('registro/',registro, name='REG'),
    path('nosotros/',nosotros, name='NOS'),
    path('contacto/',contacto, name='CONT'),
    path('iniciar/',iniciar, name='INICIAR'),
    path('registrarse/',registrarse, name='REGISTRARSE'),
    path('noti/<id>',noti, name='NOTI'),
    path('filtro_c/',filtro_categoria,name='FILTROC'),
    path('cerrar/',cerrar_sesion,name='CERRAR'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('filtro_a/',filtro_autor,name='FILTROA'),
]