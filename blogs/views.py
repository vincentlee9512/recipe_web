from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-post_date')[:8]

    context = {
        'blogs': blogs
    }

    return render(request, 'blogs/blogs.html', context)


def new_blog(request):
    return render(request, 'blogs/new_blog.html')


def single_blog(request, single_blog_id):

    target_blog = Blog.objects.filter(id=single_blog_id)[0]

    popular_blogs = Blog.objects.order_by('-post_date')[:3]

    # author = User.objects.filter(id=target_blog.author)[0]

    context = {
        'single_blog_id': single_blog_id,
        'blog': target_blog,
        # 'author': author,
        'popular_blogs': popular_blogs,
    }
    return render(request, 'blogs/blog.html', context)

