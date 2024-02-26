from django import forms
from .models import Personal_Style




class StyleForm(forms.ModelForm):
    class Meta:
        model= Personal_Style
        fields = ("follower_1","propositive_1","challenger_1",
                  "acceptant_1","intensive_1","extensive_1",
                  "divider_1","containment_1","becoming_1",
                  "development_1","individuation_1","belonging_1")
        labels = {"follower_1":"I think that people benefit from someone following their process, giving lots of space for them to express their inner world.",
                  "propositive_1":"I think that people benefit by offerening them activities and things to do with what they are feeling or thinking",
                  "challenger_1":"I think that people benefit from someone actively helping them to change what they can.",
                  "acceptant_1":"I think that people benefit by being accepted for who they are, no matter what",
                  "intensive_1":"I think that the world of imagination, ideas and feelings is the most important to consider when helping others",
                  "extensive_1":"I think that the concrete world and being grounded to reality is the most importantn to help someone",
                  "divider_1":"I think that people need help to clarify and be more clear between the different tendencies on their mind.",
                  "containment_1":"I think that people need someone to hold them emotionally and to sustain their complexity without interfering",
                  "becoming_1":"I think that people change and is mutable by engaging with others, nature and things",
                  "development_1":"I think that people need help to realise there is a bigger picture and a more abstract way of seeing problems",
                  "individuation_1":"I think that people are fundamentally individuals and need help to find their singularity.",
                  "belonging_1":"I think that people are fundamentally collective and need help to find a group of belonging."
                  }
        widgets = {"text":forms.RadioSelect()}




