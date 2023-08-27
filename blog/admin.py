from django.contrib import admin

# Register your models here.
from .models import Post, Comment


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['title', 'slug', 'author', 'published', 'Status']
    list_filter= ['Status', 'created', 'published', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields =['author']
    date_hierarchy = 'published'
    ordering = ['Status', 'published']
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
