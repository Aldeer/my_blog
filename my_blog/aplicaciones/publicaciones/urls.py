from django.urls import path
from .views import home, publicaciones

urlpatterns = [
    path('', home, name='home'),
    path('publicaciones/', publicaciones, name='publicaciones')
]