from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    context = {}
    blog_list = Post.objects.all().order_by('-created_time')
    context["last_blog"] = blog_list[1]
    return render(request, 'home/home.html', context)
