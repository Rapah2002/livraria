from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    value = models.FloatField()
        
    def __str__(self):
        return f'{self.title} - {self.value}'
    
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
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome}'

#class Avaliacao(models.Model):
   # book = models.ForeignKey('Book', on_delete=models.CASCADE)
    # usuario = models.CharField(max_length=100)
    #nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    #comentario = models.TextField()
    #data = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return f"{self.usuario} - {self.book} ({self.nota})"



    


