from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Card, CardType, DeckVersion

# Create your tests here.


class DeckTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test_user", password="testtest")
        pass

    def tearDown(self):
        pass

    def test_create_deck(self):
        deck = DeckVersion.objects.create(name="v1")
        decks = DeckVersion.objects.all()
        self.assertEqual(deck.name, "v1")
        self.assertEqual(decks.count(), 1)

    def test_create_card_type(self):
        deck_type = CardType.objects.create(name="test")
        deck_types = CardType.objects.all()
        self.assertEqual(deck_types.count(), 1)
        self.assertEqual(deck_types[0].name, deck_type.name)

    def test_create_deck_cards(self):
        card_type, _ = CardType.objects.get_or_create(name="test")
        deck, _ = DeckVersion.objects.get_or_create(name="v1")
        card = Card.objects.create(name="test", deck_version=deck, card_type=card_type)
        cards = Card.objects.all()
        self.assertEqual(cards.count(), 1)
        self.assertEqual(cards.first().name, card.name)

    def test_select_deck(self):
        self.client.force_login(self.user)
        response = self.client.get("cards/")
        self.assertEqual(response.status_code, 200)

    def test_card_display(self):
        response = self.client.get("cards/")
        self.assertEqual(response.status_code, 200)
