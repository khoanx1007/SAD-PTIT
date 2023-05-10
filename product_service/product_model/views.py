# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details


@csrf_exempt
def get_product_data(request):

    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data   
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')

def book_insert(request):
    url = 'http://127.0.0.1:8008/get_book/'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(data), content_type = 'application/json')

#fix url 
def electronic_insert(request):
    url = 'http://127.0.0.1:8009//'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(data), content_type = 'application/json')
