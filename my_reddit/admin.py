from django.contrib import admin
from .models import User, Sub, Post

admin.site.register(User)

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class SubAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
        ('Author', {'fields': ['creator']}),
    ]
    inlines = [PostInline]

admin.site.register(Sub, SubAdmin)
