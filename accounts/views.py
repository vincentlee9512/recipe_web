from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Django 内置的检测用户是否存在，用户名和密码是否匹配的函数
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # user 存在，用户名都匹配
            auth.login(request, user)
            messages.success(request, "登入成功")
            return redirect('dashboard')
        else:
            # 登入失败
            messages.error(request, "登入失败, 请检测用户名和密码")
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index')
    else:
        return redirect('dashboard')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # 检测注册输入的信息
        # 检测两个密码是否相同
        if password == password2:
            # 检测这个用户名是否被占用
            if User.objects.filter(username=username).exists():
                messages.error(request, '此用户名已被注册')
                redirect('register')
            else:
                # 检测这个 email 是否已被注册
                if User.objects.filter(email=email).exists():
                    messages.error(request, '此 email 已被使用')
                    redirect('register')
                else:
                    # user = User.objects.create_user(username=username, email=email, password=password)

                    # user.save()
                    messages.success(request, '你已经成功注册账号，请登陆')
                    return redirect('login')
        else:
            messages.error(request, '两次输入的密码不匹配')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):

    # 从 User 表获得 user 信息
    # 从 Blogs 表获得 user 发布的 blogs
    # 从 收藏 表获得收藏了的 blogs 的信息

    return render(request, 'accounts/dashboard.html')
