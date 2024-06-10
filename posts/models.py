from django.db import models
from accounts.models import Account
from category.models import Category
from tags.models import Tag
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Post(models.Model):

    STATUS = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    title = models.CharField(max_length=250, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    content = RichTextField(null=False)
    author = models.ForeignKey(Account, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    status = models.CharField(choices=STATUS, default='draft')
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_img_portada = models.ImageField(upload_to='photos/posts', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.title
        
    def get_url(self):
        return reverse('post_detail', args=[self.category.slug, self.slug])

    def get_absolute_url(self):
        return reverse("post_detail", args={self.slug})
    
    def save(self, *args, **kwargs):
        # Si el post es nuevo y no tiene un autor asignado, asigna al usuario actual como autor
        if not self.id and not self.author_id:
            self.author = self.request.user
        super().save(*args, **kwargs)




