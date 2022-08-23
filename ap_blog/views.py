from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Entrada
from .serializers import PostSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Entrada.objects.all()