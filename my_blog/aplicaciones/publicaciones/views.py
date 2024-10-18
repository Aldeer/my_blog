from django.shortcuts import render
from .models import Publicacion


def home(request):
    return render(request, 'index.html')

def publicaciones(request):
    publicaciones = Publicacion.objects.filter(activo=True)
    print(publicaciones)
    context = {
        'publicaciones':publicaciones
    }
    return render(request, 'publicaciones.html', context=context)

def publicacion(request, titulo):
    publicacion = Publicacion.objects.get(titulo=titulo)
    print(titulo)
    return render(request, 'publicacion.html', {'publicacion':publicacion})