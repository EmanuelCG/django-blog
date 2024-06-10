from django.contrib import admin
from django.http import HttpRequest
from .models import Category
from .models import Account
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'author_full_name']
    readonly_fields = ['author']
    
    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        # Si el objeto es nuevo y no tiene un autor establecido, establecer el autor como el usuario actual
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_staff or request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.author != request.user:
            return False
        return request.user.is_staff
        
    def has_delete_permissission(self, request, obj=None):
        if obj is not None and obj.author == request.user:
            return True
        return False

    def author_full_name(self, obj):
        return obj.author.full_name() if obj.author else '-'
    
    author_full_name.short_description = "Author"
    
admin.site.register(Category, CategoryAdmin)