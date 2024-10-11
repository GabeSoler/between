from django.contrib import admin
from .models import Topic,Entry,AfterJournal
# Register your models here.

class EntryInline(admin.TabularInline):
	model:Entry
	

class TopicAdmin(admin.ModelAdmin):
   	inlines : EntryInline
		   
			   
admin.site.register(Topic,TopicAdmin)
admin.site.register(AfterJournal)
