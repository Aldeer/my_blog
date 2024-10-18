from django.contrib import admin

from .models import Publicacion

class PublicacionAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo',)

admin.site.register(Publicacion, PublicacionAdmin)
