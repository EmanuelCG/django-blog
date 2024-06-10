from django.shortcuts import render
from posts.models import Post
from django.db.models import Q

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = Post.objects.order_by('-published_at').filter(Q(content__icontains=keyword) | Q(title__icontains=keyword) | Q(category__name__icontains=keyword))
    
    context = {
        'posts': posts
    }

    return render(request, 'layouts/search_result.html', context)