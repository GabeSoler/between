from threading import Thread
from django.core.mail import send_mail


class ResultsEmailThread(Thread):
    """creates an email as async thread for test results"""
    def __init__(self, text_content:str, recipient_list:str,*args,**kwargs):
        super().__init__(*args, **kwargs)    
        self.recipient_list = recipient_list        
        self.text_content = text_content
    
    def run (self):
        for i in range(0,3):
            try:
                msg = send_mail(
                "Your CreaTherapy Profile",
                self.text_content,
                "creatherapy.app@gmail.com",
                [self.recipient_list],
                fail_silently=False,
                    )
                if msg == False:
                    continue
                else:
                    break
            except Exception as e:
                print(e)

def compose_results(cont_position, cont_path, cont_tradition):
        """compose a text to display in a email"""
        text = "Your test results:\n\n" 
        text += "Position: {0}\n\t Description: {1}\n\n".format(cont_position.group.title(),cont_position.description)
        text += "Path: {0}\n\t Description: {1}\n\n ".format(cont_path.group.title(),cont_path.description,)
        text +=  "Tradition: {0}\n\t Description: {1}\n\n".format(cont_tradition.group.title(),cont_tradition.description)
        text += "Best wishes\n Gabriel Soler"
        return text
