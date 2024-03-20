"""Where i write the information to run the app's dynamic content"""


class Content():
    position = {
        "compassionate" : {
        "description" : "The Compassionate position make us feel close to other's feelings and suffering, giving lots of space to express other people's feelings. In this position we follow the rhytm of the other person avoiging interruptions",
        "shadow" : "When we polarise into it we may have difficulties with setting boundaries, which means that we tend to put others before ourselves.",
        "traditions" : "Person Centred, Focusing, Relational Psychoanalisis.",
        "authors" : 'Rogers, Jung, Stolorow, Orange'
        },
        "playful" : {
        "description" : "The Playful position invite us to create activities that can mobilise ours and the others emotions, so we can process them.",
        "shadow" : "When we polarise into it we may have problems with enactments, risking our unconcious to engangle and bring forth primitive dynamics.",
        "traditions" : "Gestalt, Psychodrama, Play Therapy, Art therapies.",
        "authors" : "Perls, Moreno, Winnicott"
        },
        "inquisitive" : {
        "description" : "The Inquisitive position invite us to analyse and collect information to find clues of deeper conflicts and underlying dynamics.",
        "shadow" : "When we polarise into it we may find ourselves over-thinking and detached from the present emotional dynamic.",
        "traditions" : "Traditional Psychoanalysis, Lacanian psychoanalysis, Jungian analysis.",
        "authors" : "Freud, Klein, Bion, Kernberg"    
    },
        "changer" : {
        "description" : "The Changer position invite us to encurage change in our clients by directly finding solutions, new behaviours, or exercises.",
        "shadow" : "When we polarise into it we may become controlling, not giving enough space for the other to express their deeper feelings.",
        "traditions" : "Cognitive Behavioural, Integrative approaches",
        "authors" : "Beck, Elis"    
    }
    }

    path = {
        "dreamer" : {
        "description" : "The Dreamer path is an invitation towards the magic of poetry, metaphor, art, and daydreaming. This path feels deeply and believes dream brings deeper truths.",
        "shadow" : "When we polarise into it we may find ourselves forgeting the concrete world over fantasy.",
        "traditions" : "Jungian analysis, Psychoanalysis.",
        "authors" : "Jung"
    },
        "sage"  : {
        "description" : "The Sage path invite us to analyse things in their components and to create more encompasing models that help us clarify our minds and the big problems of existence.",
        "shadow" : "When we polarise into it we may become obsessed with concepts and with the need to categorise every inch of human experience, clauding our mind to the beauty of life.",
        "traditions" : "Integral approach, Integrative approaches.",
        "authors" : "Wilber, Kegan"
    },
        "carer" : {
        "description" : "The Carer path is an invitation towards closeness to otherness, by an appreciation of life and the movements of nature.",
        "shadow" : "When we polarise into it we may become too close to care for others forgeting to care for ouselves, we become submisive.",
        "traditions" : "Person Centred, Focusing, Relational Psychoanalisis.",
        "authors" : "Rogers, Orange"
    },
        "explorer" : {
        "description" : "The Explorer path is an invitation to keep our curiosity for novelty, for new tecniques and solutions, and to not stop looking for something better.",
        "shadow" : "When we polarise into it we may become extremely passionate of our serch and we may lose the natural balance, risking manic defenses.",
        "traditions" : "Evidence Based, Cognitive Behavioural",
        "authors" : "Skinner, Beck, Elis,Rogers, Wilber, Opazo"  
    }
    }

    tradition = {
        "artist" : {
        "description" : "The Artist has a self deepening approach, focussing more in their own feelings and experiences, aiming to explore the deepths of the soul.",
        "shadow" : "When we polarise into it we may have difficulties with stopping our delightful practices, risking addiction and fixation.",
        "traditions" : "Jungian analysis, Psychoanalysis(Bion, Klain, Winnicott), Psychodelic treatements, holotropic breathing.",
        "authors" : "Jung, Winnicott, Perls"
        },

        "warrior" : {
        "description" : "The Warrior has a self development approach, aiming to help by becoming stronger, achieving higher concepts and techniques.",
        "shadow" : "When we polarise into it we risk to develop a tunel vision towards our fight and projects, not able to see around anymore.",
        "traditions" : "Cognitive Behavioural, Gestalt",
        "authors" : "Beck, Ellis, Perls, Wilber"
    },
        "lider" : {
        "description" : "The Lider has a group approach where they want to find an inspiration that may take them and others to a better place.",
        "shadow" : "When we polarise into it we may become too embedded in our group ideals and develop a cult like behaviour, rejecting external opinions.",
        "traditions" : "Confesional therapies",
        "authors" : "Freud when making seven rings"
        },
        "coach" : {
        "description" : "The Coach position works with a team, and aims for its perfecting by following clear techniques and strategies.",
        "shadow" : "When we polarise into it we may create a relatiionship where one dominates over the rest because they may 'know more'.",
        "traditions" : "Cognitive Behavioural.",
        "authors" : "Beck, Ellis, Opazo, Wilber" 
    }
    }


"""
Function to add content to the migration's 'run_python'. 
first create a custom migration, then pass the function. I do not know why it failed before, it created it but logged error.

def create_content():
    try: 
        ContentGroup = apps.get_model('between_app', 'ContentGroup')
        ContentProperties = apps.get_model('between_app', 'ContentProperties')
        Personal_Style = apps.get_model('between_app', 'Personal_Style')
    except: LookupError

    Position = ContentGroup.objects.create(name='position',section=Personal_Style)
    Path = ContentGroup.objects.create(name='path',section=Personal_Style)
    Tradition = ContentGroup.objects.create(name='tradition',section=Personal_Style)

    add = {Position:Content.position,
         Path:Content.path,
         Tradition:Content.tradition}
    for a, i in add.values:
       ContentProperties.objects.create(
            group = a,
            name = i['name'],
            description = i['description'],
            shadow = i['shadow'],
            traditions = i['traditions'],
            authors = i['authors'],
            )






"""