from django.db import models
from django.contrib.auth import get_user_model
from .choices import Response_Choices
from django.urls import reverse
import uuid
import floppyforms as forms


class Personal_Style(models.Model):
    """A therapeutic profile based in therapeutic positions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)
    follower_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    propositive_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    challenger_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    acceptant_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    intensive_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    extensive_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    divider_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    containment_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    becoming_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    development_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    individuation_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    belonging_1 = models.IntegerField(choices=Response_Choices.choices, default=1)
    
    def __str__(self):
        new_name = f"{self.user}:{self.updated_at}"
        return new_name

    @property
    def calPosition(self):
        #Therapeutic Positions
        compassionate = self.follower_1 + self.acceptant_1
        inquisitive = self.follower_1 + self.challenger_1
        playful = self.propositive_1 + self.acceptant_1
        changer = self.propositive_1 + self.challenger_1
        therapeuticPositions = {'compassionate': compassionate, 
                                'inquisitive':inquisitive,
                                'playful':playful, 
                                 'changer':changer}
        return therapeuticPositions
    
    @property
    def calPath(self):
        #Paths
        dreamer = self.intensive_1 + self.containment_1
        sage = self.intensive_1 + self.divider_1
        carer = self.extensive_1 + self.containment_1
        explorer = self.extensive_1 + self.divider_1
        therapeutic_paths = {'dreamer':dreamer,
                             'sage':sage,
                             'carer':carer,
                             'explorer':explorer}
        return therapeutic_paths
    
    @property
    def calTradition(self):
        #Person vs tradition relaionship
        artist = self.becoming_1 + self.individuation_1
        warrior = self.development_1 + self.individuation_1
        lider = self.becoming_1 + self.belonging_1
        coach = self.development_1 + self.belonging_1
        tradition_relationship = {'artist':artist,
                                  'warrior':warrior,
                                  'lider':lider,
                                  'coach':coach}
        return tradition_relationship
 
    @property
    def calProfile(self):
        #calculating max scores (not working)
        position = dict(self.calPosition)
        path = dict(self.calPath)
        tradRel = dict(self.calTradition)
        main_position = max(position, key=lambda x: position[x])
        main_path = max(path, key=lambda x:path[x])
        main_tradRel = max(tradRel, key=lambda x:tradRel[x])
        profile_dict = {'main_position':main_position,
                        'main_path':main_path,
                        'main_tradition':main_tradRel}
        return profile_dict

    def get_absolute_url(self):
        return reverse("between_app:results", kwargs={"pk": self.pk})
    

class Components(models.Model):
    """therapeutic components"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)
    
    #Subjective
    body = models.IntegerField(default=0)
    feelings = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    thoughts = models.IntegerField(default=0)
    narrative = models.IntegerField(default=0)
    #extended awareness
    dreaming = models.IntegerField(default=0)
    re_prog = models.IntegerField(default=0)
    subliminal = models.IntegerField(default=0)
    subparts = models.IntegerField(default=0)
    spiritual = models.IntegerField(default=0)
    #Context work
    relational = models.IntegerField(default=0)
    systems = models.IntegerField(default=0)
    setup = models.IntegerField(default=0)
    transOb = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    #Culture
    antropology = models.IntegerField(default=0)
    arts = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    philosophy = models.IntegerField(default=0)
    worldview = models.IntegerField(default=0)
    #identity
    individuation = models.IntegerField(default=0)
    sex_gender = models.IntegerField(default=0)
    values = models.IntegerField(default=0)
    belonging = models.IntegerField(default=0)
    roles = models.IntegerField(default=0)
    

class BigTraditions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)

    #Big five traditions
    hemeneutic = models.IntegerField(choices=Response_Choices.choices, default=1)
    phenomenological = models.IntegerField(choices=Response_Choices.choices, default=1)
    cybernetic = models.IntegerField(choices=Response_Choices.choices, default=1)
    spiritual = models.IntegerField(choices=Response_Choices.choices, default=1)
    scientific = models.IntegerField(choices=Response_Choices.choices, default=1)






class ContentGroup(models.Model):
    """for the group, like position, path, tradition"""
    section = models.ForeignKey(Personal_Style, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class ContentProperties(models.Model):
    """for the individual parts like compassionate, playful"""
    group = models.ForeignKey(ContentGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    shadow = models.TextField(default='')
    traditions = models.TextField(default='')
    authors = models.TextField(default='')