from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import markdown
from .models import Essay
# Create your views here.
def essay(request):
    post_list = Essay.objects.all().order_by('-created_time')
    return render(request, 'essay/essay.html', context={'post_list': post_list})

def post(request, pk):
    post = get_object_or_404(Essay, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/post.html', context={'post': post})