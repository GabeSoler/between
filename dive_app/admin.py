from django.contrib import admin
from .models import Creation,Shadow

# Admin Models

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
		

admin.site.register(Creation,CreationAdmin)
admin.site.register(Shadow,ShadowAdmin)