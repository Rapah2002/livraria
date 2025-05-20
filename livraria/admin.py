from django.contrib import admin
from .models import Book, Autor, Editora, Categoria

admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Categoria)