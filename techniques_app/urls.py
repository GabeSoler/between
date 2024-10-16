"""defines the urls for the tecniques_app"""

from django.urls import path
from . import views

app_name = 'techniques_app'

urlpatterns = [
    # page of user's techniques
    path('',views.index,name='index'),

    # page for community techniques from a components__group list
    path('components_list/',views.group_list_community_view,name='components_list'),
    path('techniques_short_community/<int:comp_id>/',views.techniques_short_community_view,name='techniques_short_community'),
    path('techniques_long_community/',views.techniques_long_community_view,name='techniques_long_community'),
    
    # page to see a full technique entry
    path('technique/<uuid:tch_pk>/',views.technique_view, name='technique'),

    # Editing functionalities
    path('new_technique/',views.new_technique_view, name='new_technique'),
    path('edit_technique/<uuid:tch_pk>/',views.edit_technique_view,name='edit_technique'),
    
    # Saved techniques
    path('save_technique/<uuid:tch_pk>/',views.save_technique_view,name='save_technique'),
    path('saved_techniques/',views.saved_techniques_view,name='saved_techniques'),

    # Deleting
    path('delete_saved_technique/<uuid:tch_pk>/',views.delete_saved_technique_view,name='delete_saved_technique'),
    path('delete_technique/<uuid:tch_pk>/',views.delete_technique_view,name='delete_technique'),

    # Techniques per user
    path('author_list/<uuid:tch_pk>/',views.author_techniques_view, name='author_list'),

    ]

