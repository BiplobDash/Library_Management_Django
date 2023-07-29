
# Create your views here.
from django.shortcuts import render, redirect
from .models import Book, Wishlist, BorrowedBook
from django.contrib.auth.decorators import login_required

def book_catalog(request):
    books = Book.objects.all()
    return render(request, 'book_catalog.html', {'books': books})

def book_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'book_search_results.html', {'books': books})

@login_required
def add_to_wishlist(request, book_id):
    book = Book.objects.get(pk=book_id)
    Wishlist.objects.create(user=request.user, book=book)
    return redirect('book_catalog')

@login_required
def view_wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})