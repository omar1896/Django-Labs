
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from ..models import Books


@csrf_protect
def book_edit(request,pk):
   book= Books.objects.get(pk=pk)
   if request.method == 'POST':
      book.title=request.POST.get('title')
      book.rate=request.POST.get('rate')
      book.views=request.POST.get('views')
      book.description=request.POST.get('description')
      book.save()


   return redirect('bookstore:books-index') 
 



def book_update(request,pk):
    book= Books.objects.get(pk=pk)
    return render(request, 'editbook.html', context={'book':book})
   