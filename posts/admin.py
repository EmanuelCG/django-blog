from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Post 
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author_full_name', 'category']
    readonly_fields = ['author']

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.is_superadmin:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(author=request.user)

    def save_model(self, request, obj, form, change):
        # Asignar el usuario actual como autor del post solo si es nuevo y no tiene un autor asignado
        if not obj.id and not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # Permitir agregar post si el usuario es staff o superusuario
        return request.user.is_staff or request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_superadmin:
            return True
        if obj is not None and obj.author != request.user:
            return False
        return request.user.is_staff
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_superadmin:
            return True
        if obj is not None and obj.author != request.user:
            return False
        return request.user.is_staff
    
    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_superadmin:
            return True
        if obj is not None and obj.author != request.user:
            return False
        return request.user.is_staff
    
    def author_full_name(self, obj):
        return obj.author.full_name() if obj.author else '-'
    
    author_full_name.short_description = 'Author'

admin.site.register(Post, PostAdmin)