from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),

    # Checkout first so it doesn’t get swallowed by product_detail
    path("checkout/<int:product_id>/", views.create_paystack_checkout_session, name="checkout-product"),
    path("webhook/paystack/", views.paystack_webhook, name="paystack-webhook"),

    # Product detail URLs
    path('shop/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),
    path("payment-success/<int:product_id>/", views.payment_success, name="payment-success"),
]

