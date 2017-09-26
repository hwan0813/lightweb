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