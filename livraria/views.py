from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addBookForm
from .models import Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        # Autenticando
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(
                request,
                "Login realizado com sucesso!"
            )
            return redirect('home')
        else:
            messages.error(
                request,
                "Erro na autenticação. Tente novamente!"
                )
            return redirect('home')
    else:
        return render(request, 'home.html', {'books':books})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(
        request,
        "Você fez o logout com sucesso!"
    )
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você fez login com sucesso com novo usuário")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def book_detail(request, id):
    if request.user.is_authenticated:
        book= Book.objects.get(id=id)
        return render(request, 'book.html', {'book':book})
    else:
        messages.error(request, 'Você precisa estar logado!')
        return redirect('home')

def book_delete(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        messages.sucess(request, 'Livro excluido com sucesso!')
        return redirect('home')
    else:
        messages.error(request, 'Você preicsa estar logado!')
        return redirect('home')
    
def book_add(request):
    form= addBookForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = addBookForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "livro adicionado com sucesso!")
                return redirect('home')
        return render(request, 'add_book.html', {'form': form})
    else:
        messages.error(request, 'Você deve star autenticado para adicionar')
        return redirect('home')