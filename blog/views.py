from django.shortcuts import get_object_or_404, render
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request , pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def blog_test(request,pid):
    #posts = Post.objects.filter(status=1) -> or in html manage it
    #posts = Post.objects.all()
    #post = Post.objects.get(pk=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request,'test.html',context)
