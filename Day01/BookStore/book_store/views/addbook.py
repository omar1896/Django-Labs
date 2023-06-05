from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import random
from ..models import Books



def book_add(request):
    return render(request,'addForm.html')   


@csrf_protect
def book_store(request):
   if request.method == 'POST':
    name=request.POST.get('title')
    rate=request.POST.get('rate')
    views=request.POST.get('views')

    description=request.POST.get('description')
    Books.objects.create(title=name,rate=rate,description=description,views=views)

    print(request.POST)

    return redirect('bookstore:books-index') 
   

 