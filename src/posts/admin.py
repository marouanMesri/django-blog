from django.contrib import admin

from posts.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published',
                    'created_at', 'last_updated')
    list_editable = ('published',)
    list_filter = ('published', 'created_at', 'last_updated')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
