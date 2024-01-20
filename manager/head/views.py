from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
context = {
    'category': Category.objects.all(),
    'book': Book.objects.all(),
    'form':BookForm(),
    'formcat': CategoryForm(),

}
def ca(request):

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
    ca(request)
    return render(request,'pages/index.html', context)
def update(request, id):
    books_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=books_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/head/index')
    else:
        book_save = BookForm(instance= books_id)
    con={'form':book_save,}
    return render(request,'pages/update.html', con)
def delete(request,id):
    book_delete =get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/head/index')
    return render(request,'pages/delete.html')
def books(request):
 return render(request,'pages/books.html', context)