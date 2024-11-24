from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        data = {"books": list(books.values())}
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            isbn=data['isbn'],
            published_year=data['published_year']
        )
        return JsonResponse({'id': book.id}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

