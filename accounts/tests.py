from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,reverse
from .forms import CommunityProfileForm,UserStatusForm,DeleteAccountForm

from allauth.account.models import EmailAddress

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
    username = "newuser"
    email = "newuser@email.com"
    password = "312%%HWH"
    data_profile = {"name":"Hey","about":"hey hey"}
    data_status = {"therapist":True,"diver":True}
    def setUp(self):
        self.user = get_user_model().objects.create_user(self.username,self.email,self.password)

#testing index with its modules
    def test_settings_index_passwords_view(self):
        pass
    def test_settings_index_profile_view(self):
        self.client.login(username=self.username,email=self.email,password=self.password)
        response = self.client.get('')
        self.assertContains(response,"newuser")

    def test_form_community_profile(self):
        form_valid = CommunityProfileForm(data=self.data_profile)
        self.assertTrue(form_valid.is_valid())

    def test_form_status_profile(self):
        form_valid = UserStatusForm(data=self.data_status)
        self.assertTrue(form_valid.is_valid())

    def test_settings_edit_profile(self):
        self.client.login(username=self.username,email=self.email,password=self.password)
        response = self.client.get(reverse('accounts:account_profile'))
        self.assertContains(response,"name")
        response = self.client.post(reverse('accounts:edit_profile'),self.data_profile, follow=True)
        self.assertRedirects(response,reverse('accounts:account_profile'),302)
        response = self.client.get(reverse('accounts:account_profile'))
        self.assertNotContains(response,"newuser")
        self.assertContains(response,"Hey")
    
    def test_settings_index_status_view(self):
        self.client.login(username=self.username,email=self.email,password=self.password)
        response = self.client.get(reverse('accounts:account_profile'))
        self.assertContains(response,"Normal")
        self.assertContains(response,"Other")
        response = self.client.post(reverse('accounts:edit_status'),self.data_status, follow=True)
        self.assertRedirects(response,reverse('accounts:account_profile'))
        response = self.client.get(reverse('accounts:account_profile'))
        self.assertContains(response,"Therapist")
        self.assertContains(response,"Diver")


class DeleteAccount(TestCase):
    username = "newuser"
    email = "newuser@email.com"
    password = "312%%HWH"
    data_profile = {"name":"Hey","about":"hey hey"}
    data_status = {"therapist":True,"diver":True}
    delete_data = {'reason':"no_inter",'confirm':True}
    def setUp(self):
        self.user = get_user_model().objects.create_user(self.username,self.email,self.password)



    def test_form_valid(self):
        form_invalid = DeleteAccountForm(data={'reason':'pepito','confirm':'hola'})
        self.assertFalse(form_invalid.is_valid())
        form_valid = DeleteAccountForm(data=self.delete_data)
        self.assertTrue(form_valid.is_valid())

    def test_account_deleted(self):
        self.assertIsNotNone(get_user_model().objects.get(username=self.user.username))
        self.client.login(username=self.username,email=self.email,password=self.password)
        self.assertTrue(self.user.is_authenticated)
        response = self.client.get('/')
        self.assertContains(response,self.user.username)
        response = self.client.get(reverse('accounts:delete_account'))
        self.assertEqual(response.status_code,200)
        response = self.client.post(
            reverse('accounts:delete_account'),self.delete_data,follow=False
        )
        self.assertRedirects(response,'/',302)
        response = self.client.get('/')
        self.assertNotContains(response,self.user.username)

        






    
