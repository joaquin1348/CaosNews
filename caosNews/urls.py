from django.contrib import admin
from django.urls import path
from .views import index, galeria, noticia1, noticia2, noticia3, autores, registro, nosotros, contacto, iniciar, registrarse,noti, filtro_categoria, filtro_autor, filtro_descripcion, cerrar_sesion, eliminar, error, buscar_modificar, modificar

urlpatterns = [
    path('',index,name='IND'),
    path('gale/',galeria,name='GALE'),
    path('noti1/',noticia1,name='NOTI1'),
    path('noti2/',noticia2,name='NOTI2'),
    path('noti3/',noticia3,name='NOTI3'),
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
    path('filtro_d/',filtro_descripcion,name='FILTROD'),
    path('error/',error,name='ERROR'),
    path('buscar_modificar/<id>/',buscar_modificar,name='BUSCARM'),
    path('modificar/',modificar,name='MODI'),
]