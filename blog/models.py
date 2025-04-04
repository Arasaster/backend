from django.db import models

from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.core.exceptions import ValidationError

def validate_image_size(image):
    filesize = image.size
    # 1MB = 1,048,576 bytes
    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")

# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='blog/images/', 
        blank=True, 
        null=True,
        validators=[validate_image_size, FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])]
    )
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)  # Optional author name
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)  # Name of the commenter
    email = models.EmailField()
    content = models.TextField()  # Comment content
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog_post}"

    # Custom method to display the name in bold (can be used in templates)
    def bold_name(self):
        return f"<b>{self.name}</b>"
