from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    def __str__(self):
        return f"{self.category_name}"