from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from ..models import Books



def book_delete(request, pk):
  book=Books.objects.get(pk=pk).delete()
  return redirect('bookstore:books-index')   
