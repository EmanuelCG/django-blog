from django.shortcuts import render
from .models import Category
# Create your views here.

def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'layouts/categories.html', {'categories': categories})