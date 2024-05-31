from django import forms
from .models import Personal_Style,BigTraditions,Components,EmailSent
from django.forms.widgets import Input

def applyWidget(fields_list:list,widget_name:object):
    """for filling same widget in a group of fields"""
    widget_dic = {}
    for field in fields_list:
        widget_dic[field] = widget_name
    return widget_dic

class RangeBooted(Input):
    def get_context(self, name, value, attrs):
        ctx = super(RangeBooted, self).get_context(name, value, attrs)
        ctx['widget']['type'] = "range"
        ctx['widget']['attrs']['class'] = "form-range bg-secondary rounded shadow w-75 p-2"
        ctx['widget']['attrs']['min'] = "0"
        ctx['widget']['attrs']['max'] = "100"
        ctx['widget']['attrs']['step'] = "2"
        return ctx
    

class StyleForm(forms.ModelForm):
    class Meta:
        model= Personal_Style
        fields = ("follower_1","propositive_1","challenger_1",
                  "acceptant_1","intensive_1","extensive_1",
                  "divider_1","containment_1","becoming_1",
                  "development_1","individuation_1","belonging_1")
        labels = {"follower_1":"I think that people benefit from someone receptive who gives lots of space for them to express their inner world and show little of themselves.",
                  "propositive_1":"I think that people benefit by being offered activities and things to do with what they are feeling or thinking",
                  "challenger_1":"I think that people benefit from someone actively helping them to change what they can.",
                  "acceptant_1":"I think that people benefit by being accepted for who they are, no matter what",
                  "intensive_1":"I think that the world of imagination, ideas and feelings is the most important to consider when helping others",
                  "extensive_1":"I think that the concrete world and being grounded to reality is the most importantn to help someone",
                  "divider_1":"I think that people need help to clarify and be more clear between the different tendencies on their mind.",
                  "containment_1":"I think that people need someone to hold them emotionally and to sustain their complexity without interfering",
                  "becoming_1":"I think that people can become into new subjectivities by engaging with others, nature and objects",
                  "development_1":"I think that people can develop by facing challenges and reaching more abstract perspectives",
                  "individuation_1":"I think that people are fundamentally individuals and need help to find their singularity.",
                  "belonging_1":"I think that people are fundamentally collective and need help to find a group of belonging."
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
            "body":"Use of body techniques for the therapeutic process",
            "feelings":"Use of feelings techniques for the therepeutic process",
            "expression":"Use of expression techniques for the therepeutic process",
            "thoughts":"Use of thoughts thechniques for the therepeutic process",
            "narrative":"Use of narrative techniques for the therepeutic process",

            "dreaming":"Use of narrative techniques for the therepeutic process",
            "re_prog":"Use of reprograming techniques (re-associations and repetitions) for the therapeutic process",
            "subliminal":"Use of subliminal techniques for the therapeutic process",
            "subparts":"Use of sub-parts techniques for the therapeutic process",
            "spiritual":"Use of spiritual techniques for the therapeutic process",

            "relational":"Use of relational techniques for the therapeutic process",
            "systems":"Use of systemic and cybernetic techniques for the therapeutic process",
            "setup":"Use of setup techniques (including reinforcements and punishments) for the therapeutic process",
            "transOb":"Use of transitional objects techniques (objects between fantasy and reality) for the therapeutic process",
            "family":"Use of family dynamics techniques for the therapeutic process",

            "antropology":"Use of antropological knoledge (understanding of culture from the inside of different groups) for the therapeutic process",
            "arts":"Use of arts techniques for the therapeutic process",
            "politics":"Use of knoledge about politics and power dynamics techniques for the therapeutic process",
            "philosophy":"Use of philosophy knoledge (understanding different conceptual ontologies) for the therapeutic process",
            "worldview":"Use of knoledge about different worldviews (including religions) for the therapeutic process",

            "individuation":"Use of the individuation process for the therapeutic process",
            "sex_gender":"Use of understanding of the dynamics of sex and gender for the therapeutic process",
            "values":"Use of understanding of the role of values and value systems for the therapeutic process",
            "belonging":"Use of understanding of belonging and groups pertenence for the therapeutic process",
            "roles":"Use of understanding of roles in groups and society for the therapeutic process",
            }

    

class BigTradForm(forms.ModelForm):
    class Meta:
        model= BigTraditions
        fields = ("hemeneutic","phenomenological","cybernetic","spiritual", "scientific")
        labels = {"hemeneutic" : "I believe we can understan hiden patterns in the words and comunications of others and we understand by inferences.",
                  "phenomenological" : "I believe we understand beter by exploring the direct experience (other's and our own).",
                  "cybernetic" : "I believe we can describe operations and processes, exploring parallels between mind and context.",
                  "spiritual" : "I believe there are biger forces inside every being that guide the process and we need to create a space for that to emerge more fluently.",
                  "scientific" : "I believe we must explore phenomenons in their parts and find reliable knoledge to explain each of the parts."
        }


class SendEmail(forms.ModelForm):
    class Meta:
        model = EmailSent
        fields = ('email',)
        labels = {'emal':'Please press send if you are singed up or write an email if not',}
        
