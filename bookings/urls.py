from django.urls import path
from .views import index, book_table

urlpatterns = [
    path('', index, name='home'),
    path('booktable/', book_table, name='book_table'),
]
