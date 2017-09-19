from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import PostForm

def index(request):
    return render(request, 'post/index.html')

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