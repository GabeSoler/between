from django.contrib import admin
from .models import Topic,Entry,AfterJournal,Creation,Shadow
# Register your models here.

class EntryInline(admin.TabularInline):
	model:Entry
	

class TopicAdmin(admin.ModelAdmin):
   	inlines : EntryInline
		   
			   

class CreationAdmin(admin.ModelAdmin):
	    list_display = [
        'title',
        'date_added',
    ]
class ShadowAdmin(admin.ModelAdmin):
	    list_display = [
        'title',
        'date_added',
    ]

admin.site.register(Topic,TopicAdmin)
admin.site.register(AfterJournal)
admin.site.register(Creation,CreationAdmin)
admin.site.register(Shadow,ShadowAdmin)
