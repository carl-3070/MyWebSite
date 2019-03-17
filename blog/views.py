from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import markdown
from .models import Post

# Create your views here.



def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/post.html', context={'post': post})


def about(request):
    return render(request, 'blog/about.html', context={})