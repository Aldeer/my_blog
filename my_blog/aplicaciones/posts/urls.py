from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacion/id=<int:id>', views.detalle_post, name='detalle_post')
]