from django.shortcuts import render,redirect
from .models import Topic,Entry,AfterJournal
from .forms import TopicForm,EntryForm,AfterForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

#Functions
def check_owner(topic_owner,request_user):
    if topic_owner != request_user:
        raise Http404

#Views

def index(request):
    """show all topics"""
    if not request.user.is_authenticated:
        return render(request,'learning_logs/index.html')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')[:3]
    questions = AfterJournal.objects.filter(owner=request.user).order_by('date_added')[:3]
    context = {'topics':topics,'questions':questions}
    return render(request,'learning_logs/index.html',context)

#Topic's CRUD
@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topic/topics.html',context)

@login_required
def topic(request, topic_pk):
    """show a single topic nad all its entries"""
    topic = Topic.objects.get(pk=topic_pk)
    #make sure topics belong to current user
    check_owner(topic.owner,request.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic/topic.html',context)

def new_topic(request):
    """add new topic"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = TopicForm()
    else:
        #POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('learning_logs:topics')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'learning_logs/topic/new_topic.html',context)

@login_required
def new_entry(request,topic_pk):
    """add a new entry for a particular topic"""
    topic = Topic.objects.get(pk=topic_pk)
    if request.method !='POST':
        #no data submitted, create a blank form
        form = EntryForm()
    else:
        #POST data submited; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topics')
    #display blank or invalid form
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/topic/new_entry.html',context)

@login_required
def edit_entry(request,entry_pk):
    """edit an existing entry"""
    entry = Entry.objects.get(pk=entry_pk)
    topic = entry.topic
    check_owner(topic.owner,request.user)
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


#After question's CRUD
@login_required
def question_item(request,question_pk):
    """show an item of creation"""
    QuestionItem = AfterJournal.objects.get(pk=question_pk)
    check_owner(QuestionItem.owner,request.user)
    context = {'question':QuestionItem}
    return render(request,'learning_logs/question/question_item.html',context)


@login_required
def after_answer_date(request):
    """show all answers by date"""
    answers_by_date = AfterJournal.objects.filter(owner=request.user).order_by('-date_added')
    context = {'answers':answers_by_date}
    return render(request,'learning_logs/question/after_by_date.html',context)

@login_required
def after_answer_question(request):
    """show all answers by question"""
    answers_by_question = AfterJournal.objects.filter(owner=request.user).order_by('question','date_added')
    context = {'answers':answers_by_question}
    return render(request,'learning_logs/question/after_by_question.html',context)

def new_question(request):
    """add new question"""
    if request.method !='POST':
        #no data submitted; create a blank form
        form = AfterForm()
    else:
        #POST data submitted; process data
        form = AfterForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user 
            new.save()
            return redirect('learning_logs:after_answer_date')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'learning_logs/question/create_Question.html',context)


@login_required
def edit_question(request,question_pk):
    """edit an existing entry"""
    AfterQuestion = AfterJournal.objects.get(pk=question_pk)
    check_owner(AfterQuestion.owner,request.user)
    if request.method != 'POST':
        #initial request;pre-fill form with the current entry
        form = AfterForm(instance=AfterQuestion)
    else:
        #POST data submitted; process data
        form = AfterForm(instance=AfterQuestion,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_pk=topic.pk)
    context = {'question':AfterQuestion,'form':form}
    return render(request,'learning_logs/question/edit_Question.html',context)

