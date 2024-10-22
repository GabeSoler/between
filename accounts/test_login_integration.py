from django.test import TestCase,Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from between_app.forms import StyleForm
from django.conf import settings
from asgiref.sync import sync_to_async

from django.test.utils import override_settings
from allauth.account import app_settings
from allauth.account.models import EmailAddress
from allauth.account import app_settings


@override_settings(
    ACCOUNT_DEFAULT_HTTP_PROTOCOL="https",
    ACCOUNT_EMAIL_VERIFICATION=app_settings.EmailVerificationMethod.MANDATORY,
    ACCOUNT_AUTHENTICATION_METHOD=app_settings.AuthenticationMethod.USERNAME,
    ACCOUNT_SIGNUP_FORM_CLASS=None,
    ACCOUNT_EMAIL_SUBJECT_PREFIX=None,
    LOGIN_REDIRECT_URL="/accounts/profile/",
    ACCOUNT_SIGNUP_REDIRECT_URL="/accounts/welcome/",
    ACCOUNT_ADAPTER="allauth.account.adapter.DefaultAccountAdapter",
    ACCOUNT_USERNAME_REQUIRED=True,
)
class ProfileLinkUserAutenticate(TestCase):
    """to test if the open profile test saves after login and signup """

    fixtures = ['between_app/fixtures/PersonalStyleGroup.yaml',
                'between_app/fixtures/PersonalStyleSection.yaml'
                ]
    def setup(self):
        self.client = Client() #to explore templates in request
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username="@usertest")
        cls.user.set_password("test123%%HH")
        cls.user.save()
        EmailAddress.objects.create(
            user=cls.user,
            email="test@test.com",
            primary=True,
            verified=True,
        )
        cls.login_data = {"login":"@usertest","password":"test123%%HH"}


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
        response = self.client.post('/tests/profile_test/',self.data, follow=True)
        self.assertEqual(self.client.session['linked'],"false")
        self.assertContains(response,"Compassionate")

    
    def test_login_after_test(self):
        self.client.logout()
        response = self.client.post('/tests/profile_test/',self.data, follow=True)
        self.assertEqual(self.client.session['linked'],"false")
        response = self.client.post(
                reverse("account_login"),
                self.login_data,
                )
        #self.assertEqual(len(callbacks), 1)
        self.assertRedirects(
            response, settings.LOGIN_REDIRECT_URL, fetch_redirect_response=False
            )
        response = self.client.get('')
        self.assertNotEqual(self.client.session['linked'],"error")
        self.assertEqual(self.client.session['linked'],"true")        
        
    def test_login_before_test(self):
        self.client.logout()
        response = self.client.post(
                reverse("account_login"),
                self.login_data,
                )
        #self.assertEqual(len(callbacks), 1)
        self.assertRedirects(
            response, settings.LOGIN_REDIRECT_URL, fetch_redirect_response=False
            )
        response = self.client.post('/tests/profile_test/',self.data, follow=True)
        self.assertEqual(self.client.session['linked'],"true")
        self.assertNotEqual(self.client.session['linked'],"error")
        
