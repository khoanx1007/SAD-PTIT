from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse



from .models import comment_detail
# Create your views here.
def get_comment_details(product):
    comments = comment_detail.objects.filter(product_id = product).values()
    list1 = []
    for comment in comments:
        list1.append(comment)
    return list1
	
def store_comment(product_id, username, comment):
    comment = comment_detail(product_id=product_id, username=username, comment=comment)
    print("--------abc", comment)
    
    comment.save()
    return 1

@csrf_exempt
def get_comment(request):
    if request.method == 'POST':
        
        if 'application/json' in request.META['CONTENT_TYPE']:            
            val1 = json.loads(request.body)
            product = val1.get('Product Id')
            resp = {}
            if product:
                ## Calling the getting the user info.
                respdata = get_comment_details(product)
                
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = respdata

                ### If user is not found then it give failed as response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Product Not Found.'

            ### It will field value is missing.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@csrf_exempt
def add_comment(request):
    product_id = request.POST.get("Product Id")
    username = request.POST.get("Username")
    comment = request.POST.get("Comment")
 
    resp = {}
    if product_id and username and comment:
        respdata = store_comment(product_id, username, comment)
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Add comment is completed.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Add comment is failed.'
    
	### If any mandatory field is missing then it will through failed message.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')