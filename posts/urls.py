from django.urls import path
from . import views
urlpatterns = [
    path('category/<slug:category_slug>/<slug:post_slug>', views.post_detail, name="post_detail")
]
