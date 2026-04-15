from django.db import models

# Create your models here.

class DeckVersion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __repr__(self):
        return f"DeckVersion:{self.name}"

class CardType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    bg_color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __repr__(self):
        return f"CardType:{self.name}"

class Card(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deck_version = models.ForeignKey(DeckVersion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    text = models.TextField(blank=True)
    alt_text = models.TextField(blank=True)
    card_type = models.ForeignKey(CardType, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Card:{self.name}"