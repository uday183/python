from django.conf.urls import url
from django.views.generic import ListView,DetailView
from blog.models import Post
from . import views
urlpatterns = [
    
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="blog/blog.html")),


    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="blog/post.html")),
    url(r'^details/', views.details_of_user , name='details'),
    url(r'^d_create/', views.create_details , name='details_create'),
    url(r'^d_edit/', views.edit_details , name='edit'),
    url(r'^edits/', views.edit , name='edits'),
    url(r'^delete/', views.delete , name='delete'),
    
  ]