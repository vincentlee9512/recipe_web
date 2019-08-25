from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
from .form import NewBlogForm, CommentForm
from .models import Blog, Comment

def blogs(request):
    blogs = Blog.objects.order_by('-post_date')[:8]

    context = {
        'blogs': blogs
    }

    return render(request, 'blogs/blogs.html', context)


def single_blog(request, single_blog_id):

    target_blog = get_object_or_404(Blog, pk=single_blog_id)

    popular_blogs = Blog.objects.order_by('-post_date')[:3]

    comments = Comment.objects.filter(recipe_id=single_blog_id)

    comment_form = CommentForm()

    context = {
        'single_blog_id': single_blog_id,
        'blog': target_blog,
        'popular_blogs': popular_blogs,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'blogs/blog.html', context)


def new_blog(request):
    form = NewBlogForm()
    comment_form = CommentForm()

    context = {
        'form': form,
        'comment_form': comment_form,
    }

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
        return render(request, 'blogs/new_blog.html', context)


def comment(request):

    if request.method == "POST":
        form = CommentForm(request.POST)

        blog_id = request.POST["blog_id"]
        user = request.user

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = user
            new_comment.recipe = Blog.objects.filter(id=blog_id)[0]
            new_comment.save()

        return redirect('/blogs/' + blog_id)

    else:
        return redirect('index')
