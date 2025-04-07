from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('shop/<int:product_id>/', views.product_detail, name='product_detail'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path("webhook/paystack/", views.paystack_webhook, name="paystack_webhook"),
]