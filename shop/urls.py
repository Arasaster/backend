from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('shop/<int:product_id>/', views.product_detail, name='product_detail'),

    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),

    path('process-payment/', views.process_payment, name='process_payment'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
]