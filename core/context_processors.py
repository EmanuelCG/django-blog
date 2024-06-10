from datetime import datetime
from category.models import Category
from tags.models import Tag

def current_datetime(request):
    return {'current_datetime': datetime.now()}

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_tags(request):
    tags = Tag.objects.all()
    return {'tags': tags}
