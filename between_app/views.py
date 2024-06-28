from django.shortcuts import render,redirect
from .models import PersonalStyle, Components,BigTraditions,PersonalStyleGroup
from django.views.generic import ListView,TemplateView
from .forms import StyleForm,ComponentsForm,BigTradForm,SendEmail
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
class PositionListView(LoginRequiredMixin, ListView):
    model = PersonalStyle
    context_object_name = 'style_list'
    template_name = 'between_app/PersonalStyle/positions_list.html'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by user
        return qs.filter(user=self.request.user.id)


def take_profile_test(request):
    if request.method !='POST':
        #no data submitted; create a blank form
        form = StyleForm()
    else:
        #POST data submitted; process data
        form = StyleForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            if request.user.is_authenticated:
                user = request.user
                new.user = user
            new.save()
            return redirect('between_app:results',new.pk)
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'between_app/PersonalStyle/profile_test.html',context)



def style_detail(request,pk):
    results = PersonalStyle.objects.get(pk=pk)
    context = {'results':results,'format':format}
    return render(request,'between_app/PersonalStyle/style_detail.html',context)

def ps_results(request,pk):
    """show the results of personal style"""
    style_detail = PersonalStyle.objects.get(pk=pk)
    results = style_detail.calProfile
    cont_position = PersonalStyleGroup.objects.get(group=results['main_position'])
    cont_path = PersonalStyleGroup.objects.get(group=results['main_path'])
    cont_tradition = PersonalStyleGroup.objects.get(group=results['main_tradition'])
    if request.method != 'POST': #Email functionality to the results (making this accesible to non registered users)
        form = SendEmail()
    else:
        form = SendEmail(data=request.POST)
        if form.is_valid():
            instance = form.save()
            user_email = instance.email
            html_content = render_to_string('between_app/email/PersonalStyle_email.html', 
                                            {'position':cont_position,'path':cont_path,'tradition':cont_tradition}) # render with dynamic value
            text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
            msg = EmailMultiAlternatives(
                subject='Profile',
                body=text_content,
                to=[user_email],
                from_email='gabriel@crea-therapy.com',
                )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect('between_app:test_home')
        else:
            pass
    context = {'results':style_detail,'position':cont_position,'path':cont_path,'tradition':cont_tradition,'form':form,'pk':pk,'format':format}
    return render(request,'between_app/PersonalStyle/results_email.html',context)



class contentView(TemplateView):
    template_name = 'between_app/PersonalStyle/content.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        context["content"] = {'position':position,'path':path,'tradition':tradition}
        return context

    
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



@login_required
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


@login_required
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
