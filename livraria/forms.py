from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book, Tag, Categoria

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        help_text='Digite um endereço de email válido'
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        help_text='Digite seu primeiro nome'
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
        help_text='Digite seu sobrenome'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
        Sua senha deve conter:
        • No mínimo 8 caracteres
        • Não pode ser muito similar às suas outras informações pessoais
        • Não pode ser uma senha muito comum
        • Não pode ser totalmente numérica
        '''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = 'Digite a mesma senha novamente para verificação'

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
        
    
    