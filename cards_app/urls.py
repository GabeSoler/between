from django.urls import path

from .views import card_game_view, card_list, select_card_type_view

app_name = "cards_app"

urlpatterns = [
    path("/card-list", card_list, name="card_list"),
    path("", select_card_type_view, name="select_card_type"),
    path("<int:type_pk>", select_card_type_view, name="select_card_type"),
    path("/game/", card_game_view, name="game_card_type"),
    path("/game/<int:type_pk>/", card_game_view, name="game_card_type"),
]
