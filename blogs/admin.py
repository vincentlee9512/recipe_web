from django.contrib import admin

from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_date', 'category')

    list_display_links = ('id', 'title')

    list_filter = ('author', )

    search_fields = ('title', 'author')

    list_per_page = 25


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe', 'post_date')

    list_display_links = ('id', 'user')

    list_filter = ('user', 'recipe')

    search_fields = ('user', 'recipe')

    list_per_page = 25


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
