from django.shortcuts import render,redirect
from .models import Client,Session
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import ClientForm, SessionForm


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
def session(request,session_pk):
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

@login_required
def edit_client(request,client_pk):
    """edit an existing entry"""
    Client_i = Client.objects.get(pk=client_pk)
    check_owner(Client_i.user,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = ClientForm(instance=Client_i)
    else:
        #POST data submitted; process data
        form = ClientForm(instance=Client_i,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tools:client',client_pk=Client_i.pk)
    context = {'client':Client_i,'form':form}
    return render(request,'tools/client_session/edit_client.html',context)


@login_required
def edit_session(request,session_pk):
    """edit an existing Session"""
    Sess = Session.objects.get(pk=session_pk)
    check_owner(Sess.user,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = SessionForm(instance=Sess)
    else:
        #POST data submitted; process data
        form = SessionForm(instance=Sess,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',creation_id=Sess.pk)
    context = {'session':Sess,'form':form}
    return render(request,'tools/client_session/edit_session.html',context)
