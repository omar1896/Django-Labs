from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import random
from .views import _get_book
from ..models import books_list



def book_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    if books_list:
        books_list.remove(book_object)

    return redirect('bookstore:books-index')   
