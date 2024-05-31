from django.shortcuts import render,redirect
from .models import Technique,Component
from django.contrib.auth.decorators import login_required
from .forms import TechniqueForm

#Global views
def index(request):
    techniques = Technique.objects.filter(user=request.user)
    context = {'techniques':techniques}
    return render(request,'techniques_app/index.html',context)

def group_list_community(request):
    subjective = Component.objects.filter(group='subj')
    extended = Component.objects.filter(group='ext')
    contextual = Component.objects.filter(group='contx')
    culture = Component.objects.filter(group='cltr')
    identity = Component.objects.filter(group='idty')
    content = {'subjective':subjective,'extended':extended,
               'contextual':contextual,'culture':culture,
               'identity':identity}
    return render(request,'techniques_app/group_list.html',content)



def techniques_short_community(request,comp_id):
    technique = Technique.objects.filter(component=comp_id)
    context = {'technique':technique}
    return render(request,'techniques_app/techniques_list_community.html',context)

def techniques_long_community(request):
    technique = Technique.objects.all()
    context = {'technique':technique}
    return render(request,'techniques_app/techniques_list_community.html',context)


def technique(request, tch_pk):
    technique = Technique.objects.get(id=tch_pk)
    author_info = technique.user__comunity_profile
    context = {'technique':technique,'author_info':author_info}
    return render(request,'techniques_app/technique.html',context)


#CRUD section, where you can edit insde the site (not admin)


#Views

@login_required
def new_technique(request):
    user_id = request.user
    if request.method !='POST':
        form = ()
    else:
        form = TechniqueForm(data=request.POST)
        #here we save the changes, the is valid check all is ok, then we save with commit False
        #in this way we can add the topic_id, to the new blog and then save with commit. 
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = user_id
            new_blog.save()
            return redirect('techniques_app:index')
    context = {'form':form}
    return render(request,'techniques_app/new_technique.html',context)

@login_required
def edit_blog(request,tch_pk):
    technique = Technique.objects.get(id=tch_pk)
    if request.method != 'POST':
        #request pre-filled with current entry
        form = TechniqueForm(instance=technique)
    else:
        #sumitting data and saving it
        form = TechniqueForm(instance=technique,data=request.POST)
        if form.is_valid():
            edited_tch = form.save(commit=False)
            edited_tch.user = request.user
            edited_tch.save()
            return redirect('techniques_app:technique',tch_pk=technique.pk)
    #blank form
    context = {'form':form,'technique':technique}
    return render(request,'techniques_app/edit-tecnique.html',context)


        
        
            

