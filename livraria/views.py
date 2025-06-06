from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, BookForm
from .models import Book, Categoria
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home(request):
    # Inicializa o queryset
    books = Book.objects.all().order_by('title')
    
    # Busca
    search_query = request.GET.get('search', '')
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(genre__icontains=search_query)
        )
    
    # Filtros
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        books = books.filter(categoria_id=categoria_id)
    
    genre = request.GET.get('genre')
    if genre:
        books = books.filter(genre=genre)
    
    # Ordenação
    order_by = request.GET.get('order_by', 'title')
    if order_by in ['title', '-title', 'year', '-year', 'value', '-value']:
        books = books.order_by(order_by)
    
    # Paginação
    paginator = Paginator(books, 10)  # 10 livros por página
    page = request.GET.get('page')
    books = paginator.get_page(page)
    
    # Dados para os filtros
    categorias = Categoria.objects.all()
    genres = Book.objects.values_list('genre', flat=True).distinct()
    
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro na autenticação. Tente novamente!")
            return redirect('home')
    
    context = {
        'books': books,
        'categorias': categorias,
        'genres': genres,
        'search_query': search_query,
        'selected_categoria': categoria_id,
        'selected_genre': genre,
        'order_by': order_by,
    }
    
    return render(request, 'home.html', context)

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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
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

def book_delete(request, id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(id=id)
            book.delete()
            messages.success(request, 'Livro excluído com sucesso!')
        except Book.DoesNotExist:
            messages.error(request, 'Livro não encontrado.')
        return redirect('home')
    else:
        messages.error(request, 'Você precisa estar logado!')
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

from .models import Book
from .forms import BookForm

# 1. Classe para Criar
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            book = form.save(commit=False)
            book.save()
            messages.success(self.request, "Livro adicionado com sucesso!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Você precisa estar logado para adicionar um livro!")
            return redirect('home')

# 2. Classe para Editar
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Você precisa estar logado!")
            return redirect('home')
        if not request.user.is_staff:
            messages.error(request, "Você não tem permissão para editar livros!")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        book = form.save(commit=False)
        book.save()
        messages.success(self.request, "Livro atualizado com sucesso!")
        return super().form_valid(form)

# 3. Classe para Detalhar
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            book = self.get_object()
            context['book'] = book
            return context
        else:
            messages.error(self.request, "Você precisa estar logado para visualizar os detalhes!")
            return redirect('home')

# 4. Classe para Deletar
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            try:
                book = self.get_object()
                book.delete()
                messages.success(self.request, "Livro excluído com sucesso!")
            except Book.DoesNotExist:
                messages.error(self.request, "Livro não encontrado!")
        else:
            messages.error(self.request, "Você precisa estar logado para excluir!")
            return redirect('home')
        return super().delete(request, *args, **kwargs)