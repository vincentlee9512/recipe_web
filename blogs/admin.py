from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

    list_display_links = ('id', 'title')

    list_filter = ('author', )

    search_fields = ('title', 'author')

    list_per_page = 25


admin.site.register(Blog, BlogAdmin)

