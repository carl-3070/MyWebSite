from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post'),

    path('about.html', views.about, name='about'),

]