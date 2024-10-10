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
    path('topic/<uuid:topic_pk>/', views.topic, name='topic'),
    #page for adding new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #page for adding a new entry
    path('new_entry/<uuid:topic_pk>/',views.new_entry,name='new_entry'),
    #page for editing an entry
    path('edit_entry/<uuid:entry_pk>/',views.edit_entry,name='edit_entry'),

#After questions CRUD
    #page to see all answers
    path('after_answers/', views.after_answer_date, name = 'after_answer_date'),
    #Detail page for a single answer
    path('after_answer/<uuid:question_pk>/', views.question_item, name='question_item'),
    #questions by andser
    path('after_answer_by_question/', views.after_answer_question, name='after_answer_question'),
    #page adding an after session question
    path('new_question/',views.new_question,name='new_question'),
    #page for editing an entry
    path('edit_question/<uuid:question_pk>/',views.edit_question,name='edit_question'),
    

#creating CRUD
    #page to see all creations by date
    path('creation_by_date/', views.creation_by_date, name = 'creations_by_date'),
    #page to see all creations by title
    path('creation_by_title/', views.creation_by_title, name = 'creations_by_title'),
    #Detail page for a single creation
    path('creation/<uuid:creation_pk>/', views.creation_item, name='creation_item'),
    #page adding an after session question
    path('new_creation/',views.new_creation,name='new_creation'),
    #page for editing an entry
    path('edit_creation/<uuid:creation_pk>/',views.edit_creation,name='edit_creation'),
    
#Shadow's CRUD
    #page to see all shadows by date
    path('shadows_by_date/', views.shadow_by_date, name = 'shadows_by_date'),
    #page to see all creations by title
    path('shadows_by_title/', views.shadow_by_title, name = 'shadows_by_title'),
    #Detail page for a single creation
    path('shadow/<uuid:shadow_pk>/', views.shadow_item, name='shadow_item'),
    #page adding an after session question
    path('new_shadow/',views.new_shadow,name='new_shadow'),
    #page for editing an entry
    path('edit_shadow/<uuid:shadow_pk>/',views.edit_shadow,name='edit_shadow'),
    
    ]