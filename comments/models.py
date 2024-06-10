from django.db import models
from accounts.models import Account
from posts.models import Post
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True )
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    content = models.TextField(null=True)
    creted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
