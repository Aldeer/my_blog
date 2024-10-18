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