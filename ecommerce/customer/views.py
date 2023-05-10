import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
from .forms import CustomerForm

@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        data = {
            'customers': [
                {
                    'id': customer.id,
                    'name': customer.name,
                    'email': customer.email,
                    'phone_number': customer.phone_number,
                    'address': customer.address
                } for customer in customers
            ]
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            data = {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'phone_number': customer.phone_number,
                'address': customer.address
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=201)
        else:
            data = {
                'error': 'Invalid data'
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=400)

@csrf_exempt
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'GET':
        data = {
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
            'phone_number': customer.phone_number,
            'address': customer.address
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    elif request.method == 'PUT':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            data = {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'phone_number': customer.phone_number,
                'address': customer.address
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                'error': 'Invalid data'
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=400)

    elif request.method == 'DELETE':
        customer.delete()
        data = {
            'message': 'Customer deleted successfully'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
