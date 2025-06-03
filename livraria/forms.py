from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book, Tag, Categoria

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuário'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        self.fields['password2'].label = ''

class BookForm(forms.ModelForm):
    #    title = forms.CharField(required=True,
    #        widget=forms.TextInput(attrs={'placeholder': 'Título Livro', "class": "form-control"}),
    #         label='')
        
    #    description = forms.CharField(required=True,
    #         widget=forms.Textarea(attrs={'placeholder': 'Descrição Livro', "class": "form-control"}),
    #         label='')

    #     year = forms.IntegerField(required=True,
    #         widget=forms.NumberInput(attrs={'placeholder': 'Ano Livro', "class": "form-control"}),
    #         label='')

    #    genre = forms.CharField(required=True,
    #         widget=forms.TextInput(attrs={'placeholder': 'Gênero Livro', "class": "form-control"}),
    #         label='')

    #    value = forms.IntegerField(required=True,
    #         widget=forms.NumberInput(attrs={'placeholder': 'Valor Livro', "class": "form-control"}),
    #         label='')

    class Meta:
        model = Book
        fields = ('title', 'description', 'year', 'genre', 'value', 'categoria', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do livro'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição do livro',
                'rows': 4
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ano de publicação'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Gênero do livro'
            }),
            'value': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Valor do livro',
                'step': '0.01'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'year': 'Ano',
            'genre': 'Gênero',
            'value': 'Valor',
            'categoria': 'Categoria',
            'tags': 'Tags'
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecione uma categoria"
        self.fields['categoria'].required = False
        self.fields['tags'].required = False
        
    
    