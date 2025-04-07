from django.db import models

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

    def __str__(self):
        return self.name

# transaction
class Transaction(models.Model):
    reference = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.reference}"