from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password

def login(request) :

    if request.method == "POST":

        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)

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
        useremail = request.POST.get('useremail', None)
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword',None)
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != repassword:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username = useremail,
                                    first_name=firstname,
                                    last_name=lastname,
                                    password = password)
            auth.login(request, user)
            return render(request,"index.html")
    return render(request, 'register.html', res_data)


def forgotpw(request):
    if request.method == "POST":
        useremail = request.POST.get("useremail")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        try:
            user = User.objects.get(username = useremail, first_name = firstname, last_name = lastname)
        except User.DoesNotExist:
            context ={"error" : '이름 또는 이메일이 등록되지 않았습니다.'}
            return render(request,'forgotpw.html',context)
        else:
            request.user.username = useremail
            return redirect('/accountapp/changepw/?username=' + useremail)
    else:
        return render(request,"forgotpw.html")

def changepw(request):
    if request.method == "POST":
        newpassword=request.POST.get("newpassword")
        renewpassword=request.POST.get("renewpassword")
        email = request.GET.get('username')
        if newpassword != renewpassword:
            return render(request,'changepw.html',context={"error":"비밀번호가 일치하지 않습니다.",'useremail':email})
        else:
            user=User.objects.get(username=email)
            user.password=make_password(newpassword)
            user.save()
            auth.login(request, user)
            return render(request,"index.html")
    else:
        email=request.GET.get('username',"NotFound")
        if email == "NotFound":
            return render(request, 'forgotpw.html', {'error': "변경할 이메일을 입력해 주세요."})
        return render(request, 'changepw.html',{'useremail':request.GET['username']})

# Create your views here.
