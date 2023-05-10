from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from .models import Book

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        book_list = json.loads(serializers.serialize('json', books))
        return HttpResponse(json.dumps(book_list), content_type='application/json')
    elif request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        author = data['author']
        description = data['description']
        price = data['price']
        book = Book(title=title, author=author, description=description, price=price)
        book.save()
        data = {'success': True, 'message': 'Book saved successfully!'}
        return JsonResponse(data, content_type='application/json')

@csrf_exempt
def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        data = {'success': False, 'message': 'Book does not exist!'}
        return JsonResponse(data, content_type='application/json', status=404)

    if request.method == 'GET':
        book_detail = json.loads(serializers.serialize('json', [book]))
        return HttpResponse(json.dumps(book_detail), content_type='application/json')
    elif request.method == 'PUT':
        data = json.loads(request.body)
        book.title = data['title']
        book.author = data['author']
        book.description = data['description']
        book.price = data['price']
        book.save()
        data = {'success': True, 'message': 'Book updated successfully!'}
        return JsonResponse(data, content_type='application/json')
    elif request.method == 'DELETE':
        book.delete()
        data = {'success': True, 'message': 'Book deleted successfully!'}
        return JsonResponse(data, content_type='application/json')
