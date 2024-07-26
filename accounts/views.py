"""Views from Accounts creation Learning Logs"""
from django.shortcuts import render,redirect
from .models import CommunityProfile, UserStatus
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    """deals with pasword and user details"""
    profile,created_p = CommunityProfile.objects.get_or_create(user=request.user)
    status,created_s = UserStatus.objects.get_or_create(user=request.user)
    context = {'profile':profile,'status':status}
    return render(request,'templates/account/profile.html',context)

@login_required
def community_profile_edit_view(request):
    profile = CommunityProfile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request,'templates/profile/account-profile.html',context)

@login_required
def user_status_edit_view(request):
    profile = CommunityProfile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request,'templates/profile/account-profile.html',context)

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