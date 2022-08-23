from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']
