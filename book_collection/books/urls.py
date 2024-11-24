from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/recommendation/', views.book_recommendation, name='book_recommendation'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
]