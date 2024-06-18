from django.shortcuts import render,redirect
from .models import Technique,Component, TechSaved
from .forms import TechniqueForm
from django.contrib.auth.decorators import login_required
from .forms import TechniqueForm

#Global views
def index(request):
    if request.user.is_authenticated:
        techniques = Technique.objects.filter(user=request.user).order_by('-date_made')
        context = {'techniques':techniques}
        return render(request,'techniques_app/index.html',context)
    return render(request,'techniques_app/index.html')

@login_required
def saved_techniques(request):
    try:
        tech_saved = TechSaved.objects.get(user=request.user).saved.all().order_by('name')
    except:
        tech_saved = ''
    context = {'tech_saved':tech_saved}
    return render(request,'techniques_app/saved_techniques.html',context)




def group_list_community(request): #Components list to organise the techniques
    subjective = Component.objects.filter(group='subj')
    extended = Component.objects.filter(group='ext')
    contextual = Component.objects.filter(group='contx')
    culture = Component.objects.filter(group='cltr')
    identity = Component.objects.filter(group='idty')
    context = {'subjective':subjective,'extended':extended,
               'contextual':contextual,'culture':culture,
               'identity':identity}
    return render(request,'techniques_app/group_list.html',context)



def techniques_short_community(request,comp_id): #List organised by component
    technique = Technique.objects.filter(share=True).filter(component=comp_id).order_by('-date_made')
    component = Component.objects.get(pk=comp_id)
    context = {'technique':technique, 'component':component}
    return render(request,'techniques_app/techniques_list_community.html',context)

def techniques_long_community(request): #Full list of techniques
    technique = Technique.objects.filter(share=True).order_by('-date_made')
    context = {'technique':technique}
    return render(request,'techniques_app/techniques_list_community.html',context)


def technique(request, tch_pk):
    technique = Technique.objects.get(id=tch_pk)
    try:    
        author_info = technique.user__comunity_profile
    except:
        author_info = ''
    context = {'technique':technique,'author_info':author_info}
    return render(request,'techniques_app/technique.html',context)


#CRUD section, where you can edit insde the site (not admin)


#Views

@login_required
def new_technique(request):
    user_id = request.user
    if request.method !='POST':
        form = TechniqueForm
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
def edit_technique(request,tch_pk):
    technique = Technique.objects.get(pk=tch_pk)
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
    return render(request,'techniques_app/edit-technique.html',context)


@login_required
def save_technique(request,tch_pk):
    user = request.user
    if request.method !='POST':
        return redirect('techniques_app:technique',tch_pk)
    else:
        tech_save,created = TechSaved.objects.get_or_create(user=user)
        if created:
            tech_save.saved = tch_pk
        else:
            tech_save.saved.add(tch_pk)
        tech_save.save()
    return redirect('techniques_app:saved_techniques')

        
@login_required
def delete_technique(request,tch_pk):
    user_id = request.user
    if request.method !='POST':
        context = {'tech_pk':tch_pk}
    else:
        tech_save = TechSaved.objects.get(user=user_id)
        tech_save.saved.remove(tch_pk)
        tech_save.save()
        return redirect('techniques_app:saved_techniques')
    return render(request,'techniques_app/delete_saved.html',context)


