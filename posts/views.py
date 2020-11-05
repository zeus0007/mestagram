from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def index(request):
    posts = Post.objects.all()
    context= {'posts':posts}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {'post':post}
    return render(request, 'posts/detail.html', context)

def create(request):
    return render(request, 'posts/create.html')

def new(request):
    new_post = Post(
        author = request.POST['author'], 
        content = request.POST['content'], 
        created_at=timezone.now()
        )
    new_post.save()

    return redirect('posts:detail', post_id=new_post.id)


    
