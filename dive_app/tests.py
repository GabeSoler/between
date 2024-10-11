from django.test import TestCase
from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Creation,Shadow


class TestCreation(TestCase):

    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.creation = Creation.objects.create(
            #id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            owner = cls.user,
            title = "a title",
            goal = "a goal",
            text_sensation = "content",
            text_conection = "content",
            text_metaphore = "content",
            text_concepts = "content",
            text_craft = "content",
        )
    def setup(self):
        self.client = Client() 
        self.client.login(username = 'usertest',
            password = 'test123')    


    def test_topic_entry_creation(self):
        topic = Creation.objects.get(pk=self.creation.id)
        self.assertEqual(topic.title,"a title")    

    def test_creation_item_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/creation/{self.creation.id}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.creation.title)
        self.assertTemplateUsed(response,'learning_logs/creating/creation_item.html')
  
    def test_creations_by_date_date_rendering(self):
        self.setup()
        response = self.client.get(reverse('learning_logs:creations_by_date'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.creation.title)
        self.assertTemplateUsed(response,'learning_logs/creating/creation_by_date.html')

    def test_creations_by_title_rendering(self):
        self.setup()
        response = self.client.get(reverse('learning_logs:creations_by_title'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.creation.title.title())
        self.assertTemplateUsed(response,'learning_logs/creating/creation_by_title.html')
   
    def test_new_creation_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/new_creation/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"A guided creative reflection:")
        self.assertTemplateUsed(response,'learning_logs/creating/create_reflection.html')

    def test_edit_entry_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/edit_creation/{self.creation.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Edit Creation")
        self.assertTemplateUsed(response,'learning_logs/creating/edit_creation.html')



class TestShadow(TestCase):

    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.shadow = Shadow.objects.create(
            #id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            owner = cls.user,
            title = "some content",
            goal = "some content",
            text_opossite_style = "some content",
            text_opposite_sex = "some content",
            text_oppossite_elements = "some content",
            #wounded healer
            text_transf_characters = "some content",
            text_furor_curandis = "some content",
            text_trauma_history = "some content",
            text_trauma_triggers = "some content",
            #plan
            text_care_plan = "some content",
        )
    def setup(self):
        self.client = Client() 
        self.client.login(username = 'usertest',
            password = 'test123')    