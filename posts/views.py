from django.shortcuts import render, get_object_or_404
from posts.models import Post
from posts.models import Category
from utils.breadcrumbs import get_breadcrumbs
def post_detail(request, category_slug, post_slug):
    posts = Post.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    single_post = get_object_or_404(Post, category__slug=category_slug, slug=post_slug)
    breadcrumbs = get_breadcrumbs(
    (category.name, category.get_absolute_url()),
    (single_post.title, single_post.get_url())
    )
    context = {'single_post': single_post, 'posts': posts, 'breadcrumbs': breadcrumbs}

    return render(request, 'posts/single_post.html', context)