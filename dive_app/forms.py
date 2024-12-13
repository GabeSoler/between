from django import forms 
from .models import Creation,Shadow,AssembleModel



class CreationForm(forms.ModelForm):
    class Meta:
        model = Creation
        fields = ['goal','text_sensation','text_conection','text_metaphore','text_concepts','text_craft','title']
        labels = {'goal':"Please, write the goal for this creation (it may change on the way)",
                  'text_sensation':'Explore how this goal feels in your body, what comes to your senses, internal and external. Try to write a description of what you have expereinced.',
                  'text_conection':"Now, without losing this feeling, see if you can associate it with people, a group or someone, allow the sensation to guide you. Write down who did you think about.",
                  'text_metaphore':"Keeping the feelings of the connection now relax your mind. Come back to your body sensations for a few seconds. Now, observe your sensations, their colours, textures and forms. Relax into this observation and let it take you, to new images, memories or sensations.",
                  'text_concepts':"After an image, memory or sensation has taken place, you can now describe it with words and concepts bellow. Then as you write, take notes of the ideas that emerge.",
                  'text_craft':"Imagine something you could do with these feelings, images and ideas, something concrete that can combine the different aspects of these journey.",
                  'title':"Lets end with a title for reflection, so you can remember it later (it will appear as a title in your list of entries)"}
        widgets = {'text_sensation':forms.Textarea(attrs={'cols':80}),
                   'text_conection':forms.Textarea(attrs={'cols':80}),
                   'text_metaphore':forms.Textarea(attrs={'cols':80}),
                   'text_concepts':forms.Textarea(attrs={'cols':80}),
                   'text_craft':forms.Textarea(attrs={'cols':80})}

class ShadowForm(forms.ModelForm):
    class Meta:
        model = Shadow
        fields = ['goal','text_opossite_style','text_opposite_sex','text_oppossite_elements','text_transf_characters','text_furor_curandis','text_trauma_history','text_trauma_triggers','text_care_plan','title']
        labels = {'goal':"Please write your goal for this exploration (it can change on the way) (required)",
                  'text_opossite_style':"Reflect on the profile you have and the areas that you scored the lowest, or styles you know feel difficult or annoying. These are your opposite style and may say something about your shadow",
                  'text_opposite_sex':"Reflect on your sexual orientation and gender, try to imagine how would you be if on an opposite side, how would that feel?(This give us clues about our Anima and Animus)",
                  'text_oppossite_elements':"Reflect on what are your preferred elements and what are your opposites. Here fire is connected with intuition, air with reason, water with emotions and earth with sensations (Jungian personalities).",
                  'text_transf_characters':"Here explore what type of characters appear in your transference and countertransference, who do you tend to embody, which type of parent, which type of child?",
                  'text_furor_curandis':"In this space reflect on your passion for helping others, and how this appears in sessions. When we get too passionate about helping we lose sight of ourselves and others, and it may become iatrogenic.",
                  'text_trauma_history':"In this section please reflect on your trauma history, what do you remember of your childhood, your fears and conflicts. Many things may be blocked and appear later on your journey.",
                  'text_trauma_triggers':"Are there topics or people that make you feel uncomfortable? or even anxious? These may be your trauma triggers, please write them here.",
                  'text_care_plan':"Please have a read of what you have written above and think of actions that may help you to accept and care for your weaker parts, your shadows and dark spaces.",
                  'title':"To finish, please give a title to this exploration, and it will appear as a link for you to see it again later. (required)"}
        widgets = {'text_opossite_style':forms.Textarea(attrs={'cols':80}),
                   'text_opposite_sex':forms.Textarea(attrs={'cols':80}),
                   'text_oppossite_elements':forms.Textarea(attrs={'cols':80}),
                   'text_transf_characters':forms.Textarea(attrs={'cols':80}),
                   'text_furor_curandis':forms.Textarea(attrs={'cols':80}),
                   'text_trauma_history':forms.Textarea(attrs={'cols':80}),
                   'text_trauma_triggers':forms.Textarea(attrs={'cols':80}),
                   'text_care_plan':forms.Textarea(attrs={'cols':80}),
                    }


class AssembleForm(forms.ModelForm):
    class Meta:
        model = AssembleModel
        fields = ["position","reality_assumptions","change","relational","ontology","knowledge","traditions","components","clients","simple_words","title",]
        labels = {
    "position":"Write how do you feel about your personal position's test.",
    "clients":"Who do you want to work with and how it connects with what you have written above?",
    "reality_assumptions":"Write a spontaneously what do your feel more relevant about your world right now.",
    "change":"Write spontaneity what do you feel makes you and others change.",
    "relational":"Write spontaneously what are your feelings and thoughts about relationships.",
    "ontology":"In a more philosophical way, what do think about what is reality (See Big Traditions for inspiration)?",
    "knowledge":"In a more philosophical way, what is your best way of producing knowledge?",
    "traditions":"Have a moment to think of what psychotherapeutic discourse is more align with you (or you are struggling with).",
    "components":"Write the components you are more drown into and what do you think about them.",
    "simple_words":"Write in simple words, how you work coherently and how to frame it in a theoretical model.",
    "title":"Give a title to this reflection to find it later.",
        }
        widgets = {
    "position":forms.Textarea(attrs={'cols':80}),
    "reality_assumptions":forms.Textarea(attrs={'cols':80}),
    "change":forms.Textarea(attrs={'cols':80}),
    "relational":forms.Textarea(attrs={'cols':80}),
    "ontology":forms.Textarea(attrs={'cols':80}),
    "knowledge":forms.Textarea(attrs={'cols':80}),
    "traditions":forms.Textarea(attrs={'cols':80}),
    "components":forms.Textarea(attrs={'cols':80}),
    "clients":forms.Textarea(attrs={'cols':80}),
    "simple_words":forms.Textarea(attrs={'cols':80}),
                    }

