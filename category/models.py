from django.db import models
from django.urls import reverse
from accounts.models import Account
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', null=True, blank=True)
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("categories")
    