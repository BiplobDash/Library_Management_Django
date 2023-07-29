from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Wishlist, BorrowedBook
admin.site.register(Book)
admin.site.register(Wishlist)
admin.site.register(BorrowedBook)