"""Views from Accounts creation Learning Logs"""
from django.shortcuts import render,redirect
from .models import CommunityProfile, UserStatus,DeleteAccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from .forms import UserStatusForm,CommunityProfileForm,DeleteAccountForm

@login_required
def profile_view(request):
    """deals with password and user details"""
    profile,created_p = CommunityProfile.objects.get_or_create(user=request.user)
    status,created_s = UserStatus.objects.get_or_create(user=request.user)
    context = {'profile':profile,'status':status}
    return render(request,'profile.html',context)

@login_required
def community_profile_edit_view(request):
    profile = CommunityProfile.objects.filter(user=request.user).last()
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
def user_status_edit_view(request):
    status = UserStatus.objects.filter(user=request.user).last()
    user = request.user
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
            return redirect('accounts:account_profile')
    context = {'status':status,'form':form}
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


#example
'''
@login_required
def edit_entry(request,entry_pk):
    """edit an existing entry"""
    entry = Entry.objects.get(pk=entry_pk)
    topic = entry.topic
    check_owner(entry.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_pk=topic.pk)
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/topic/edit_entry.html',context)

    '''