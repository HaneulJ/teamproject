from pyexpat.errors import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import auth
from django.urls import reverse_lazy

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




def comment_writer(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Boardview, pk=post_pk)
        content= request.POST.get('content')

        conn_user = request.user
        conn_profile = Boardview.objects.get(user=conn_user)

        if not content:
            messages.info(request, '댓글을 입력하세요')
            return HttpResponseRedirect('Boardview')

    Comment.objects.create(post=post, comment_writer=conn_profile, comment_contents=content)
    return HttpResponseRedirect('Boardview')

from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def new(request):
    if request.method == 'POST':
        # Database에 저장
        # 1. 요청에 실려온 data 꺼내오기
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        form = PostForm(request.POST)

        # 2-1. data 유효성 검사
        if form.is_valid():
            # (ModelForm) 2-2. Database에 저장
            post = form.save()
            # # 2-2. 검증된 data 꺼내오기
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # # 2-3. Database에 저장
            # article = Article(title=title, content=content)
            # article.save()
            # 3. 저장된 data를 확인할 수 있는 곳으로 안내
            return redirect('Boardview', post.pk)

    else:  # GET
        # 작성 양식 보여주기
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'Boardview.html', context)


def Boardview_detail(request, pk):
    # Database에서 data 가져오기
    post = Post.objects.get(pk=pk)

    # 댓글 작성 양식 가져오기
    comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'Boardview', context)


def delete(request, pk):  # POST
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('Boardview')


def edit(request, pk):
    # 1. Database에서 data 가져오기
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        # data 수정!

        # (ModelForm) 2-1. form에 data 집어넣기 + instance와 연결
        form = PostForm(request.POST, instance=post)
        # # 2-1. form에 data 집어넣기(검증 목적)
        # form = ArticleForm(request.POST)
        # 2-2. form에서 data 유효성 검사
        if form.is_valid():
            # (ModelForm) 2-3. Database에 저장
            post = form.save()
            # # 2-3. 검증된 data를 반영하기(저장)
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            # 3. 저장된 내용을 확인할 수 있는 페이지로 안내
            return redirect('Boardview', post.pk)
    else:
        # 수정 양식 보여주기!
        # (ModelForm) 2. Form에 data 채워 넣기
        form = PostForm(instance=post)
        # # 2. Form에 data 채워 넣기
        # form = ArticleForm(initial=article.__dict__)
    context = {
        'form': form,
    }
    return render(request, 'comments_edit.html', context)


def comments_new(request, post_pk):  # POST
    # 1. 요청이 POST 인지 점검
    if request.method == 'POST':
        # 2. form에 data를 집어넣기 (목적 == 유효성 검사)
        form = CommentForm(request.POST)
        # request.POST #=>
        # 3. form에서 유효성 검사를 시행
        if form.is_valid():
            # 4. 통과하면 database에 저장
            comment = form.save(commit=False)
            # 4-1. article 정보 주입
            comment.post_id = post_pk
            comment.save()
    # 5. 생성된 댓글을 확인할 수 있는 곳으로 안내
    return redirect('Boardview', post_pk)


def comments_delete(request, post_pk, pk):  # POST
    # 0. 요청이 POST인지 점검
    if request.method == 'POST':
        # 1. pk를 가지고 삭제하려는 data를 꺼내오기
        comment = Comment.objects.get(pk=pk)
        # 2. 삭제
        comment.delete()
    # 3. 삭제되었는지 확인 가능한 곳으로 안내

    return redirect('Boardview', post_pk)


def comments_edit(request, post_pk, pk):  # GET , POST
    # Database에서 수정하려 하는 data 가져오기
    comment = Comment.objects.get(pk=pk)
    # 0. 요청의 종류가 POST인지 GET인지 점검
    if request.method == 'POST':
        # 실제로 수정 !
        # 1. form에 '넘어온 data' & '수정하려는 data' 집어넣기
        form = CommentForm(request.POST, instance=comment)
        # 2. 유효성 검사
        if form.is_valid():
            # 3. 검사를 통과했다면, save
            comment = form.save()
            # 4. 변경된 결과 확인하는 곳으로 안내
            return redirect('Boardview', post_pk)
    else:
        # 수정 양식 보여주기!
        # 1. form class 초기화 (생성)
        form = CommentForm(instance=comment)

    context = {
        'form': form,
    }
    return render(request, 'comments_edit.html', context)