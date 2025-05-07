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

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@csrf_exempt
@require_POST
def process_payment(request):
    """Process successful payment and create order"""
    try:
        data = json.loads(request.body)
        
        # Extract data from request
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        transaction_id = data.get('transaction_id')
        remita_reference = data.get('remita_reference')
        amount = float(data.get('amount', 0))
        
        # Validate product exists
        product = get_object_or_404(Product, id=product_id)
        
        # Create order
        order = Order.objects.create(
            order_number=uuid.uuid4().hex[:10].upper(),
            first_name=first_name,
            last_name=last_name,
            email=email,
            total_amount=amount,
            payment_status='PAID',
            payment_method='Remita',
            transaction_id=transaction_id,
            payment_reference=remita_reference
        )
        
        # Create order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price,
            total=quantity * product.price
        )
        
        # Send confirmation email
        # send_order_confirmation_email(order)
        
        return JsonResponse({
            'status': 'success',
            'message': 'Order processed successfully',
            'order_id': order.order_number
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

def order_confirmation(request):
    """Display order confirmation page"""
    return render(request, 'shop/order_confirmation.html')