from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.book_catalog, name='book_catalog'),
    path('search/', views.book_search, name='book_search'),
    path('add_to_wishlist/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
]