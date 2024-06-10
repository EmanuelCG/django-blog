
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name="search"),
    path('post/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/', include('category.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
