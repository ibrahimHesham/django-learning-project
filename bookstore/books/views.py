from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BooksForm
from .models import Books
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import api_view
from .serializers import BookSerializers
from rest_framework.response import Response
from rest_framework import status

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

@login_required()
@permission_required('books.view_books',raise_exception=True)
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


@api_view(['GET','POST'])
def books_list(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializers = BookSerializers(books,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = BookSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def books_details(request,pk):
    try:
        book = Books.objects.get(pk=pk)
        print("book hena")
    except Books.DoesNotExist:
        print("in not found")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = BookSerializers(book)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = BookSerializers(book,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

