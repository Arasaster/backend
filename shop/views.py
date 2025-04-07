from django.shortcuts import render

# Create your views here.
from . models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

#replace with proper "product_list.html"

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    amount = product.price
    return render(request, 'shop/product_detail.html', {'product': product})


# core/views.py

import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction, Product

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        ref = request.POST.get('reference')
        email = request.POST.get('email')
        product_id = request.POST.get('product_id')
        amount = request.POST.get('amount')

        url = f"https://api.paystack.co/transaction/verify/{ref}"
        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json',
        }

        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            if data['data']['status'] == 'success':
                name = data['data'].get('customer', {}).get('first_name', '') + " " + data['data'].get('customer', {}).get('last_name', '')
                txn = Transaction.objects.create(
                    reference=ref,
                    email=email,
                    name=name.strip(),
                    product=Product.objects.get(id=product_id),
                    amount=amount,
                    verified=True,
                )
                return JsonResponse({"status": "success", "name": name})
        return JsonResponse({"status": "failed"}, status=400)


# views.py
import json, hmac, hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from .models import Transaction
from django.conf import settings

secret_key = settings.PAYSTACK_SECRET_KEY

@csrf_exempt
def paystack_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_X_PAYSTACK_SIGNATURE')

    expected_sig = hmac.new(
        key=bytes(settings.PAYSTACK_SECRET_KEY, 'utf-8'),
        msg=payload,
        digestmod=hashlib.sha512
    ).hexdigest()

    if sig_header != expected_sig:
        return HttpResponse(status=400)

    event = json.loads(payload)

    if event['event'] == 'charge.success':
        data = event['data']
        reference = data['reference']
        email = data['customer']['email']
        amount = int(data['amount']) / 100  # Convert kobo to dollars

        try:
            tx = Transaction.objects.get(reference=reference)
            tx.verified = True
            tx.save()
        except Transaction.DoesNotExist:
            pass  # Optionally log this

    return HttpResponse(status=200)


