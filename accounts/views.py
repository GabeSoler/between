"""Views from Accounts creation Learning Logs"""
from django.shortcuts import render,redirect
from .models import CommunityProfile, UserStatus,DeleteAccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from .forms import UserStatusForm,CommunityProfileForm,DeleteAccountForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


@login_required
def profile_view(request):
    """deals with password and user details"""
    profile,created_p = CommunityProfile.objects.get_or_create(user=request.user)
    status,created_s = UserStatus.objects.get_or_create(user=request.user)
    context = {'profile':profile,'status':status}
    return render(request,'profile.html',context)

@login_required
def community_profile_edit_view(request):
    profile,_ = CommunityProfile.objects.get_or_create(user=request.user)
    user = request.user
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = CommunityProfileForm(instance=profile)
    else:
        #POST data submitted; process data
        form = CommunityProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = user
            form.save()
            return redirect('accounts:account_profile')
    context = {'profile':profile,'form':form}
    return render(request,'profile/edit-account-profile.html',context)

@login_required
def user_status_edit_view(request): # * I have made this one able to give different permissions to the app
    status,_ = UserStatus.objects.get_or_create(user=request.user)
    user = request.user
    #* Getting 'next' to go back after a redirect
    if request.GET.get('next'):
        next = request.GET.get('next')
    else:
        next = ''
    #* Separating post from get
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = UserStatusForm(instance=status)
    else:
        #POST data submitted; process data
        form = UserStatusForm(instance=status,data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = user
            form.save()            
            # get permissions:
            user_status = UserStatus.objects.get(user=user)
            content_type_user_status = ContentType.objects.get_for_model(UserStatus)
            perm_therapist = Permission.objects.get(        
                            codename="is_therapist",
                            content_type=content_type_user_status)
            perm_diver = Permission.objects.get(        
                            codename="can_dive",
                            content_type=content_type_user_status)
            # add permissions relative to database (using the form was confusing, not registering true and false)
            if user_status.therapist == True:
                user.user_permissions.add(perm_therapist)
            else:
                user.user_permissions.remove(perm_diver)
            #adds permissions to be a diver
            if user_status.diver == True:
                user.user_permissions.add(perm_diver)
                if next:
                    return redirect(next)
            else:
                user.user_permissions.remove(perm_diver)
            return redirect('accounts:account_profile')
    context = {'status':status,'form':form,'next':next}
    return render(request,'profile/status-edit.html',context)

def delete_account_view(request):
    user = request.user
    if request.method != 'POST':
        form = DeleteAccountForm()
    else:
        form = DeleteAccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            if form['confirm'] == True:
                user.delete()
                return redirect('between_app:index')
    context = {'form':form}
    return render(request,'profile/delete.html',context)

