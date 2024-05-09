"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

#Topics CRUD
    #page to see all topics
    path('topics/', views.topics, name = 'topics'),
    #Detail page for a single topic
    path('topics/<uuid:topic_id>/', views.topic, name='topic'),
    #page for adding new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #page for adding a new entry
    path('new_entry/<uuid:topic_id>/',views.new_entry,name='new_entry'),
    #page for editing an entry
    path('edit_entry/<uuid:entry_id>/',views.edit_entry,name='edit_entry'),

#After questions CRUD
    #page to see all answers
    path('after_answers/', views.after_answer_date, name = 'after_answer_date'),

    #Detail page for a single answer
    path('after_answer/<uuid:topic_id>/', views.after_answer_question, name='after_answer_question'),


    #page adding an after session question
    path('new_question/',views.new_question,name='new_question'),

    
    #page for editing an entry
    path('edit_question/<uuid:entry_id>/',views.edit_question,name='edit_question'),
    ]