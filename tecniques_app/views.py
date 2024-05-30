from django.shortcuts import render,redirect
from .models import Blog_Topic,Blog,Author
from .forms import TopicForm,BlogForm

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse

#Global views
def index(request):
    topics = Blog_Topic.objects.order_by('text')
    context = {'topics':topics}
    return render(request,'blog_app/index.html',context)

def blog_list(request):
    blogs = Blog.objects.order_by('-date_made')
    content = {'blogs':blogs}
    return render(request,'blog_app/blog_list.html',content)

def blog_list_by_topic(request, topic_id):
    topic = Blog_Topic.objects.get(id=topic_id)
    blogs = topic.blog_set.order_by('-date_made')
    context = {'blogs':blogs,'topic':topic}
    return render(request,'blog_app/blog_list_by_topic.html',context)


def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    topic = blog.topic
    context = {'blog':blog,'topic':topic}
    return render(request,'blog_app/blog.html',context)


#CRUD section, where you can edit insde the site (not admin)


#Views
@login_required
def new_topic(request):
    if request.method !='POST':
        form = TopicForm()
    else:
        #saves the form and takes you back to index
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:index')
    #display a blank form
    context = {'form':form}
    return render(request,'blog_app/new_topic.html',context)


@login_required
def new_blog(request):
    user_id = request.user
    try:
        blog_author = Author.objects.get(user_info=user_id)
    except:
        new_author = Author(name=user_id.username, about="",user_info=request.user)
        new_author.save()
        blog_author = new_author


    if request.method !='POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        #here we save the changes, the is valid check all is ok, then we save with commit False
        #in this way we can add the topic_id, to the new blog and then save with commit. 
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = blog_author
            new_blog.save()
            return redirect('blog_app:blog_list')
    context = {'form':form}
    return render(request,'blog_app/new_blog.html',context)

@login_required
def edit_blog(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    topic = blog.topic
    author_key = blog.author
    try:
        author_id = Author.objects.get(name=author_key)
    except:
        html = "<html><body><h1>You are not the owner of this blog, and you have not made your frist post</h1></body></html>"
        return HttpResponse(html)

    author_user = author_id.user_info
 
    if author_user != request.user:
        html = "<html><body><h1>You are not the owner of this blog</h1></body></html>"
        return HttpResponse(html)


    #here we save changes again, this time we fill instance with the blog
    #when we finish editing (in the else) we give the instance and new data. we redirect to the blog, giving the id again
    if request.method != 'POST':
        #request pre-filled with current entry
        form = BlogForm(instance=blog)
    else:
        #sumitting data and saving it
        form = BlogForm(instance=blog,data=request.POST)
        if form.is_valid():
            edited_blog = form.save(commit=False)
            edited_blog.author = blog.author
            edited_blog.topic = topic
            edited_blog.save()
            return redirect('blog_app:blog',blog_id=blog.id)
    #blank form
    context = {'form':form,'topic':topic,'blog':blog}
    return render(request,'blog_app/edit_blog.html',context)


        
        
            

