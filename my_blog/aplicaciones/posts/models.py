from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    "Clase modelo de publicacion"

    titulo = models.CharField('Titulo', max_length=200, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=200, blank=False, null=False)
    contenido = RichTextField('Contenido')
    portada = models.URLField('Portada', blank=False, null=False)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Ultima modificacion', auto_now=True, auto_now_add=False)
    activo = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.titulo}'


