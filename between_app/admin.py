from django.contrib import admin
from .models import Personal_Style, ContentGroup, ContentProperties, ContentSection

# Register your models here.

class PropertiesInLine(admin.TabularInline):
    model = ContentProperties
class GroupsInLine(admin.TabularInline):
    model = ContentGroup

class ContentAdminSection(admin.ModelAdmin):
    inlines = [
        GroupsInLine
    ]
class ContentAdminGroup(admin.ModelAdmin):
    inlines = [
        PropertiesInLine
    ]

class ContentAdminProperties(admin.ModelAdmin):
   	list_display = ('name','group')


admin.site.register(Personal_Style)
admin.site.register(ContentProperties, ContentAdminProperties)
admin.site.register(ContentSection,ContentAdminSection)
admin.site.register(ContentGroup,ContentAdminGroup)



