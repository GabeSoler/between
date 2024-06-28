from django import forms
from .models import PersonalStyle,BigTraditions,Components,EmailSent
from django.forms.widgets import Input

def applyWidget(fields_list:list,widget_name:object):
    """for filling same widget in a group of fields"""
    widget_dic = {}
    for field in fields_list:
        widget_dic[field] = widget_name
    return widget_dic

class RangeBooted(Input):
    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx['widget']['type'] = "range"
        ctx['widget']['attrs']['class'] = "form-range bg-secondary rounded shadow w-75 p-2"
        ctx['widget']['attrs']['min'] = "0"
        ctx['widget']['attrs']['max'] = "100"
        ctx['widget']['attrs']['step'] = "2"
        return ctx
    

class StyleForm(forms.ModelForm):
    class Meta:
        model= PersonalStyle
        fields = ("follower_1","propositive_1","challenger_1",
                  "acceptant_1","intensive_1","extensive_1",
                  "divider_1","containment_1","becoming_1",
                  "development_1","individuation_1","belonging_1")
        widgets = applyWidget(fields,RangeBooted)

        labels = {"follower_1":"Follower: I prefer to keep a following position, by allowing the client to guide as I actively listen.",
                  "propositive_1":"Propositive: I prefer to propose things in the session, offering activities or exercises.",
                  "challenger_1":"Challenger: I prefer to point to things that may be hidden or conflictive.",
                  "acceptant_1":"Acceptant: I prefer to create an space of acceptance of everything that comes from the other.",
                  "intensive_1":"Intensive: I prefer spaces of intensity, where metaphores, and dream-like experiences are the focus.",
                  "extensive_1":"Extensive: I prefer the extensive world, where things can be measured, touched and clearly percived.",
                  "divider_1":"Divider: I prefer to divide conflicts into pieces, analyse and fragment to see more clearly.",
                  "containment_1":"Containment: I prefer to hold complexity and multiplicity to help processes to take the shape they need.",
                  "becoming_1":"Becoming: I prefer to allow life to guide me as I move through new emergent processes.",
                  "development_1":"Development: I prefer to find coherence and organise things into levels of complexity.",
                  "individuation_1":"Individuation: I prefer to follow my own path, do discover things in my own way.",
                  "belonging_1":"Belonging: I prefer to be part of a group or community, to share my talents with others and grow together."
                  }

class ComponentsForm(forms.ModelForm):
    class Meta:
        model= Components
        fields = ("body","feelings","expression","thoughts","narrative",
                 "dreaming","re_prog","subliminal","subparts","spiritual",
                 "relational","systems","setup","transOb","family",
                 "antropology","arts","politics","philosophy","worldview",
                 "individuation","sex_gender","values","belonging","roles",)
        widgets = applyWidget(fields,RangeBooted)
        labels = {
            "body":"Body: Use of body sensations, positions, movements, or embodied trauma.",
            "feelings":"Feelings: Use of feelings, its recognition, descriptions, intensification or reduction..",
            "expression":"Expression: Use of expression, by opening up coherently feelings, tensions, thoughts or movements.",
            "thoughts":"Thoughts: Use of the thinking process, rationale, logics, deduction, induction or abduction.",
            "narrative":"Narrative: Use of narrative, stories, arc, characters.",

            "dreaming":"Dreaming: use of dreaming, or dreaming like experiences, including active imagination, interpretation, and archetypes.",
            "re_prog":"Re-programming: Use of re-programming techniques, like creating new associations, new conditionings, new connections with objects, situations, or people.",
            "subliminal":"Subliminal: Use of subliminal techniques, like hypnosis (concious or unconcious), subliminal stories, or intentional non-verbal comunication.",
            "subparts":"Sub-parts: Use of different parts of the self, in the form of voices, characters or parts of the body.",
            "spiritual":"Spiritual: Use of meditation, altered states of conciousness, alucinogenics, or spiritual healing.",

            "relational":"Relational: Use of the relational space that emerges between people, as unconcious dynamics, emergent properties, attunement or attachment.",
            "systems":"Systems: Use of emergent systems, and their comunicative dynamics, including contexts like family, work, friends, and relatinosihps.",
            "setup":"Set-up: Use of the set-up, the environement, its objects, the system of rewards and punishments created, and a study of practices and routines.",
            "transOb":"Transitional objects: Use of objects/situations embued with affect (unconcious energy), like playing, creativity, cultural experience and popuplar culture referents.",
            "family":"Family: Work with family dynamics of the present and the past, use of internal family systems, constellations, or transference.",

            "antropology":"Antropology: use of the micro cultural spaces, local practices, shared meanings or conflicting assumptions due to cultural difference.",
            "arts":"Arts: Use of arts, its mediums of expression, its different textures and styles, use of materiality and craft.",
            "politics":"Politics: Use of the political space, understanding of power dynamics, of legality and the impacts of goverment policies and institutions.",
            "philosophy":"Philosopy: Use of philosophy, understanding of different paradigms, modes of thiking, reality assumptions, ethical principles and conceptual creation.",
            "worldview":"World View: Use and understanding of world views, including religions, local and macro world constructions, including notions of class, migration, multiculturality.",

            "individuation":"Individuation: Use of the individuaiton process, tendencies of self discovery, inner call for coherence, differentiation and spontaneus development.",
            "sex_gender":"Sex&Gender: work with the tension between sex, gender and comunity, body and cultural identifications, roles in society, power dynamics and discrimination.",
            "values":"Values: Use of value systems, as meaning and motivation, understanding of competing commitments, the place of values in the social sphere.",
            "belonging":"Belonging: Use of the notion of belonging, being part of, being-with. The role of the comunity in development, meaning and identity formation.",
            "roles":"Roles: Use of roles as multiple positions and characters, place in groups and society, identificaiton, or desidentification with the role, creation of coherent roles.",
            }

    

class BigTradForm(forms.ModelForm):
    class Meta:
        model= BigTraditions
        fields = ("hemeneutic","phenomenological","cybernetic","spiritual", "scientific","constructive","participatory")
        labels = {"hemeneutic" : "Hermeneutic: I believe we can understan symbols and hiden patterns of people, texts, and the world by interpeting them, going deeper and deeper in the truth behing the signs and symbols.",
                  "phenomenological" : "Phenomenological: I believe we understand beter by exploring the direct concious experience, the changes of our conciousness, our senses and embodiment to understand and affect the world.",
                  "cybernetic" : "Cybernetic: I believe we can describe operations, functions and processes; we can see how mind, nature and computers share some logical mechanisms we can describe, and use realiably.",
                  "spiritual" : "Spiritual: I believe there are biger forces inside every being that guide their process and we need to create a space for that to emerge more fluently.",
                  "scientific" : "Scientific: I believe we must explore phenomenons in their parts and find reliable knoledge, based in statistics and controlled trials.",
                  "constructive" : "Constructive: I believe reality is constructed, and therefore different for everyone, knolege emerges by studying individuals reports or group patterns.",
                  "participatory" :"Participatory: I believe reality is an unique assemblage between the individual and the world, we can get a more crafted access by developing skill and practice.",   
        }
        widgets = applyWidget(fields,RangeBooted)



class SendEmailForm(forms.ModelForm):
    class Meta:
        model = EmailSent
        fields = ('email',)
        labels = {'emal':'Please press send if you are singed up or write an email if not',}
        
