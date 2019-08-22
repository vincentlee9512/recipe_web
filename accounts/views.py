from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def register(request):
    if request.method == 'POST':
        print("Get the POST")

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        print(f'username: {username}, email: {email}, password: {password}, password2: {password2}')

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
                    user = User.objects.create_user(username=username, email=email, password=password)

                    user.save()
                    messages.success(request, '你已经成功注册账号，请登陆')
                    return redirect('login')
        else:
            messages.error(request, '两次输入的密码不匹配')
            return redirect('register')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
