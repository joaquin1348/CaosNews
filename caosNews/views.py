from django.shortcuts import render
from .models import Categoria, Noticia


#importar al modelo la tabla user
from django.contrib.auth.models import User
#importar libreria para autentificar usuarios
from django.contrib.auth import authenticate,logout,login
#importar una libreria decoradora que evita el ingreso a algunas paginas
from django.contrib.auth.decorators import login_required,permission_required

def index(request):
    noticias = Noticia.objects.all()
    cat = Categoria.objects.all()
    context = {"categorias":cat,"noticias":noticias}
    return render(request,"index2.html",context)


def galeria(request):
    noticias = Noticia.objects.all() #select * from Noticia
    categorias = Categoria.objects.all()
    contexto = {"noticias":noticias,"categorias":categorias}
    return render(request,"galeria.html",contexto)

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

def filtro_autor(request):
    noticias_t = Noticia.objects.all()
    if request.POST:
        autor = request.POST.get("txtAutor")
        noticias_a = Noticia.objects.filter(autor=autor)
        contexto = {"noticias":noticias_t,"noti_a":noticias_a}
        
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
            autor = request.POST.get("txtAutor")
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

    noticia = Noticia.objects.all()    
    contexto = {'Categorias':cate,"mensaje":mensaje,"noticia":noticia}
    return render(request,"registro.html",contexto)
@login_required(login_url='/iniciar/')
@permission_required('caosNews.delete_noticia',login_url='/login')
def eliminar(request,id):
    try:
        noti = Noticia.objects.get(titulo=id)
        noti.delete()
        mensaje = "elimino noticia"
    except:
        mensaje="no elimino noticia"
        
    categorias= Categoria.objects.all()
    noticia = Noticia.objects.all()    
    contexto = {'Categorias':categorias,"mensaje":mensaje,"noticia":noticia}
    return render(request,"registro.html",contexto)