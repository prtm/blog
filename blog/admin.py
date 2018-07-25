# core django
from django.contrib import admin

# project
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'publish',
                    'status')
    list_filter = ('status', 'publish', 'created', 'modified', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-publish', 'status', 'created', 'modified')
