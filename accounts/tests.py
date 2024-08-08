from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,resolve
# Create your tests here.


class SignupPageTest(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse_lazy('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200) #I did not add template check as it is third party
        self.assertContains(self.response,'Sign Up')    #only checking it works well
        self.assertNotContains(self.response,'Hi there, i should not be here')

    def test_signup_model(self):
        new_user = get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,new_user.username)
        self.assertEqual(get_user_model().objects.all()[0].email,new_user.email)
    
    def test_signup_form(self):
        response = self.client.get(reverse_lazy('account_signup')) #I decided to not test more as it is a third party work
        self.assertContains(response,'Already have an account?')  #I will test this from the functional side instead

    def test_login_form(self):
        response = self.client.get(reverse_lazy('account_login'))
        self.assertContains(response,'If you have not created an account yet')





class SettingsTest(TestCase):
    def setUp(self):
        pass

#testing index with its modules
    def test_settings_index_passwords_view(self):
        pass
    def test_settings_index_profile_view(self):
        pass
    def test_settings_index_status_view(self):
        pass