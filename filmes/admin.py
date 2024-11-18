from django.contrib import admin
from .models import Filme

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'categoria')
    list_filter = ('categoria', 'ano')
    search_fields = ('titulo', 'descricao')

