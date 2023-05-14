from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import random
from ..models import books_list



def book_add(request):
    return render(request,'addForm.html')   


@csrf_protect
def book_store(request):
   if request.method == 'POST':
    name=request.POST.get('name')
    price=request.POST.get('price')
    description=request.POST.get('description')

    newbook={'id':random.randint(1, 100),
             'name':name,
             'price':price,
             'description':description
             }

    books_list.append(newbook)
    print(request.POST)

    return redirect('bookstore:books-index') 
   

 