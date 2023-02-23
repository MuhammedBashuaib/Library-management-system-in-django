from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

#index page
def index(request):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'frmAddBook': FrmBook(),
        'frmAddCategory': FrmCategory(),
        'allBooks': Book.objects.filter(active = True).count(),
        'bookSold': Book.objects.filter(status = 'sold').count(),
        'bookRental': Book.objects.filter(status = 'rental').count(),
        'bookAvailble': Book.objects.filter(status = 'availble').count(),
    }

    #save the book from index page
    if request.method == 'POST':
        addBook = FrmBook(request.POST, request.FILES)
        if addBook.is_valid():
            addBook.save()

    #save the category form sidebar
    if request.method == 'POST':
        addCategory = FrmCategory(request.POST)
        if addCategory.is_valid():
            addCategory.save()

    return render(request, 'pages/index.html', context)

#################################################
#books page
def books(request):
    #Search
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'category': Category.objects.all(),
        'books': search,
        'frmAddCategory': FrmCategory(),
    }
    return render(request, 'pages/books.html', context)

#################################################
#update page
def update(request, id):
    idBook = Book.objects.get(id= id)
    if request.method == 'POST':
        modifiBook = FrmBook(request.POST, request.FILES, instance= idBook)
        if modifiBook.is_valid():
            modifiBook.save()
            return redirect('/')
    else:
        modifiBook = FrmBook(instance= idBook)
        
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'frmBook': modifiBook,
    }
    return render(request, 'pages/update.html', context)

#################################################
#update delete
def delete(request, id):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
    }
    deleteBook = get_object_or_404(Book, id= id)
    if request.method == 'POST':
        deleteBook.delete()
        return redirect('/')
    return render(request, 'pages/delete.html', context)
