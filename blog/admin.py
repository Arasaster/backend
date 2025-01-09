from django.contrib import admin

# Register your models here.
from .models import BlogPost, Comment

admin.site.register(BlogPost)
admin.site.register(Comment)
