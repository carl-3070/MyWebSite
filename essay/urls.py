from django.urls import path

from . import views

app_name = 'essay'
urlpatterns = [
    path('', views.essay, name='essay'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.post, name='essay'),

]