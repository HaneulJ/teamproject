from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import auth

from .forms import CommentForm
from .models import Post, Comment
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone


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

def Boarddel(request):
    id = request.GET['id']
    view = Post.objects.get(id=id)
    view.delete()
    return redirect('Board')

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



def blogSingle(request) :
    template = loader.get_template('blog-single.html')
    return HttpResponse(template.render(None, request))




def add_comment_to_post(request, blog_id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Boardview
            comment.save()
            return redirect('Boardview', id)
        else:
            form = CommentForm()
    return render(request, 'Boardview.html')
