from django.contrib import admin
from .models import Creation,Shadow,AssembleModel

# Admin Models

class CreationAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'date_added',
    'owner'
    ]
class ShadowAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'date_added',
    'owner'
    ]

class AssembleModelAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'date_added',
    'owner'
    ]
		

admin.site.register(Creation,CreationAdmin)
admin.site.register(Shadow,ShadowAdmin)
admin.site.register(AssembleModel,AssembleModelAdmin)