from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BooksForm
from .models import Books

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    books = Books.objects.all()
    return render(request,"books/index.html",{'books':books})

# Create your views here.
def create(request):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/create.html",{'form':form})

def destroy(request, id):  
    book = Books.objects.get(id=id)  
    book.delete()  
    return redirect("index") 

def show(request, id):  
    book = Books.objects.get(id=id)  
    # book.delete()  
    return render(request,"books/show.html",{'book':book})

def edit(request,id):
    # context = {}
    book = Books.objects.get(id=id) 

    form = BooksForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"books/edit.html",{'form':form,'book':book})
