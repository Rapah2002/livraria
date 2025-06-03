from django.contrib import admin
from .models import Book, Categoria, Tag, Autor, Editora

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'value', 'categoria')
    list_filter = ('genre', 'year', 'categoria', 'tags')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)
    list_per_page = 20

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    list_filter = ('nacionalidade',)
    search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    list_filter = ('cidade',)
    search_fields = ('nome',)