from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['nome']

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    year = models.IntegerField(verbose_name='Ano')
    genre = models.CharField(max_length=30, verbose_name='Gênero')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoria')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Tags')
        
    def __str__(self):
        return f'{self.title} - R$ {self.value}'
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['title']

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(blank=True)
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'

class Categoria(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

#class Avaliacao(models.Model):
   # book = models.ForeignKey('Book', on_delete=models.CASCADE)
    # usuario = models.CharField(max_length=100)
    #nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    #comentario = models.TextField()
    #data = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return f"{self.usuario} - {self.book} ({self.nota})"



    


