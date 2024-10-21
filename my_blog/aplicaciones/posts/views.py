from django.shortcuts import render
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'publicaciones.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'publicacion.html', context)

def crear_post(request):
    form = PostForm()
    context = {'form': form}
    return render(request, 'formulario_post.html', context)