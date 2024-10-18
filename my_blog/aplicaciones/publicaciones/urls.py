from django.urls import path
from .views import home, publicaciones, publicacion

urlpatterns = [
    path('', home, name='home'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('publicaciones/<str:titulo>/', publicacion, name='publicacion')
]