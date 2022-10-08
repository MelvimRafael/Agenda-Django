from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'categoria')
    list_filter = ('nome', 'telefone')
    search_fields = ('nome', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)