"""defines the urls for the tecniques_app"""

from django.urls import path
from . import views

app_name = 'techniques_app'

urlpatterns = [
    #page of user's techniques
    path('',views.index,name='index'),

    #page for community techniques from a components__group list
    path('group_list_community/',views.group_list_community,name='components_list'),
    path('techniques_short_community/<int:comp_id>/',views.techniques_short_community,name='techniques_short_community'),
    path('techniques_long_community/',views.techniques_long_community,name='techniques_long_community'),
    
    #page to see a full technique entry
    path('technique/<uuid:tch_pk>/',views.technique, name='technique'),

    #editting funtionalities
    path('new_technique/',views.new_technique, name='new_technique'),
    path('edit_technique/<uuid:tch_pk>/',views.edit_technique,name='edit_technique'),
    
    #Saved techniques
    path('save_technique/<uuid:tch_pk>/',views.save_technique,name='save_technique'),
    path('delete_technique/<uuid:tch_pk>/',views.delete_technique,name='delete_technique'),
    path('saved_techniques/',views.saved_techniques,name='saved_techniques'),
    ]

