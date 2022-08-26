from django.urls import path

from . import views
# from .views import api_:home

urlpatterns = [
    path('', views.api_home)
]