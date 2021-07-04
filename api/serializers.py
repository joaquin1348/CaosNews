from caosNews.models import Noticia
from rest_framework import serializers

class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        #fields = ["titulo","autor","descripcion","categoria"]
        fields = "__all__"

