from django.shortcuts import render,redirect
from .models import PersonalStyle, Components,BigTraditions,PersonalStyleGroup
from django.views.generic import TemplateView
from .forms import StyleForm,ComponentsForm,BigTradForm,StyleFormClient
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .content import Content
from django.conf import settings
# Create your views here.

#A useful formating for bootstrap progress bars
format = ('bg-primary text-success',
        'bg-warning text-primary',
        'bg-info text-danger',
        'bg-danger text-dark',
        'bg-success text-danger',
        'bg-secondary text-primary',
        'bg-light text-dark',
        'bg-dark text-light',
        )
#Start classes with caps
class index_View(TemplateView):
    template_name = 'between_app/index.html'

        
def test_home(request):
    """show all tests"""
    if request.user.is_authenticated:
        try: 
            style_detail = PersonalStyle.objects.filter(user=request.user).latest('updated_at')
            results = style_detail.calProfile
            cont_position = PersonalStyleGroup.objects.get(group=results['main_position'])
            cont_path = PersonalStyleGroup.objects.get(group=results['main_path'])
            cont_tradition = PersonalStyleGroup.objects.get(group=results['main_tradition'])
        except:
            cont_position,cont_path,cont_tradition = None,None,None
        try:
            bigTrad = BigTraditions.objects.filter(user=request.user).latest('updated_at')
        except:
            bigTrad = None
        try:
            components = Components.objects.filter(user=request.user).latest('updated_at')
        except:
            components = None
        context = {'cont_position':cont_position,'cont_path':cont_path,'cont_tradition':cont_tradition,'BigTrad':bigTrad,'components':components,'format':format}
        return render(request,'between_app/test-home.html',context)
    return render(request,'between_app/test-home.html')


#Therapeutic Positions
@login_required
def positions_list_view(request):
    style_list = PersonalStyle.objects.filter(user=request.user).order_by('-updated_at')
    context = {"style_list":style_list}
    return render(request,'between_app/personal_style/positions_list.html', context)



def take_profile_test(request):
    if request.method !='POST':
        #no data submitted; create a blank form
        form = StyleForm()
    else:
        #POST data submitted; process data
        form = StyleForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            pk = new_form.pk
            if request.user.is_authenticated:
                user = request.user
                new_form.user = user
            new_form.save()
            return redirect('between_app:results',pk)
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'between_app/personal_style/profile_test.html',context)

def take_profile_test_client(request):
    if request.method !='POST':
        #no data submitted; create a blank form
        form = StyleFormClient()
    else:
        #POST data submitted; process data
        form = StyleFormClient(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            pk = new_form.pk
            if request.user.is_authenticated:
                user = request.user
                new_form.therapist = False
                new_form.user = user
            new_form.save()
            return redirect('between_app:results',pk)
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'between_app/personal_style/profile_test.html',context)



def style_detail(request,pk):
    results = PersonalStyle.objects.get(pk=pk)
    context = {'results':results,'format':format}
    return render(request,'between_app/personal_style/style_detail.html',context)

def ps_results(request,pk):
    """show the results of personal style"""
    style_detail = PersonalStyle.objects.get(pk=pk)
    user = request.user
    if user.is_authenticated and style_detail.user != user:
        style_detail.user = user
        style_detail.save()
    results = style_detail.calProfile
    cont_position = PersonalStyleGroup.objects.get(group=results['main_position'])
    cont_path = PersonalStyleGroup.objects.get(group=results['main_path'])
    cont_tradition = PersonalStyleGroup.objects.get(group=results['main_tradition'])
    context = {'results':style_detail,'position':cont_position,'path':cont_path,'tradition':cont_tradition,'pk':pk,'format':format}
    return render(request,'between_app/personal_style/results.html',context)


def positions_content_view(request):
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        content = {'position':position,'path':path,'tradition':tradition}
        context = {"content":content}
        return render(request,'between_app/personal_style/content.html',context)

    
#Components Views
@login_required
def components_list(request):
    list = Components.objects.filter(user=request.user)
    context = {'list':list}    
    return render(request,'between_app/Components/components_list.html',context)

@login_required
def components_detail(request,pk):
    detail = Components.objects.get(pk=pk)
    context = {'components':detail,'format':format} 
    return render(request,'between_app/Components/components_detail.html',context)



def take_components(request):
    """add new client"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = ComponentsForm()
    else:
        #POST data submitted; process data
        form = ComponentsForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('between_app:test_home')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'between_app/Components/components_test.html',context)


#Big traditions Views
@login_required
def big_trad_list(request):
    list = BigTraditions.objects.filter(user=request.user)
    context = {'list':list}    
    return render(request,'between_app/BigTraditions/traditions_list.html',context)

@login_required
def big_trad_detail(request,pk):
    detail = BigTraditions.objects.get(pk=pk)
    context = {'detail':detail,'format':format}
    return render(request,'between_app/BigTraditions/traditions_detail.html',context)


def big_trad_test(request):
    if request.method != 'POST': #Email functionality to the results (making this accesible to non registered users)
        form = BigTradForm()
    else:
        form = BigTradForm(data=request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('between_app:test_home')
    context = {'form':form}
    return render(request,'between_app/BigTraditions/traditions_test.html',context)
