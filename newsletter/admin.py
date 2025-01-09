from django.contrib import admin

# Register your models here.
from .models import NewsletterSubscriber

admin.site.register(NewsletterSubscriber)
