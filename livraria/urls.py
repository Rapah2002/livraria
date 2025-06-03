from django.urls import path
from livraria.views import (
    home, logout_user, register_user, login_user,
    BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView
)

urlpatterns = [
    # Views baseadas em função
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('cadastro/', register_user, name='register'),
    
    # Views baseadas em classe (CRUD)
    path('livro/novo/', BookCreateView.as_view(), name='book_create'),
    path('livro/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('livro/<int:pk>/editar/', BookUpdateView.as_view(), name='book_update'),
    path('livro/<int:pk>/deletar/', BookDeleteView.as_view(), name='book_delete'),
]