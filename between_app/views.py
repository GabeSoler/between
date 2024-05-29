from django.shortcuts import render,redirect
from .models import Personal_Style, Components,BigTraditions,PS_Section,PS_group
from django.views.generic import ListView, DetailView,TemplateView,CreateView
from .forms import StyleForm,ComponentsForm,BigTradForm,SendEmail
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,get_connection
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .content import Content
from django.conf import settings
# Create your views here.

#Start classes with caps
class index_View(TemplateView):
    template_name = 'between_app/index.html'

        
def test_home(request):
    """show all tests"""
    if request.user.is_authenticated:
        try:
            positions = Personal_Style.objects.filter(user=request.user).latest('updated_at')
        except Personal_Style.DoesNotExist:
            positions = None
        try:
            bigTrad = BigTraditions.objects.filter(user=request.user).latest('updated_at')
        except BigTraditions.DoesNotExist:
            bigTrad = None
        try:
            components = Components.objects.filter(user=request.user).latest('updated_at')
        except Components.DoesNotExist:
            components = None
        context = {'positions':positions,'BigTrad':bigTrad,'components':components}
        return render(request,'between_app/test-home.html',context)
    return render(request,'between_app/test-home.html')


#Therapeutic Positions
class PositionListView(LoginRequiredMixin, ListView):
    model = Personal_Style
    context_object_name = 'style_list'
    template_name = 'between_app/personal_style/positions_list.html'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by user
        return qs.filter(user=self.request.user.id)


class takeTestView(CreateView):
    model = Personal_Style
    form_class = StyleForm
    template_name = 'between_app/personal_style/profile_test.html'
    success_url = 'between_app/personal_style/results/'

    def post(self, request, *args, **kwargs):
        form = StyleForm(request.POST)
        try:
            user = request.user
        except:
            try:
                user = get_user_model().objects.get(username='guest')
            except:
                user = get_user_model().objects.create_user(email='guest@guest.guest',username='guest' )
        if form.is_valid():
            profile_test = form.save(commit=False)
            profile_test.user = user
            profile_test.save()
            return HttpResponseRedirect(reverse_lazy('between_app:results', args=[profile_test.pk]))
        return render(request, 'between_app/profile_test.html', {'form': form})



class formDetailView(DetailView):
    model = Personal_Style
    context_object_name ='style_detail'
    template_name = "personal_style/personal_style_detail.html"


class resultsView(DetailView):
    model = Personal_Style
    template_name = 'between_app/personal_style/results.html'
    context_object_name = 'style_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        context["content"] = {'position':position,'path':path,'tradition':tradition}
        return context

def ps_results(request,pk):
    """show the results of personal style"""
    style_detail = Personal_Style.objects.get(pk=pk)
    results = style_detail.calProfile
    cont_position = PS_group.objects.filter(section__section='position')
    cont_path = PS_group.objects.filter(section__section='path')
    cont_tradition = PS_group.objects.filter(section__section='tradition')
    for position in cont_position:
        if results['main_position'] == position.group: #targeting main position result
            position_text = position
            break
        else:
            position_text = 'error'
    for path in cont_path:
        if results['main_path'] == path.group: #targeting main path
            path_text = path
            break
        else:
            path_text = 'error'
    for tradition in cont_tradition:
        if results['main_tradition'] == tradition.group: #targeting main tradition
            tradition_text = tradition
            break
        else:
            path_text = 'error'
    
    if request.method != 'POST': #Email functionality to the results (making this accesible to non registered users)
        form = SendEmail()
    else:
        form = SendEmail(data=request.POST)
        if form.is_valid:
            instance = form.save()
            user_email = instance.email
            user_email = tuple(user_email)
        else:
            return html_content("<h3>Please add a valid email!</h3>")
        with get_connection(
            host= settings.RESEND_SMTP_HOST,
            port= settings.RESEND_SMTP_PORT,
            username= settings.RESEND_SMTP_USERNAME,
            password= settings.RESEND_API_KEY,
            use_tls=True,
            ) as connection:
                subject, from_email, to = 'Profile', 'crea@therapy.com', user_email
                html_content = render_to_string('between_app/email/personal_style_email.html', 
                                                {'position':position_text,'path':path_text,'tradition':tradition_text}) # render with dynamic value
                #text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
                msg = EmailMessage(
                    subject=subject,
                    body=html_content,
                    to=user_email,
                    from_email=from_email,
                    connection=connection)
                msg.content_subtype = 'html'
                msg.send()
                return redirect('between_app:test_home')
    context = {'position':position_text,'path':path_text,'tradition':tradition_text,'form':form,'pk':pk}
    return render(request,'between_app/personal_style/results_email.html',context)



class contentView(TemplateView):
    template_name = 'between_app/personal_style/content.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        context["content"] = {'position':position,'path':path,'tradition':tradition}
        return context

    
#Components Views

class takeComponentstView(CreateView):
    model = Components
    form_class = ComponentsForm
    template_name = 'between_app/Components/components_test.html'
    success_url = 'between_app/test_home'

    def post(self, request, *args, **kwargs):
        form = ComponentsForm(request.POST)
        try:
            user = request.user
        except NameError:
            user = get_user_model().objects.get(username='guest')
        except:
            user = get_user_model().objects.create_user(email='guest@guest.guest',username='guest' )
        if form.is_valid():
            profile_test = form.save(commit=False)
            profile_test.user = user
            profile_test.save()
            return HttpResponseRedirect(reverse_lazy('between_app:test_home'))
        return render(request, 'between_app/Components/components_test.html', {'form': form})

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
class takeTraditionsView(CreateView):
    model = BigTraditions
    form_class = BigTradForm
    template_name = 'between_app/BigTraditions/traditions_test.html'
    success_url = 'between_app/results/'

    def post(self, request, *args, **kwargs):
        form = StyleForm(request.POST)
        try:
            user = get_user_model().objects.get(pk=request.user.id)
        except NameError:
            user = get_user_model().objects.get(username='guest')
        except:
            user = get_user_model().objects.create_user(email='guest@guest.guest',username='guest' )
        if form.is_valid():
            profile_test = form.save(commit=False)
            profile_test.user = user
            profile_test.save()
            return HttpResponseRedirect(reverse_lazy('between_app:index'))
        return render(request, 'between_app/BitTraditions/traditions_test.html', {'form': form})
    