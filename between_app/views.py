from django.shortcuts import render,redirect
from .models import Personal_Style, Components,BigTraditions
from django.views.generic import ListView, DetailView,TemplateView,CreateView
from .forms import StyleForm,ComponentsForm,BigTradForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .content import Content
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
    template_name = 'between_app/profile_test.html'
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
    template_name = 'between_app/results.html'
    context_object_name = 'style_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        context["content"] = {'position':position,'path':path,'tradition':tradition}
        return context


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
    