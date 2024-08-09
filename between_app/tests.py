from django.test import TestCase,RequestFactory,Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from .models import PersonalStyle,Components,BigTraditions
from django.utils import timezone
from .forms import StyleForm,ComponentsForm, BigTradForm
from .views import take_components,test_home
# Create your tests here.

class PersonalStyleTests(TestCase):
    fixtures = ['between_app/fixtures/PersonalStyleGroup.yaml',
                'between_app/fixtures/PersonalStyleSection.yaml'
                ]
    def setup(self):
        self.client = Client() #to explore templates in request
    
    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.profile = PersonalStyle.objects.create(
                user = cls.user,
                follower_1 = 10,
                propositive_1 = 2,
                challenger_1 = 6,
                acceptant_1 = 10,
                intensive_1 = 50,
                extensive_1 = 6,
                divider_1 = 3,
                containment_1 = 1,
                becoming_1 = 1,
                development_1 = 6,
                individuation_1 = 10,
                belonging_1 = 3,
                ) 


    def test_Profile_creation(self):
        t = timezone.now()
        t = t.strftime('%Y-%m-%d')
        self.assertEqual(f"{self.profile.follower_1}",'10')
        self.assertEqual(f"{self.profile.containment_1}",'1')
        self.assertEqual(f"{self.profile.created_at.date()}",t)

    def test_test_home_view(self):
        response = self.client.get(reverse('between_app:test_home'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Therapist Style")
        self.assertTemplateUsed(response, 'between_app/test-home.html')


    def test_position_list_view(self):
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123',)
        response = self.client.get(reverse('between_app:profiles_list'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Explore your detailed scores')
        self.assertTemplateUsed(response,'between_app/personal_style/positions_list.html')
    

    def test_take_profile_test(self):
        response = self.client.get(reverse('between_app:profile_test'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Profile Test")
        self.assertTemplateUsed(response, 'between_app/personal_style/profile_test.html')
    
    
    def test_style_detail_view(self):
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123',)
        response = self.client.get(self.profile.get_absolute_url())
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Therapist Style: Scores")
        self.assertTemplateUsed(response, 'between_app/personal_style/style_detail.html')

    def test_ps_results_view(self):
        self.client.login(username = 'usertest',
        email = 'test@test.com',
        password = 'test123',)
        response = self.client.get(f'/results/{self.profile.pk}/', follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Compassionate")
        self.assertTemplateUsed(response, 'between_app/personal_style/results_email.html')

    def test_content_view(self):
        response = self.client.get(reverse('between_app:content'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "categories explained")
        self.assertTemplateUsed(response, 'between_app/personal_style/content.html')

    def test_form_profiles(self):
        data = {
                'follower_1':90,
                'propositive_1':2,
                'challenger_1':6,
                'acceptant_1':10,
                'intensive_1':20,
                'extensive_1':6,
                'divider_1':3,
                'containment_1':30,
                'becoming_1':1,
                'development_1':60,
                'individuation_1':10,
                'belonging_1':3,

        }
        form_invalid = StyleForm(data={"name": "Computer", "price": 400.1234})
        self.assertFalse(form_invalid.is_valid())
        form_valid = StyleForm(data=data)
        self.assertTrue(form_valid.is_valid())
        response = self.client.post('/profile_test/',data, follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Compassionate")
        response = self.client.post(reverse_lazy('account_signup', 
                                 {'username':'testuser','password':'123%%gabe'} ))#testing saving of test
        self.assertContains(response,"Wellcome back!")
        

   

class ComponentsTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )

        cls.profile = Components.objects.create(
                user = cls.user,
                body = 30,
                feelings = 40,
                expression = 1,
                thoughts = 1,
                narrative = 60,
                #extended awareness
                dreaming = 1,
                re_prog = 1,
                subliminal = 70,
                subparts = 1,
                spiritual = 1,
                #Context work
                relational = 1,
                systems = 90,
                setup = 1,
                transOb = 1,
                family = 1,
                #Culture
                antropology = 65,
                arts = 1,
                politics = 1,
                philosophy = 99,
                worldview = 1,
                #identity
                individuation = 1,
                sex_gender = 1,
                values = 1,
                belonging = 30,
                roles = 1,
                )
    def setup(self):
        self.client = Client()

    def test_components_creation(self):
        component = Components.objects.get(pk=self.profile.pk)
        self.assertEqual(component.politics,1)
        self.assertEqual(component.philosophy,99)
    
    def test_component_user(self):
        component = Components.objects.get(pk=self.profile.pk)
        self.assertEqual(component.user, self.profile.user)

    def test_home_view(self):
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123')        
        response = self.client.get(reverse('between_app:test_home'), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"narrative")
        self.assertTemplateUsed(response,'between_app/test-home.html')

    def test_components_list_view(self):
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123')
        response = self.client.get(reverse('between_app:components_list'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Your Components tests")
        self.assertTemplateUsed(response, 'between_app/Components/components_list.html')
    
    def test_components_detail_view(self):
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123')
        response = self.client.get(f"/components_detail/{self.profile.pk}/")
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Components test")
        self.assertTemplateUsed(response, 'between_app/Components/components_detail.html')

    def test_take_components_view(self):
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123')
        response = self.client.get(reverse('between_app:components_test'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Use of body sensations")#taken from
        self.assertTemplateUsed(response, 'between_app/Components/components_test.html')
    
    def test_form_components(self):
        data = {
                'body':30,
                'feelings':40,
                'expression':1,
                'thoughts':1,
                'narrative':60,
                #extended awareness
                'dreaming':1,
                're_prog':1,
                'subliminal':70,
                'subparts':1,
                'spiritual':1,
                #Context work
                'relational':1,
                'systems':90,
                'setup':1,
                'transOb':1,
                'family':1,
                #Culture
                'antropology':65,
                'arts':1,
                'politics':1,
                'philosophy':2,
                'worldview':1,
                #identity
                'individuation':1,
                'sex_gender':1,
                'values':1,
                'belonging':30,
                'roles':1,
        }
        self.client.login(username = 'usertest',
            email = 'test@test.com',
            password = 'test123')
        form_invalid = ComponentsForm(data={"name": "Computer", "price": 400.1234})
        self.assertFalse(form_invalid.is_valid())
        form_valid = ComponentsForm(data=data)
        self.assertTrue(form_valid.is_valid())
        response = self.client.post('/components_test/',data, follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"philosophy-2%")
        
    
class BigTraditionsTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )

        cls.profile = BigTraditions.objects.create(
                user = cls.user,
                hemeneutic = 20,
                phenomenological = 80,
                cybernetic = 60,
                spiritual = 70,
                scientific = 50,
                constructive = 30,
                participatory = 90,
                            )


    def test_big_traditions_creation(self):
        big_trad = BigTraditions.objects.get(pk=self.profile.pk)
        self.assertEqual(big_trad.hemeneutic,20)
        self.assertEqual(big_trad.cybernetic,60)

    """
    def test_home_view(self):
        response = self.client.get(reverse('between_app:test_home'), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"hemeneutic-20%")
        self.assertTemplateUsed(response,'between_app/test-home.html')

    def test_big_trad_list_view(self):
        response = self.client.get(reverse('between_app:traditions_list'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Your Traditions Tests")
        self.assertTemplateUsed(response, 'between_app/BigTraditions/traditions_list.html')

    def test_big_trad_detail_view(self):
        response = self.client.get(reverse('between_app:traditions_detail',self.profile.id), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Big Traditions")
        self.assertTemplateUsed(response, 'between_app/BigTraditions/traditions_detail.html')

    def test_take_big_traditions_view(self):
        response = self.client.get(reverse('between_app:traditions_test'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Traditions Test")
        self.assertTemplateUsed(response, 'between_app/BigTraditions/traditions_test.html')

    def test_form_big_traditions(self):
        data = {
                'hemeneutic':20,
                'phenomenological':80,
                'cybernetic':60,
                'spiritual':70,
                'scientific':50,
                'constructive':30,
                'participatory':90,
        }
        form_invalid = BigTradForm(data={"name": "Computer", "price": 400.1234})
        self.assertFalse(form_invalid.is_valid())
        form_valid = BigTradForm(data=data)
        self.assertTrue(form_valid.is_valid())
        response = self.client.post('/traditions_test/',data, follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"cybernetic-60%")

        """