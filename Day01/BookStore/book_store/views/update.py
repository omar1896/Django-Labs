
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import random
from .views import _get_book
from ..models import books_list


@csrf_protect
def book_edit(request,**kwargs):
   book_id = kwargs.get('book_id')
   print(book_id)
#    book = _get_book(book_id)
#    index
   for i, book in enumerate(books_list):
        if book['id'] == book_id:
            print(i)
            index = i
   if request.method == 'POST':
      print('indexxx',index)
      books_list[index]['name']=request.POST.get('name')
      books_list[index]['price']=request.POST.get('price')
      books_list[index]['description']=request.POST.get('description')

      return redirect('bookstore:books-index') 
   



def book_update(request,**kwargs):
     book_id = kwargs.get('book_id')
     book = _get_book(book_id)
     print(book)
     my_context = {
        'book_id': book.get('id'),
        'book_name': book.get('name'),
        'book_price': book.get('price'),
        'book_description': book.get('description')
     }
     return render(request, 'editbook.html', context=my_context)