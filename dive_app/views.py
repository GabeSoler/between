from django.shortcuts import render,redirect
from .models import Creation,Shadow
from .forms import CreationForm,ShadowForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


#Functions
def check_owner(topic_owner,request_user):
    if topic_owner != request_user:
        raise Http404
    
#Views

def index(request):
    """show all topics"""
    if not request.user.is_authenticated:
        return render(request,'learning_logs/index.html')
    creations = Creation.objects.filter(owner=request.user).order_by('date_added')[:3]
    shadows = Shadow.objects.filter(owner=request.user).order_by('date_added')[:3]
    context = {'creations':creations,'shadows':shadows}
    return render(request,'learning_logs/index.html',context)


#Creation's CRUD
@login_required
def creation_item(request,creation_pk):
    """show an item of creation"""
    CreationItem = Creation.objects.get(pk=creation_pk)
    check_owner(CreationItem.owner,request.user)
    context = {'creations':CreationItem}
    return render(request,'learning_logs/creating/creation_item.html',context)


@login_required
def creation_by_date(request):
    """show all answers by date"""
    creations_by_date = Creation.objects.filter(owner=request.user).order_by('-date_added')
    context = {'creations':creations_by_date}
    return render(request,'learning_logs/creating/creation_by_date.html',context)

@login_required
def creation_by_title(request):
    """show all creations by title"""
    by_title = Creation.objects.filter(owner=request.user).order_by('title','date_added')
    context = {'creations':by_title}
    return render(request,'learning_logs/creating/creation_by_title.html',context)

def new_creation(request):
    """add new Creation"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = CreationForm()
    else:
        #POST data submitted; process data
        form = CreationForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('learning_logs:index')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'learning_logs/creating/create_reflection.html',context)


@login_required
def edit_creation(request,creation_pk):
    """edit an existing entry"""
    Creations = Creation.objects.get(pk=creation_pk)
    check_owner(Creations.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = CreationForm(instance=Creations)
    else:
        #POST data submitted; process data
        form = CreationForm(instance=Creations,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',creation_id=Creations.id)
    context = {'creations':Creations,'form':form}
    return render(request,'learning_logs/creating/edit_creation.html',context)


#Shadow's CRUD


@login_required
def shadow_item(request,shadow_pk):
    """show an item of shadow"""
    ShadowItem = Shadow.objects.get(pk=shadow_pk)
    check_owner(ShadowItem.owner,request.user)
    context = {'shadows':ShadowItem}
    return render(request,'learning_logs/shadow/shadow_item.html',context)


@login_required
def shadow_by_date(request):
    """show all answers by date"""
    answers_by_date = Shadow.objects.filter(owner=request.user).order_by('-date_added')
    context = {'answers':answers_by_date}
    return render(request,'learning_logs/shadow/shadow_by_date.html',context)

@login_required
def shadow_by_title(request):
    """show all answers by question"""
    answers_by_question = Shadow.objects.filter(owner=request.user).order_by('question','date_added')
    context = {'answers':answers_by_question}
    return render(request,'learning_logs/shadow/shadow_by_question.html',context)

def new_shadow(request):
    """add new question"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = ShadowForm()
    else:
        #POST data submitted; process data
        form = ShadowForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('learning_logs:index')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'learning_logs/shadow/new_shadow.html',context)


@login_required
def edit_shadow(request,shadow_pk):
    """edit an existing entry"""
    Shadows = Shadow.objects.get(pk=shadow_pk)
    check_owner(Shadows.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = ShadowForm(instance=Shadows)
    else:
        #POST data submitted; process data
        form = ShadowForm(instance=Shadow,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:shadow_by_date',shadow_id=Shadows.id)
    context = {'shadow':Shadows,'form':form}
    return render(request,'learning_logs/shadow/edit_shadow.html',context)
