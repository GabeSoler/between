"""defines the urls for the blog_app"""

from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    #page for the topics of blogs
    path('',views.index,name='index'),
    #page for a list of blogs
    path('blog_list/',views.blog_list,name='blog_list'),
    path('blog_list_by_topic/<int:topic_id>/',views.blog_list_by_topic,name='blog_list_by_topic'),
    #page to see a full blog
    path('blog/<int:blog_id>/',views.blog, name='blog'),

    #editting funtionalities
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_blog/',views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_id>/',views.edit_blog,name='edit_blog'),
    ]

