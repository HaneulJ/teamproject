from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request) :
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(useremail=useremail, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/echozapp/index/")
        else:
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else:
        return render (request, 'login.html')

def register(request):
    res_data = None
    if request.method =='POST':
        useremail = request.POST.get('useremail')
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword',None)
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != repassword:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(useremail = useremail,
                            username = username,
                            password = password)
            auth.login(request, user)
            redirect("/echozapp/index/")
    return render(request, 'register.html', res_data)


# Create your views here.
