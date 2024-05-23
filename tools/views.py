from django.shortcuts import render,redirect
from models import Client,Session
from django.contrib.auth.decorators import login_required
from django.http import Http404
from forms import ClientForm,SessionForm


#Functions
def check_owner(topic_owner,request_user):
    if topic_owner != request_user:
        raise Http404
    
# Create your views here.

def index(request):
    """show all tools"""
    return render(request,'tools/index.html')


#Session-Client
@login_required
def session_home(request):
    """show clients and sessions"""
    clients = Client.objects.filter(user=request.user).order_by('client_code')
    sessions = Session.objects.filter(user=request.user).order_by('created_at')[:10]
    context = {'clients':clients,'sessions':sessions}
    return render(request,'tools/client_session/home.html',context)


@login_required
def client(request,client_pk):
    """show one client"""
    client = Client.objects.get(pk=client_pk)
    check_owner(client.user,request.user)
    context = {'client':client}
    return render(request,'tools/client_session/client.html',context)

@login_required
def client(request,session_pk):
    """show one session"""
    session = Session.objects.get(pk=session_pk)
    check_owner(session.user,request.user)
    context = {'client':client}
    return render(request,'tools/client_session/session.html',context)



@login_required
def clients(request):
    """show all clients"""
    clients = Client.objects.filter(user=request.user).order_by('client_code')
    context = {'clients':clients}
    return render(request,'tools/client_session/client_list.html',context)

@login_required
def sessions(request):
    """show all sessions"""
    sessions = Session.objects.filter(user=request.user).order_by('created_at')
    context = {'sessions':sessions}
    return render(request,'tools/client_session/sessions_list.html',context)

@login_required
def add_client(request):
    """add new client"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = ClientForm()
    else:
        #POST data submitted; process data
        form = ClientForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('tools:home')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'tools/client_session/add_client.html',context)

@login_required
def add_session(request):
    """add new session"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = SessionForm()
    else:
        #POST data submitted; process data
        form = SessionForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('tools:home')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'tools/client_session/add_session.html',context)
