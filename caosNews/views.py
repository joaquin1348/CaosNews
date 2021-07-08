from django.shortcuts import render
from .models import Categoria, Noticia


#importar al modelo la tabla user
from django.contrib.auth.models import User
#importar libreria para autentificar usuarios
from django.contrib.auth import authenticate,logout,login
#importar una libreria decoradora que evita el ingreso a algunas paginas
from django.contrib.auth.decorators import login_required,permission_required

def index(request):
    noticias = Noticia.objects.all()[:3]
    cat = Categoria.objects.all()
    carru_noti= Noticia.objects.filter(publicar=True).order_by('-fecha')[:3]
    context = {"categorias":cat,"noticias":noticias,"carru":carru_noti}
    return render(request,"index2.html",context)


def galeria(request):
    noticias = Noticia.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    contexto = {"noticias":noticias,"categorias":categorias}
    return render(request,"galeria.html",contexto)

def noticia1(request):
    return render(request,"noticia1.html")

def noticia2(request):
    return render(request,"noticia2.html")

def noticia3(request):
    return render(request,"noticia3.html")

def autores(request):
    noticias_t = Noticia.objects.all()
    contexto = {"noticias":noticias_t}
    return render(request,"autores.html",contexto)
    
def nosotros(request):
    return render(request,"nosotros.html")

def contacto(request):
    return render(request,"contacto.html")

def iniciar(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login(request,us) 
            return render(request,"index2.html")
        else:
            mensaje="no existe usuario o contraseña esta incorrecta"
    contexto={"mensaje":mensaje}
    return render(request,"iniciar.html",contexto)

def cerrar_sesion(request):
    logout(request)
    return render(request,"index2.html")

def registrarse(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellidos = request.POST.get("txtApellidos")
        email = request.POST.get("txtEmail")
        nom_usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtPass1")

        usu = User()
        usu.first_name = nombre
        usu.last_name = apellidos
        usu.email = email
        usu.username = nom_usuario
        usu.set_password(pass1)
        usu.save()

        mensaje="Grabo"
    contexto = {"mensaje":mensaje}    
    return render(request,"registrarse.html",contexto)
    
def noti(request, id):
    noticia= Noticia.objects.get(titulo=id)
    contexto = {"noticia":noticia}
    return render(request,"noti.html",contexto)

def filtro_categoria(request):
    noticias = Noticia.objects.all() #select * from Noticia
    categorias = Categoria.objects.all()
    if request.POST:
        cate = request.POST.get("cboCategoria")
        obj_categoria = Categoria.objects.get(nombre_noticia=cate)
        noticias = Noticia.objects.filter(categoria=obj_categoria)
    contexto = {"noticias":noticias,"categorias":categorias}
    return render(request,"galeria.html",contexto)

def filtro_descripcion(request):
    noticias = Noticia.objects.all()
    categorias = Categoria.objects.all()
    if request.POST:
        texto = request.POST.get("txtDesc")
        noticias = Noticia.objects.filter(descripcion__contains=texto)
    contexto = {"noticias":noticias,"categorias":categorias}
    return render(request, "galeria.html",contexto)


def filtro_autor(request):
    noticias_t = Noticia.objects.all()
    cant = Noticia.objects.all().count()
    categorias = Categoria.objects.all()
    if request.POST:
        autor = request.POST.get("txtAutor")
        noticias_a = Noticia.objects.filter(autor=autor)
        cant = Noticia.objects.filter(autor=autor).count()
        contexto = {"noticias":noticias_t,"noti_a":noticias_a,"categorias":categorias,"cantidad":cant}
    return render(request,"autores.html",contexto)
    


@login_required(login_url='/iniciar/')

def registro(request):
    cate=Categoria.objects.all()
    contexto = {'Categorias':cate}
    mensaje=""
    if request.POST:
        try:
            noticia.objects.get(titulo=titulo)
            mensaje= "nombre de noticia existente"
        except:

            titulo = request.POST.get("txtTitulo")
            autor = request.user.username
            desc = request.POST.get("txtDesc")
            categoria = request.POST.get("cboCategoria")
            obj_cate = Categoria.objects.get(nombre_noticia=categoria)
            imagen = request.FILES.get("txtImg")
            noti = Noticia(
            
                titulo=titulo,
                autor=autor,
                descripcion=desc,
                imagen=imagen,
                categoria=obj_cate
            )
            noti.save()
            mensaje='grabo'

    noticia = Noticia.objects.filter(autor=request.user.username)    
    contexto = {'Categorias':cate,"mensaje":mensaje,"noticia":noticia}
    return render(request,"registro.html",contexto)

@login_required(login_url='/iniciar/')
@permission_required('caosNews.delete_noticia',login_url='/error')
def eliminar(request,id):
    try:
        noti = Noticia.objects.get(titulo=id)
        noti.delete()
        mensaje = "elimino noticia"
    except:
        mensaje="no elimino noticia"
        
    categorias= Categoria.objects.all()
    noticia = Noticia.objects.filter(autor=request.user.username)    
    contexto = {'Categorias':categorias,"mensaje":mensaje,"noticia":noticia}
    return render(request,"registro.html",contexto)

def error(request):
    return render(request,"error.html")

@login_required(login_url='/iniciar/')
@permission_required('caosNews.delete_noticia',login_url='/error')
def modificar(request):
    mensaje=""
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        autor = request.user.username
        desc = request.POST.get("txtDesc")
        categoria = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre_noticia=categoria)
        imagen = request.FILES.get("txtImg")

        try:
            noticia = Noticia.objects.get(titulo=titulo)
            noticia.titulo = titulo
            noticia.autor = autor
            noticia.descripcion = desc
            if imagen is not None:
                noticia.imagen = imagen

            noticia.categoria = obj_cate
            noticia.comentario = '--'
            noticia.save()
            mensaje="modifico noticia"
        except:
            mensaje='no modifico'

    cate=Categoria.objects.all()
    noticia = Noticia.objects.filter(autor=request.user.username)    
    contexto = {'Categorias':cate,"mensaje":mensaje,"noticia":noticia}
    return render(request,"registro.html",contexto)

@login_required(login_url='/iniciar/')
def buscar_modificar(request,id):
    try:
        noti = Noticia.objects.get(titulo=id)
        categorias= Categoria.objects.all()
        contexto = {'Categorias':categorias,"noticia":noti}
        return render(request,"modificar.html",contexto)
    except:
        mensaje="no encontro noticia"
        
    categorias= Categoria.objects.all()
    noticia = Noticia.objects.all()    
    contexto = {'Categorias':categorias,"mensaje":mensaje,"noticia":noticia}
    return render(request,"registro.html",contexto)
# permite realizar peticione HTTP
import requests


def consumir_api(request):
    

    response = requests.get("http://127.0.0.1:8787/api/noticias/")
    noticias = response.json()

    response = requests.get("http://127.0.0.1:8787/api/categorias/")
    categorias= response.json()
    if request.POST:
        autor = request.POST.get("txtAutor")
        response = requests.get("http://127.0.0.1:8787/api/noticia/"+autor+"/")
        noticias = response.json()

    contexto = {"noticias":noticias,"categorias":categorias}
    return render(request,"consumir_api.html",contexto)