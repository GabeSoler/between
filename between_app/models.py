from django.db import models
from django.contrib.auth import get_user_model
from .choices import Response_Choices
from django.urls import reverse
import uuid


class Personal_Style(models.Model):
    """A therapeutic profile based in therapeutic positions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),blank=True,null=True,on_delete=models.PROTECT)
    follower_1 = models.IntegerField(default=1)
    propositive_1 = models.IntegerField(default=1)
    challenger_1 = models.IntegerField(default=1)
    acceptant_1 = models.IntegerField(default=1)
    intensive_1 = models.IntegerField(default=1)
    extensive_1 = models.IntegerField(default=1)
    divider_1 = models.IntegerField(default=1)
    containment_1 = models.IntegerField(default=1)
    becoming_1 = models.IntegerField(default=1)
    development_1 = models.IntegerField(default=1)
    individuation_1 = models.IntegerField(default=1)
    belonging_1 = models.IntegerField(default=1)

    @property
    def calPosition(self):
        #Therapeutic Positions
        compassionate = self.follower_1 + self.acceptant_1
        inquisitive = self.follower_1 + self.challenger_1
        playful = self.propositive_1 + self.acceptant_1
        changer = self.propositive_1 + self.challenger_1
        therapeuticPositions = {'compassionate': compassionate/2, 
                                'inquisitive':inquisitive/2,
                                'playful':playful/2, 
                                 'changer':changer/2}
        return therapeuticPositions
    
    @property
    def calPath(self):
        #Paths
        dreamer = self.intensive_1 + self.containment_1
        sage = self.intensive_1 + self.divider_1
        carer = self.extensive_1 + self.containment_1
        explorer = self.extensive_1 + self.divider_1
        therapeutic_paths = {'dreamer':dreamer/2,
                             'sage':sage/2,
                             'carer':carer/2,
                             'explorer':explorer/2}
        return therapeutic_paths
    
    @property
    def calTradition(self):
        #Person vs tradition relaionship
        artist = self.becoming_1 + self.individuation_1
        warrior = self.development_1 + self.individuation_1
        leader = self.becoming_1 + self.belonging_1
        coach = self.development_1 + self.belonging_1
        tradition_relationship = {'artist':artist/2,
                                  'warrior':warrior/2,
                                  'leader':leader/2,
                                  'coach':coach/2}
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
    
    @property
    def raw(self):
        position = {
            'follower':self.follower_1,
            'propositive':self.propositive_1, 
            'challenger':self.challenger_1, 
            'acceptant':self.acceptant_1, 
        }
        path = {
            'intensive':self.intensive_1,
            'extensive':self.extensive_1,
            'divider':self.divider_1, 
            'containment':self.containment_1, 
        }
        
        tradition = {
            'becoming':self.becoming_1,
            'development':self.development_1, 
            'individuation':self.individuation_1, 
            'belonging':self.belonging_1, 
        }
        return {'position':position,'path':path,'tradition':tradition}


    def get_absolute_url(self):
        return reverse("between_app:results", kwargs={"pk": self.pk})
        
    def __str__(self):
        new_name = f"{self.user}:{self.updated_at}"
        return new_name
    class Meta():
        get_latest_by = 'updated_at'

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

    @property
    def results(self):
        results = {
            'subjective':{
                'body':self.body,
                'feelings':self.feelings,
                'expression':self.expression,
                'thoughts':self.thoughts,
                'narrative':self.narrative,
            },
    
        
            'extended':{
                'dreaming':self.dreaming,
                're-programming':self.re_prog,
                'subliminal':self.subliminal,
                'subparts':self.subparts,
                'spiritual':self.spiritual,
            },
            'context':{
                'relational':self.relational,
                'systems':self.systems,
                'setup':self.setup,
                'transitional':self.transOb,
                'family':self.family,
            },
            'culture':{
                'antropology':self.antropology,
                'arts':self.arts,
                'politics':self.politics,
                'philosophy':self.philosophy,  
                'worldview':self.worldview,

            },
            'identity':{
                'individuation':self.individuation,
                'sex and gender':self.sex_gender,
                'values':self.values,
                'belonging':self.belonging,
                'roles':self.roles,
            }
        }
        return results


class BigTraditions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)

    #Big five traditions
    hemeneutic = models.IntegerField(default=1)
    phenomenological = models.IntegerField(default=1)
    cybernetic = models.IntegerField(default=1)
    spiritual = models.IntegerField(default=1)
    scientific = models.IntegerField(default=1)
    constructive = models.IntegerField(default=1)
    participatory = models.IntegerField(default=1)
    @property
    def results(self):
        results = {
                'hemeneutic':self.hemeneutic,
                'phenomenological':self.phenomenological,
                'cybernetic':self.cybernetic,
                'spiritual':self.spiritual,
                'scientific':self.scientific,
                'constructive':self.constructive,
                'participatory':self.participatory,
            }
        return results
    

#Content fixtures


class PS_Section(models.Model):
    updated_at = models.DateTimeField(auto_now=True, editable=True)
    section = models.CharField(max_length=20,default='') #position, path,tradition
class PS_Group(models.Model):
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    section = models.ForeignKey(PS_Section,default=None, on_delete=models.CASCADE)
    group = models.CharField(max_length=20, default='') #compassionate,playgul, etc
    image = models.CharField(max_length=300, default='')
    description = models.TextField(default='')
    shadow = models.TextField(default='')
    traditions = models.TextField(default='')
    authors = models.TextField(default='')

class EmailSent(models.Model):
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

