from django.shortcuts import get_object_or_404, render
from blog.models import Post

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request , pid):
    #post = get_object_or_404(Post, pk=pid, status=1)
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

# def blog_test(request,pid):
    #posts = Post.objects.filter(status=1) -> or in html manage it
    #posts = Post.objects.all()
    #post = Post.objects.get(pk=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request,'test.html',context)

def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)