from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Technique,Component
from .forms import TechniqueForm
import uuid

class TestThechniques(TestCase):
    fixtures = [
        'techniques_app/fixtures/components.yaml',
                ]
    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.technique = Technique.objects.create(
            #id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            user = cls.user,
            name = "test",
            component = Component.objects.get(pk=1), #feelings
            text = 'about me',
            notes = 'comments',
        )
    def setup(self):
        self.client = Client() 
        self.client.login(username = 'usertest',
            password = 'test123')    
    
    def test_technique_creation(self):
        technique = Technique.objects.get(pk=self.technique.id)
        self.assertEqual(technique.name,"test")
        self.assertEqual(technique.text,"about me")    

    def test_index_rendering(self): 
        response = self.client.get(reverse('techniques_app:index'), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/index.html')
    
    def test_technique_rendering(self):
        response = self.client.get(f'/techniques/technique/{self.technique.pk}/')
        #response = self.client.get(reverse('techniques_app:technique'),self.technique.pk)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/technique.html')

    def test_long_list_rendering(self):
        response = self.client.get(f'/techniques/techniques_long_community/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/techniques_list_community.html')    
        
    def test_short_list_rendering(self):
        response = self.client.get(f'/techniques/techniques_short_community/1/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/techniques_list_community.html')    
    
    def test_components_rendering(self):
        response = self.client.get(f'/techniques/components_list/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Identity")
        self.assertTemplateUsed(response,'techniques_app/group_list.html')    

    def test_author_list_rendering(self):
        response = self.client.get(f'/techniques/author_list/{self.technique.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/techniques_list_by_user.html')    

    def test_edit_technique_rendering(self):
        self.client.login(username = 'usertest',
            password = 'test123')
        response = self.client.get(f'/techniques/edit_technique/{self.technique.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/edit-technique.html')    

    def test_new_technique_rendering(self):
        self.client.login(username = 'usertest',
            password = 'test123')
        response = self.client.get(f'/techniques/new_technique/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/new_technique.html')    

    def test_save_technique_redirect(self):
        self.client.login(username = 'usertest',
            password = 'test123')
        response = self.client.post(f'/techniques/save_technique/{self.technique.pk}/')
        self.assertRedirects(response,reverse('techniques_app:saved_techniques'))
    
    def test_author_list_integration(self):
        self.client.login(username = 'usertest',
            password = 'test123')
        response = self.client.post('accounts/edit_profile/',data={'name':'test','about':'about me'})
        response = self.client.get(f'/techniques/author_list/{self.technique.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"test")
        self.assertTemplateUsed(response,'techniques_app/techniques_list_by_user.html')    
