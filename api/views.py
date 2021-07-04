from django.shortcuts import render
from rest_framework import generics
from caosNews.models import Noticia
from .serializers import NoticiasSerializer

class NoticiasViewSet(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasSerializer

class NoticiasCreateViewSet(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasSerializer

class NoticiaBuscarViewSet(generics.ListAPIView):
    serializer_class = NoticiasSerializer
    def get_queryset(self):
        nombre_autor = self.kwargs['autor']
        return Noticia.objects.filter(autor=nombre_autor)