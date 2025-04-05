from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid
from django.utils.functional import cached_property


class PersonalStyle(models.Model):
    """A therapeutic profile based in therapeutic positions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),blank=True,null=True,on_delete=models.SET_NULL)
    follower_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    propositive_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    challenger_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    acceptant_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    intensive_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    extensive_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    divider_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    containment_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    becoming_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    development_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    individuation_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    belonging_1 = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")

    therapist = models.BooleanField(default=True)

    @cached_property
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
    
    @cached_property
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
    
    @cached_property
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
 
    @cached_property
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
    
    @cached_property
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
        return reverse("between_app:style_detail", kwargs={"pk": self.pk})
        
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
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True,blank=True)
    
    #Subjective
    body = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    feelings = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    expression = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    thoughts = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    narrative = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    #extended awareness
    dreaming = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    re_prog = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    subliminal = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    subparts = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    spiritual = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    #Context work
    relational = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    systems = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    setup = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    transOb = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    family = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    #Culture
    antropology = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    arts = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    politics = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    philosophy = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    worldview = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    #identity
    individuation = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    sex_gender = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    values = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    belonging = models.IntegerField(default=0,help_text="Training until the center, forward expertise")
    roles = models.IntegerField(default=0,help_text="Training until the center, forward expertise")

    @cached_property
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
    def __str__(self):
        new_name = f"{self.user}:{self.updated_at}"
        return new_name

class BigTraditions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,blank=True,null=True)

    #Big five traditions
    hemeneutic = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    phenomenological = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    cybernetic = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    spiritual = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    scientific = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    constructive = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    participatory = models.IntegerField(default=50,help_text="Move right for support of the statement, and left for disagreement")
    @cached_property
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
    def __str__(self):
        new_name = f"{self.user}:{self.updated_at}"
        return new_name

#Content fixtures


class PersonalStyleSection(models.Model):
    updated_at = models.DateTimeField(auto_now=True, editable=True)
    section = models.CharField(max_length=20,default='') #position, path,tradition
class PersonalStyleGroup(models.Model):
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    section = models.ForeignKey(PersonalStyleSection,default=None, on_delete=models.CASCADE) # profile, path, tradition
    group = models.CharField(max_length=20, default='') #compassionate,playgul, etc
    image = models.CharField(max_length=300, default='')
    description = models.TextField(default='')
    shadow = models.TextField(default='')
    traditions = models.TextField(default='')
    authors = models.TextField(default='')

class EmailSent(models.Model):
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

