from django.shortcuts import render
from blogs.models import Blog


def index(request):
    blogs = Blog.objects.order_by('-post_date')[:8]

    for blog in blogs:
        print(blog.cover.url)

    context = {
        'blogs': blogs
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
