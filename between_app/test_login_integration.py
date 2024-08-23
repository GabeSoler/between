from django.test import TestCase,Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from .forms import StyleForm
from allauth.account.forms import LoginForm
from django.test.utils import override_settings
from allauth.account import app_settings



class ProfileLinkUserAutenticate(TestCase):
    """to test if the open profile test saves after login and signup """

    fixtures = ['between_app/fixtures/PersonalStyleGroup.yaml',
                'between_app/fixtures/PersonalStyleSection.yaml'
                ]
    def setup(self):
        self.client = Client() #to explore templates in request
    
    @classmethod
    def setUpTestData(cls):
        cls.login_data = {'password':'test123%%HH','remember':'False',
                                'username':'usertest'}
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123%%HH',
        )
        cls.data = {
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

    def test_client_login(self):
        self.client.login(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        self.assertTrue(self.user.is_authenticated)
        self.client.logout()
    
    def test_form_valid(self):
        form_invalid = StyleForm(data={"name": "Computer", "price": 400.1234})
        self.assertFalse(form_invalid.is_valid())
        form_valid = StyleForm(data=self.data)
        self.assertTrue(form_valid.is_valid())
    
    def test_post_form(self):
        response = self.client.post('/profile_test/',self.data, follow=True)
        self.assertEqual(self.client.session['linked'],"false")
        self.assertContains(response,"Compassionate")

    def test_login_form_is_valid(self):
        login_valid = LoginForm(data=self.login_data)
        self.assertTrue(login_valid.is_valid())
    
    def test_login_after_test(self):
        self.client.logout()
        response = self.client.post('/profile_test/',self.data, follow=True)
        self.assertEqual(self.client.session['linked'],"false")        
        response = self.client.post(reverse('account_login'),data=self.login_data)
        #self.assertRedirects(response=response,expected_url='/')
        #self.client.login(username='usertest',password='test123')
        response = self.client.get('')
        #self.assertContains(response,"Welcome back")
        self.assertEqual(self.client.session['linked'],"true")        
        #self.assertContains(response,"Welcome back")
        
