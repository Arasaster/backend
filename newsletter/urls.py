# newsletter/urls.py

from django.urls import path
from .views import subscribe_newsletter

app_name = 'newsletter'  # 👈 this is key

urlpatterns = [
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
]
