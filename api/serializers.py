from caosNews.models import Noticia, Categoria
from rest_framework import serializers

class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        #fields = ["titulo","autor","descripcion","categoria"]
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"