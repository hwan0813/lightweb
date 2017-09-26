from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm
from .models import Post, Comment
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View,TemplateView , ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post

#post_delete = DeleteView.as_view(model=Post, success_url = reverse_lazy('post:post_list'))
# 그냥 reverse를 쓰면 코드가 처음 올라가자마자 reverse가 수행되므로 내부로직상(?) 에러가발생
# 딱 reverse가 필요할때 그제서야 호출하는 reverse_lazy를 통해 문자열을 만들어주는것이 좋다. 
#post_new = CreateView.as_view(model=Post)

#post_edit = UpdateView.as_view(model=Post, fields='__all__')

#post_detail = DetailView.as_view(model=Post)

def board(request):

    qs = Post.objects.all().prefetch_related('tag_set', 'comment_set')
    #이렇게 prefetch_related 해주면 단체로 가져와서 장고단에서 조합해줌. ->sql문의 수가 급진적감소. 효율적.

    q = request.GET.get('q','') # q있으면 ㄴ가져오고 없으면 빈문자가져오고
    if q: # q가 있다면...?
        qs = qs.filter(title__icontains = q)
    #이게 가능한 이유가 그냥 request라는 인자때문에 그냥 무한히 왕복 주고받고가능한건가. 

    #messages.error(request,'에러메세지 테스트')

    name = ' 이것도 넘겨보자. '
    return render(request, 'post/board.html',
     {'name':name, 'post_list' : qs, 'q':q} 
    ) # 인자 넘기나봄. 




def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request,'새 포스팅을 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', { 
            'form':form,   
        })

def post_detail(request, id):
    #try: # 포스트가 삭제되었을경우, 서버에러(500)으로 처리되는것이아니라 404로 처리도되도록 예외처리해줌. 
    #    post = Post.objects.get(id=id)
    #except Post.DoesNotExist:
    #    raise Http404
    # 위의 4줄이랑 같은코드. 이걸쓰자. shortcut으로부터 import는 하고 
    post = get_object_or_404(Post, id = id)
    #지정레코드가 없는것은 서버오류가 아니므로 모든 인스턴스처리는 get_ob~404로 한다. 

    return render(request, 'post/post_detail.html', {
    'post':post,
    })
def mainpage(request):
    return render(request, 'post/main.html')

def photo(request):
    return render(request, 'post/photo.html')
def about(request):
    return render(request, 'post/about.html')
def member(request):
    return render(request, 'post/member.html')
def introduce(request):
    return render(request, 'post/introduce.html')

