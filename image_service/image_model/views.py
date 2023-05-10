from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Image

# Create your views here.
def get_image1(product_id):
    images = Image.objects.filter(product_id = product_id).values()
    list1 = []
    for item in images:
        list1.append(str(item['image']))
    return list1

@csrf_exempt
def get_image(request):
    product_id = request.POST.get("Product Id")
    resp = {}
    if product_id:
        images = get_image1(product_id)
        images = list(map(lambda x: request.get_host()+"/"+x, images))
        resp['status'] = 'Success'
        resp['status_code'] = '400'
        resp['data'] = images
        
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Cần nhập đủ trường'
    
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def add_image(request):
    return