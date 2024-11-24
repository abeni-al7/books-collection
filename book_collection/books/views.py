from django.http import JsonResponse, HttpResponseNotAllowed
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

@csrf_exempt
def book_detail(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

    if request.method == 'GET':
        data = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'published_year': book.published_year,
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.isbn = data.get('isbn', book.isbn)
        book.published_year = data.get('published_year', book.published_year)
        book.save()
        return JsonResponse({'message': 'Book updated successfully'})
    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

