from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('biography/', views.biography, name='biography'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
