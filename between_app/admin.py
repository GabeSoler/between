from django.contrib import admin
from .models import Personal_Style, ContentGroup, ContentProperties

# Register your models here.

class PropertiesInLine(admin.TabularInline):
    model = ContentProperties
class GroupsInLine(admin.TabularInline):
    model = ContentGroup

class ContentAdminSection(admin.ModelAdmin):
    inlines = [
        GroupsInLine
    ]
    list_display = ('name',)

class ContentAdminGroup(admin.ModelAdmin):
    inlines = [
        PropertiesInLine
                ]
    list_display = ('name','section')


class ContentAdminProperties(admin.ModelAdmin):
   	list_display = ('name','group')


admin.site.register(Personal_Style)
admin.site.register(ContentProperties, ContentAdminProperties) #hide when working
admin.site.register(ContentGroup,ContentAdminGroup)



