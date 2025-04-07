from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)


from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['reference', 'email', 'product', 'amount', 'verified', 'created_at']
