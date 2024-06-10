from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'author_full_name']
    readonly_fields = ['author']
    
    def has_view_permission(self, request, obj=None):
        return True
    
    def save_model(self, request, obj, form, change):
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

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.author == request.user:
            return True
        return False
    def author_full_name(self, obj):
        return obj.author.full_name() if obj.author else '.'
    author_full_name.short_description = "Author"

admin.site.register(Tag, TagAdmin)
