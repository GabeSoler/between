from django.contrib import admin
from .models import Personal_Style
# Register your models here.

class ContentAdminProperties(admin.ModelAdmin):
   	list_display = ('name','group')


admin.site.register(Personal_Style)




