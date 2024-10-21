from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacion/id=<int:pk>', views.post, name='post'),
    path('crear_post/', views.crear_post, name='crear_post')
]