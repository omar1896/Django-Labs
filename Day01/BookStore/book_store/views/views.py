
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import random
from ..models import *



# Create your views here.




def _get_book(book_id):
    for book in books_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None


 
def index(request, **kwrgs):
  
    my_context = {'books_list': books_list}
    return render(request,'bookstore.html', context=my_context)



def book_list(request, **kwrgs):
    my_context = {'books_list': books_list}
    # template_loader > bok/templates/
    return render(request, 'bookstore.html', context=my_context)



def book_detail(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book = _get_book(book_id)
    print(book)
    my_context = {
        'book_id': book.get('id'),
        'book_name': book.get('name'),
        'book_price': book.get('price'),
        'book_description': book.get('description')
    }
    return render(request, 'book-detail.html', context=my_context)









 


   
   
   

    
    
 
   




   

 