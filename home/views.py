from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    context = {}
    blog_list = Post.objects.all().order_by('-created_time')
    if blog_list != []:
        context["last_blog"] = blog_list[0:2]
    return render(request, 'home/home.html', context)
