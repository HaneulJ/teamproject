from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth

def index(request) :
    return render(request,'index.html')
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render(None, request))

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("index")

def mypage(request):
    context= None
    if request.user.is_authenticated:
        context ={'loginuser' : request.user.last_name+request.user.first_name}
    return render(request, 'mypage.html',context)

def What(request):
    return render(request, 'What.html')

def How(request):
    return render(request, 'How.html')

def Where(request):
    return render(request, 'Where.html')

def Board(request):
    return render(request, 'Board.html')

def Events(request):
    return render(request, 'Events.html')

def checklist0(request):
    return render(request, 'checklist0.html')

def checklist1(request):
    return render(request, 'checklist1.html')

def checklist2(request):
    return render(request, 'checklist2.html')

def checklist3(request):
    return render(request, 'checklist3.html')

def news1(request):
    return render(request, 'news1.html')

def news2(request):
    return render(request, 'news2.html')

def news3(request):
    return render(request, 'news3.html')

def news4(request):
    return render(request, 'news4.html')

def news5(request):
    return render(request, 'news5.html')

def news6(request):
    return render(request, 'news6.html')

def news7(request):
    return render(request, 'news7.html')

def news8(request):
    return render(request, 'news8.html')

def shop1(request):
    return render(request, 'shop1.html')

def shop2(request):
    return render(request, 'shop2.html')

def shop3(request):
    return render(request, 'shop3.html')

def tip1(request):
    return render(request, 'tip1.html')

def tip2(request):
    return render(request, 'tip2.html')

def tip3(request):
    return render(request, 'tip3.html')

def zero1(request):
    return render(request, 'zero1.html')

def zero2(request):
    return render(request, 'zero2.html')

def video1(request):
    return render(request, 'video1.html')

def video2(request):
    return render(request, 'video2.html')

def video3(request):
    return render(request, 'video3.html')

def video4(request):
    return render(request, 'video4.html')

def video5(request):
    return render(request, 'video5.html')

def event12(request):
    return render(request, 'event12.html')

def event1(request):
    return render(request, 'event1.html')


def event2(request):
    return render(request, 'event2.html')



def blogSingle(request) :
    template = loader.get_template('blog-single.html')
    return HttpResponse(template.render(None, request))

# Create your views here.
