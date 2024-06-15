from django.contrib import admin
from .models import Personal_Style,Components,PS_Group,PS_Section
# Register your models here.

class ContentAdminProperties(admin.ModelAdmin):
   	list_display = ('name','group')

class PSgroupInline(admin.TabularInline): #Allows this model to be inside another
	model = PS_Group

class PSAdmin(admin.ModelAdmin):  # inlines: other models inside
	inlines = [
		PSgroupInline,
		]
	list_display = ('section','updated_at')

admin.site.register(Personal_Style)
admin.site.register(Components)
admin.site.register(PS_Section,PSAdmin)






