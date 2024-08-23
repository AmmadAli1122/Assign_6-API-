from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
from functools import reduce


'''def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
'''
@csrf_exempt
def operation(request): 
    json_data = json.loads(request.body)
    numbers = json_data.get('numbers')
    total = sum(numbers)
    average = total / len(numbers)
    product = reduce(lambda num1, num2: num1 * num2, numbers)
    return JsonResponse({
        'total': total,
        'average': average,
        'product': product
    })