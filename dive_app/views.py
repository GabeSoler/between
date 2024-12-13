from django.shortcuts import render,redirect
from .models import Creation,Shadow,AssembleModel
from .forms import CreationForm,ShadowForm,AssembleForm
from django.contrib.auth.decorators import login_required,permission_required
from django.http import Http404
from django.urls import reverse


#Functions
def check_owner(topic_owner,request_user):
    if topic_owner != request_user:
        raise Http404
    
#Views

def index(request):
    """show all Dive sections"""
    if not request.user.is_authenticated:
        return render(request,'dive_app/index.html')
    creations = Creation.objects.filter(owner=request.user).order_by('-date_added')[:5]
    shadows = Shadow.objects.filter(owner=request.user).order_by('-date_added')[:5]
    assembles = AssembleModel.objects.filter(owner=request.user).order_by('-date_added')[:5]
    context = {'creations':creations,'shadows':shadows,"assembles":assembles}
    return render(request,'dive_app/index.html',context)


#Creation's CRUD
@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def creation_item(request,creation_pk):
    """show an item of creation"""
    CreationItem = Creation.objects.get(pk=creation_pk)
    check_owner(CreationItem.owner,request.user)
    context = {'creations':CreationItem}
    return render(request,'dive_app/creating/creation_item.html',context)


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def creation_by_date(request):
    """show all answers by date"""
    creations_by_date = Creation.objects.filter(owner=request.user).order_by('-date_added')
    context = {'creations':creations_by_date}
    return render(request,'dive_app/creating/creation_by_date.html',context)

@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def creation_by_title(request):
    """show all creations by title"""
    by_title = Creation.objects.filter(owner=request.user).order_by('title','date_added')
    context = {'creations':by_title}
    return render(request,'dive_app/creating/creation_by_title.html',context)

@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
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
            return redirect('dive_app:index')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'dive_app/creating/create_reflection.html',context)


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def edit_creation(request,creation_pk):
    """edit an existing entry"""
    creation = Creation.objects.get(pk=creation_pk)
    check_owner(creation.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = CreationForm(instance=creation)
    else:
        #POST data submitted; process data
        form = CreationForm(instance=creation,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dive_app:creation_item',creation_pk)
    context = {'creations':creation,'form':form}
    return render(request,'dive_app/creating/edit_creation.html',context)


#* Shadow's CRUD


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def shadow_item(request,shadow_pk):
    """show an item of shadow"""
    ShadowItem = Shadow.objects.get(pk=shadow_pk)
    check_owner(ShadowItem.owner,request.user)
    context = {'shadows':ShadowItem}
    return render(request,'dive_app/shadow/shadow_item.html',context)


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def shadow_by_date(request):
    """show all answers by date"""
    answers_by_date = Shadow.objects.filter(owner=request.user).order_by('-date_added')
    context = {'answers':answers_by_date}
    return render(request,'dive_app/shadow/shadow_by_date.html',context)

@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def shadow_by_title(request):
    """show all answers by question"""
    answers_by_question = Shadow.objects.filter(owner=request.user).order_by('title','-date_added')
    context = {'answers':answers_by_question}
    return render(request,'dive_app/shadow/shadow_by_title.html',context)

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
            return redirect('dive_app:index')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'dive_app/shadow/new_shadow.html',context)


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def edit_shadow(request,shadow_pk):
    """edit an existing entry"""
    shadow = Shadow.objects.get(pk=shadow_pk)
    check_owner(shadow.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = ShadowForm(instance=shadow)
    else:
        #POST data submitted; process data
        form = ShadowForm(instance=shadow,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dive_app:shadow_item',shadow_pk)
    context = {'shadow':shadow,'form':form}
    return render(request,'dive_app/shadow/edit_shadow.html',context)


#* Assemble's CRUD


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def assemble_item(request,assemble_pk):
    """show an item of assemble"""
    assembleItem = AssembleModel.objects.get(pk=assemble_pk)
    check_owner(assembleItem.owner,request.user)
    context = {'assemble':assembleItem}
    return render(request,'dive_app/assemble/assemble_item.html',context)


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def assemble_by_date(request):
    """show all answers by date"""
    answers_by_date = AssembleModel.objects.filter(owner=request.user).order_by('-date_added')
    context = {'answers':answers_by_date}
    return render(request,'dive_app/assemble/assemble_by_date.html',context)

@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def assemble_by_title(request):
    """show all answers by question"""
    answers_by_question = AssembleModel.objects.filter(owner=request.user).order_by('title','-date_added')
    context = {'answers':answers_by_question}
    return render(request,'dive_app/assemble/assemble_by_title.html',context)

def new_assemble(request):
    """add new question"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = AssembleForm()
    else:
        #POST data submitted; process data
        form = AssembleForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('dive_app:index')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'dive_app/assemble/new_assemble.html',context)


@login_required
@permission_required('accounts.can_dive',login_url="/accounts/edit_status/")
def edit_assemble(request,assemble_pk):
    """edit an existing entry"""
    assemble = AssembleModel.objects.get(pk=assemble_pk)
    check_owner(assemble.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = AssembleForm(instance=assemble)
    else:
        #POST data submitted; process data
        form = AssembleForm(instance=assemble,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dive_app:assemble_item',assemble_pk)
    context = {'assemble':assemble,'form':form}
    return render(request,'dive_app/assemble/edit_assemble.html',context)
