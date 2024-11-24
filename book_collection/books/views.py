from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    data = list(books.values())
    return JsonResponse(data, safe=False)

