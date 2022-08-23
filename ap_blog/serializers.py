from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Entrada

class PostSerializer(ModelSerializer):
    class Meta:
        model = Entrada
        fields = ['id', 'titulo', 'contenido']
