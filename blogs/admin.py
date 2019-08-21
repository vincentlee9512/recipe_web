from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'post_date')

    list_display_links = ('id', 'title')

    list_filter = ('author', )

    list_editable = ('is_published', )

    search_fields = ('title', 'author', 'description', 'ingredient', 'category_1', 'category_2', 'category_3')

    list_per_page = 25


admin.site.register(Blog, BlogAdmin)

