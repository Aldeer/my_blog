from django.db import models
from ckeditor.fields import RichTextField

class Publicacion(models.Model):

    titulo = models.CharField('Titulo', max_length=200, null=False, blank=False)
    descripcion = models.CharField('Descripcion', max_length=200, null=False, blank=False)
    contenido = RichTextField('Contenido')
    portada = models.URLField('Portada', max_length=255, null=False, blank=False)
    creado = models.DateTimeField('Fecha de publicacion', auto_now=False,auto_now_add=True)
    modificado = models.DateTimeField('Ultima modificacion', auto_now=True, auto_now_add=False)
    activo = models.BooleanField('Publicacion activa', default=True)


    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return f'{self.titulo}'