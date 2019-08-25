from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .form import NewBlogForm, CommentForm
from .models import Blog, Comment


def blogs(request):
    blogs = Blog.objects.order_by('-post_date')

    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': paged_blogs
    }

    return render(request, 'blogs/blogs.html', context)


def single_blog(request, single_blog_id):

    target_blog = get_object_or_404(Blog, pk=single_blog_id)

    popular_blogs = Blog.objects.order_by('-post_date')[:3]

    comments = Comment.objects.filter(recipe_id=single_blog_id).order_by('-post_date')

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

            return redirect('dashboard')

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


def search(request):
    queryset_list = Blog.objects.all().order_by('-post_date')


    # 用 keyword 过滤结果，在菜名和分类的字段中过滤
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        print(f"KEYWORD: {keyword}")
        # 如果 keyword 不为空
        if keyword:
            title_queryset_list = queryset_list.filter(title__icontains=keyword)
            category_queryset_list = queryset_list.filter(category__icontains=keyword)
            queryset_list = title_queryset_list.union(category_queryset_list).order_by('-post_date')

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_result = paginator.get_page(page)

    context = {
        'blogs': paged_result,
    }

    return render(request, 'blogs/blogs.html', context)


def categorize(request, cate_type):
    print(f'cate_type: {cate_type}')

    queryset_list = Blog.objects.all().order_by('-post_date').filter(category__icontains=cate_type)
    active_cate = cate_type

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_result = paginator.get_page(page)

    context = {
        'blogs': paged_result,
        'active_cate': active_cate
    }

    return render(request, 'blogs/blogs.html', context)
