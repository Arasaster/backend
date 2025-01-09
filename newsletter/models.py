from django.db import models

# Create your models here.
class NewsletterSubscriber(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)  # Subscriber's email
    name = models.CharField(max_length=100)  # Name of the subscriber
    date_subscribed = models.DateTimeField(auto_now_add=True)  # Subscription date

    def __str__(self):
        return f"{self.name} - {self.email}"
