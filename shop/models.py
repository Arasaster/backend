from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.CharField(max_length=100)  # Art size
    price = models.DecimalField(max_digits=200, decimal_places=2)
    medium = models.CharField(max_length=100)  # Art medium
    year = models.IntegerField(blank=True, null=True)  # Year of creation (optional)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)  # Product image
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Order(models.Model):
    """Model for customer orders"""
    ORDER_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    
    order_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return f"Order {self.order_number}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class OrderItem(models.Model):
    """Model for items in an order"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"