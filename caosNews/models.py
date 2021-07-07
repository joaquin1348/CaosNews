from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_noticia = models.CharField(primary_key=True,max_length=25)
    id_noticia = models.IntegerField() 

    def _str_(self):
        return self.nombre_noticia
class Noticia(models.Model):
    
    titulo = models.CharField(primary_key=True,max_length=80)
    autor = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=350)
    imagen = models.ImageField(upload_to='noticias',null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    comentario = models.TextField (null=True,default='sin comentario')
    publicar = models.BooleanField(default=False)
    
    def _str_(self):
        return self.nombre
class Contacto(models.Model):
    nombre = models.CharField(primary_key=True,max_length=80)
    apellidos = models.TextField(max_length=20)
    correo = models.TextField()
    comentario = models.TextField(max_length=350)

    def __str__(self):
        return self.nombre
