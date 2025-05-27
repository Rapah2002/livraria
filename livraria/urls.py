from django.urls import path
from livraria.views import (
    home, logout_user, register_user, login_user,
    book_detail, book_delete, book_add,
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView
)

urlpatterns = [
    # Views baseadas em função
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('book/<int:id>/', book_detail, name='book'),
    path('delete_book/<int:id>/', book_delete, name='delete_book'),
    path('add_book/', book_add, name='add_book'),

    # Views baseadas em classe (CRUD)
    path('livros/', BookListView.as_view(), name='book_list'),
    path('livro/novo/', BookCreateView.as_view(), name='book_create'),
    path('livro/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('livro/<int:pk>/editar/', BookUpdateView.as_view(), name='book_update'),
    path('livro/<int:pk>/deletar/', BookDeleteView.as_view(), name='book_delete'),
]