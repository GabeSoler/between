""" urls for dive app """

from django.urls import path

from . import views

app_name = 'dive_app'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),


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

#Assemble's CRUD
    #page to see all assemble by date
    path('assemble_by_date/', views.assemble_by_date, name = 'assemble_by_date'),
    #page to see all creations by title
    path('assemble_by_title/', views.assemble_by_title, name = 'assemble_by_title'),
    #Detail page for a single creation
    path('assemble/<uuid:assemble_pk>/', views.assemble_item, name='assemble_item'),
    #page adding an after session question
    path('new_assemble/',views.new_assemble,name='new_assemble'),
    #page for editing an entry
    path('edit_assemble/<uuid:assemble_pk>/',views.edit_assemble,name='edit_assemble'),
]