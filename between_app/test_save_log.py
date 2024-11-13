from django.test import TestCase,Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from between_app.forms import StyleForm
from django.conf import settings
from asgiref.sync import sync_to_async

from allauth.account.models import EmailAddress


class ProfileLinkUserAutenticate(TestCase):
    """to test if the open profile test saves after login and signup """

    fixtures = ['between_app/fixtures/PersonalStyleGroup.yaml',
                'between_app/fixtures/PersonalStyleSection.yaml'
                ]
    
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

    def next_link(self,next,reverse_tag):
        login_in_address = reverse(reverse_tag)
        next_link = f"{login_in_address}?next={next}"
        return next_link

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
        self.assertContains(response,"Compassionate")

    
    def test_login_after_test(self):
        self.client.logout()
        response = self.client.post('/tests/profile_test/',self.data, follow=True)
        next = response.request['PATH_INFO']
        response = self.client.post(
                self.next_link(next,"account_login"),
                self.login_data,follow=True
                )
        self.assertRedirects(
            response,next, fetch_redirect_response=False
            )
        response = self.client.get(reverse('between_app:profiles_list'))
        self.assertContains(response,"@usertest's Therapist Profile")

    def test_login_before_test(self):
        self.client.logout()
        response = self.client.post(
                reverse("account_login"),
                self.login_data,
                )
        self.assertRedirects(
            response,'/', fetch_redirect_response=False
            )
        response = self.client.post('/tests/profile_test/',self.data,follow=True)
        response = self.client.get(reverse('between_app:profiles_list'))
        self.assertContains(response,"@usertest's Therapist Profile")
 
