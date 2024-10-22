from django.shortcuts import render
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.filter(activo=True).order_by('-fecha_modificacion')
    context = {'posts': posts}
    return render(request, 'index.html', context)

def detalle_post(request,id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'detalle_post.html', context)