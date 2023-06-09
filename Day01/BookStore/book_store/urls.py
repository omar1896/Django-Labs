from django.urls import path
# from ..views import index ,book_detail,book_delete,book_update,book_list,book_add,book_store,book_edit,book_add
from .views.views import *
from .views .addbook import *
from .views .delete import *
from .views .update import *

app_name = 'bookstore'


urlpatterns = [
    path('index', index, name='books-index'),
    path('book_add', book_add, name="book-add"),
    path('book_store', book_store, name="book-store"),
    path('book_detail/<int:pk>', book_detail, name="book-detail"),
    path('book_delete/<int:pk>', book_delete, name="book-delete"),
    path('book_update/<int:pk>', book_update, name="book-update"),
    path('book_store/<int:pk>', book_edit , name="book-edit"),

]