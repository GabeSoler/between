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
        response = self.client.get(reverse_lazy('account_signup'))
        self.assertContains(response,'Already have an account?')
        response = self.client.post(reverse_lazy('account_signup'),{
            'username':'test_user',
            'password1':'128763HiTesting%',
            'password2':'128763HiTesting%',
            'email':'test@test.test',
        },follow=True)
        self.assertEqual(response.status_code,200)
        self.assertNotContains(response,'A user with that username already exists.')
        self.assertNotContains(response,'A user is already registered with this email address.')
        self.assertNotContains(response,'You must type the same password each time.')
        self.assertNotContains(response,'This password is too common')
        self.assertNotContains(response,'Already have an account?')
        self.assertContains(response,'test_user')
    
    def test_login_form(self):

        response = self.client.post(reverse_lazy('account_signup'),{
            'username':'test_user',
            'password1':'128763HiTesting%',
            'password2':'128763HiTesting%',
            'email':'test@test.test',
        },follow=True)
        self.client.logout()
        response = self.client.get(reverse_lazy('account_login'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'If you have not created an account')
        response = self.client.post(reverse_lazy('account_login'),{
            'id_login':'test_user',
            'password':'128763HiTesting%',
            },follow=True)
        self.assertEqual(response.status_code,200)
        self.assertNotContains(response,'The username and/or password you specified are not correct.')
        self.assertNotContains(response,'If you have not created an account')
        self.assertContains(response,self.username)





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