from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('iduser', 'idfilme', 'data_criacao')
    search_fields = ('iduser__username', 'idfilme__titulo', 'coment')
    list_filter = ('data_criacao',)

