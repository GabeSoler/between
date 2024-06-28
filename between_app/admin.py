from django.contrib import admin
from .models import PersonalStyle,Components,PersonalStyleGroup,PersonalStyleSection,BigTraditions
# Register your models here.

class ContentAdminProperties(admin.ModelAdmin):
   	list_display = ('name','group')

class PSgroupInline(admin.TabularInline): #Allows this model to be inside another
	model = PersonalStyleGroup

class PSAdmin(admin.ModelAdmin):  # inlines: other models inside
	inlines = [
		PSgroupInline,
		]
	list_display = ('section','updated_at')

admin.site.register(PersonalStyle)
admin.site.register(Components)
admin.site.register(PersonalStyleSection,PSAdmin)
admin.site.register(BigTraditions)







