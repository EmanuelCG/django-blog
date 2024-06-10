from django.db import models
from accounts.models import Account
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name