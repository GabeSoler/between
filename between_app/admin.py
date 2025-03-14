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

class PersonalStyleAdmin(admin.ModelAdmin):
   	list_display = ('created_at','user')
	   
class ComponentsAdmin(admin.ModelAdmin):
   	list_display = ('created_at','user')
	   
class BigTradAdmin(admin.ModelAdmin):
   	list_display = ('created_at','user')


admin.site.register(PersonalStyle,PersonalStyleAdmin)
admin.site.register(Components,ComponentsAdmin)
admin.site.register(PersonalStyleSection,PSAdmin)
admin.site.register(BigTraditions,BigTradAdmin)







