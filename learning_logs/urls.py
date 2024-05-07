"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

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

    #page adding an after session question
    path('afterQuestions/',views.afterQuestions,name='afterQuestions'),
    ]