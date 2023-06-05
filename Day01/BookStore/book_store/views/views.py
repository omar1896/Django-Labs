
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import random
from ..models import Books

# Create your views here.




 
def index(request, **kwrgs):
  
 books_list=Books.objects.all()
 return render(request,'bookstore.html', context={"books_list":books_list})






def book_detail(request, pk):
  book=Books.objects.get(pk=pk)
  return render(request, 'book-detail.html', context={"book":book})









 


   
   
   

    
    
 
   




   

 