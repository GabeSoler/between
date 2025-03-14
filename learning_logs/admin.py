from django.contrib import admin
from .models import Topic,Entry,AfterJournal
# Register your models here.

class EntryInline(admin.TabularInline):
	model = Entry
	

class TopicAdmin(admin.ModelAdmin):
	inlines = [EntryInline,]
	list_display = ('date_added','text','owner')


class AfterJournalAdmin(admin.ModelAdmin):
   	list_display = ('date_added','question','owner')

			   
admin.site.register(Topic,TopicAdmin)
admin.site.register(AfterJournal,AfterJournalAdmin)
