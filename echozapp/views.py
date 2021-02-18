from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from .models import Post
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from echozapp.models import Latlng, Seoul, GIG, CD, JG, GDBU, Jeju


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
        author = request.user.id
        user_post=Post.objects.filter(author_id=author)
        user_post = user_post.order_by('-writedate')
        myboardcount = user_post.count()
        page = request.GET.get('page', 1)
        paginator = Paginator(user_post , 3)
        user_postpage = paginator.get_page(page)
        context ={'loginid': request.user.username,'loginuser' : request.user.last_name+request.user.first_name, 'user_post' : user_postpage, 'myboardcount' : myboardcount, 'user_postpage' : user_postpage}
    return render(request, 'mypage.html',context)


#글작성
def Boardwrite(request):
    title = request.POST['title']
    content = request.POST['content']
    author = request.user.id
    wdata = Post(author_id = author, title=title, content=content)
    wdata.save()
    return redirect("Board")

def Board(request):

    page = request.GET.get('page', 1)
    vlist = Post.objects.all()
    vlist = vlist.order_by('-writedate')
    paginator = Paginator(vlist, 3)
    vlistpage = paginator.get_page(page)
    boardcount = Post.objects.count()
    context = {"vlist": vlistpage,"boardcount":boardcount}

    return render(request, 'Board.html',context)

def Boardview(request):
    context={}
    id = request.GET['Boardview']
    Boardview = Post.objects.get(id=id)
    Boardview.count = Boardview.count + 1
    Boardview.save()
    context['Boardview'] = Boardview
    return render(request, 'Boardview.html',context)

def Boardview1(request):
    context={}
    id = request.GET['Boardview1']
    Boardview1 = Post.objects.get(id=id)
    Boardview1.save()
    context['Boardview1'] = Boardview1
    return render(request, 'Boardview1.html',context)

def Boarddel(request):
    id = request.GET['id']
    view = Post.objects.get(id=id)
    view.delete()
    return redirect('mypage')

def Boardupdate(request):
    if request.method == "POST":
        id = request.GET.get('id')
        update = Post.objects.get(id=id)
        update.title = request.POST['title']
        update.content = request.POST['content']
        update.writedate = timezone.datetime.now()
        update.save()
        return redirect('Board')
    else :
        id = request.GET.get("id")
        update = Post.objects.get(id=id)
        jsonContent={"title" : update.title, "content": update.content }
        return JsonResponse( jsonContent, json_dumps_params={'ensure_ascii':False})

def search1(request, name) :
    page = request.GET.get('page', 1)
    vlist = Post.objects.filter(title__contains = name)
    paginator = Paginator(vlist, 3)
    vlistpage = paginator.get_page(page)
    context = {"vlist": vlistpage}
    return render(request, 'Board.html', context)

def search2(request, content):
    page = request.GET.get('page', 1)
    vlist = Post.objects.filter(content__contains=content)
    paginator = Paginator(vlist, 3)
    vlistpage = paginator.get_page(page)
    context = {"vlist": vlistpage}
    return render(request, 'Board.html', context)


def What(request):
    return render(request, 'What.html')

def What2(request):
    return render(request, 'What2.html')

def How(request):
    return render(request, 'How.html')

def Where(request):
    return render(request, 'Where.html')

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

def event121(request):
    return render(request, 'event121.html')

def event1231(request):
    return render(request, 'event1231.html')

def event11(request):
    return render(request, 'event11.html')

def event131(request):
    return render(request, 'event131.html')


def event21(request):
    return render(request, 'event21.html')

def book1(request):
    return render(request, 'book1.html')

def book2(request):
    return render(request, 'book2.html')

def book3(request):
    return render(request, 'book3.html')

def book4(request):
    return render(request, 'book4.html')



def blogSingle(request) :
    template = loader.get_template('blog-single.html')
    return HttpResponse(template.render(None, request))

def map(request):
    latlng = Latlng.objects.all()
    return render(request, 'map.html', {'latlng': latlng})

def map_my(request):
    latlng = Latlng.objects.all()
    return render(request, 'map_my.html', {'latlng': latlng})

def shop1(request):
    seoul = Seoul.objects.all()
    return render(request, 'shop1.html', {'seoul': seoul})

def shop2(request):
    gig = GIG.objects.all()
    return render(request, 'shop2.html', {'gig': gig})

def shop3(request):
    cd = CD.objects.all()
    return render(request, 'shop3.html', {'cd': cd})

def shop4(request):
    jg = JG.objects.all()
    return render(request, 'shop4.html', {'jg': jg})

def shop5(request):
    gdbu = GDBU.objects.all()
    return render(request, 'shop5.html', {'gdbu': gdbu})

def shop6(request):
    jeju = Jeju.objects.all()
    return render(request, 'shop6.html', {'jeju': jeju})
