import json
import hashlib
import requests
import uuid
from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Order, OrderItem, Product
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .paystack import checkout


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@csrf_exempt
@require_POST
def create_paystack_checkout_session(request, product_id):
    product = Product.objects.get(id=product_id)

    data = json.loads(request.body)
    email = data.get("email")
    qty = int(data.get("qty", 1))

    if not email:
        return JsonResponse({"error": "Email is required"}, status=400)

    purchase_id = f"purchase_{uuid.uuid4()}"
    callback_url = f"{request.scheme}://{request.get_host()}{reverse('payment-success', kwargs={'product_id': product_id})}"

    checkout_data = {
        "email": email,
        "amount": int(product.price * 100 * qty),
        "currency": "USD",
        "channels": ["card", "bank_transfer", "bank", "ussd"],
        "reference": purchase_id,
        "callback_url": callback_url,
        "metadata": {
            "product_id": product_id,
            "purchase_id": purchase_id,
            "qty": qty,
        },
        "label": f"Checkout For {product.name}"
    }

    status, url_or_error = checkout(checkout_data)

    if status:
        return JsonResponse({"redirect_url": url_or_error})
    else:
        return JsonResponse({"error": url_or_error}, status=400)


import hmac
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from .models import Order

@csrf_exempt
def paystack_webhook(request):
    secret = settings.PAYSTACK_SECRET_KEY
    request_body = request.body

    computed_hash = hmac.new(
        secret.encode("utf-8"),
        request_body,
        hashlib.sha512
    ).hexdigest()

    paystack_signature = request.META.get("HTTP_X_PAYSTACK_SIGNATURE")

    if computed_hash != paystack_signature:
        return HttpResponse(status=400)

    webhook_post_data = json.loads(request_body)

    if webhook_post_data["event"] == "charge.success":
        metadata = webhook_post_data["data"]["metadata"]

        product_id = metadata["product_id"]
        user_id = metadata["user_id"]
        purchase_id = metadata["purchase_id"]

        Order.objects.create(
            purchase_id=purchase_id,
            user=User.objects.get(id=user_id),
            purchase_status=True
        )

    return HttpResponse(status=200)

def payment_success(request, product_id):
    # You can render a simple success page or redirect somewhere
    return render(request, 'shop/payment_success.html', {'product_id': product_id})


from django.shortcuts import render, get_object_or_404
from .models import Product

def payment_success(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get query params from Paystack
    trxref = request.GET.get('trxref')
    reference = request.GET.get('reference')

    context = {
        'product': product,
        'trxref': trxref,
        'reference': reference
    }

    return render(request, 'shop/payment_success.html', context)

