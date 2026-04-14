from django.contrib import admin
from cards_app.models import CardType, DeckVersion, Card


# Register your models here.

class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name','description',)
    list_filter = ('name',)

class DeckVersionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class CardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name','deck_version','card_type')


admin.site.register(CardType,CardTypeAdmin)
admin.site.register(DeckVersion,DeckVersionAdmin)
admin.site.register(Card,CardAdmin)
