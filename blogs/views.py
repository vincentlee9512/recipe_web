from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from .form import NewBlogForm
from .models import Blog

def blogs(request):
    blogs = Blog.objects.order_by('-post_date')[:8]

    context = {
        'blogs': blogs
    }

    return render(request, 'blogs/blogs.html', context)


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


def new_blog(request):
    form = NewBlogForm()

    if request.method == "POST":

        form_with_data = NewBlogForm(request.POST, request.FILES)

        if form_with_data.is_valid():
            new_single_blog = form_with_data.save(commit=False)
            new_single_blog.author = request.user
            new_single_blog.save()

            return render(request, 'accounts/dashboard.html')

        else:
            return render(request, 'blogs/new_blog.html')

    else:
        return render(request, 'blogs/new_blog.html', { 'form': form, })


