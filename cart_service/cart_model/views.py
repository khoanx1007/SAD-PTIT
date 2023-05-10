from __future__ import unicode_literals

from django.shortcuts import render
from .models import cart_item as citem
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def get_cart_item(username):
    cart_items = citem.objects.filter(
        username=username, status='actived').values()
    list1 = []
    for cart_item in cart_items:
        list1.append(cart_item)
    return list1

# Create your views here.


@csrf_exempt
def get_cart(request):
    uname = request.POST.get("User Name")
    resp = {}
    if uname:
        # asda
        respdata = get_cart_item(uname)
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = respdata

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

def update_cart1(id, username, product_id, quantity, price, status):
    item = citem.objects.get(id=id)
    item.username = username
    item.product_id = product_id
    item.quantity = quantity
    item.price = price
    item.status = status
    item.save()
    return 1
@csrf_exempt
def update_cart(request):
    
    resp = {}

    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            id = val1.get('Id')
            username = val1.get('Username')
            product_id = val1.get('Product Id')
            quantity = val1.get('Quantity')
            price = val1.get('Price')
            status = val1.get('Status')
            update_cart1(id, username, product_id, quantity, price, status)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Update Cart Item Completed'

        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

def add_cart1(username, product_id, quantity, price, status):
    item = citem(username=username, product_id=product_id, quantity=quantity, price=price, status=status)
    print("-----------sadada")
    item.save()
    return 1
    
@csrf_exempt
def add_cart(request):
    
    resp = {}

    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            username = val1.get('Username')
            product_id = val1.get('Product Id')
            quantity = val1.get('Quantity')
            price = val1.get('Price')
            status = val1.get('Status')
            if username and product_id and quantity and price and status:   
                add_cart1(username, product_id, quantity, price, status)
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Add Cart Item Completed'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'

    return HttpResponse(json.dumps(resp), content_type='application/json')