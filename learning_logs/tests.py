from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Topic,Entry,AfterJournal


class TestTopic(TestCase):

    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.topic = Topic.objects.create(
            id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            owner = cls.user,
            text = 'I am a Topic',
        )
        cls.entry = Entry.objects.create(
            #id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            topic = cls.topic,
            text = "an entry",
        )
    def setup(self):
        self.client.login(username = 'usertest',
            password = 'test123')    

    def test_topic_entry_creation(self):
        topic = Topic.objects.get(pk=self.topic.id)
        entry = Entry.objects.get(pk=self.entry.id)
        self.assertEqual(topic.text,'I am a Topic')    
        self.assertEqual(entry.text,"an entry")    

    def test_index_rendering(self): 
        response = self.client.get(reverse('learning_logs:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Journal Space")
        self.assertTemplateUsed(response,'learning_logs/index.html')

    def test_topic_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/topic/{self.topic.id}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Topic:")
        self.assertTemplateUsed(response,'learning_logs/topic/topic.html')
  
    def test_topics_rendering(self):
        self.setup()
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Topics:")
        self.assertTemplateUsed(response,'learning_logs/topic/topics.html')

    def test_new_topic_rendering(self): 
        response = self.client.get(reverse('learning_logs:new_topic'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Add here a new Topic")
        self.assertTemplateUsed(response,'learning_logs/topic/new_topic.html')
   
    def test_new_entry_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/new_entry/{self.topic.id}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Add New Entry")
        self.assertTemplateUsed(response,'learning_logs/topic/new_entry.html')

    def test_edit_entry_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/edit_entry/{self.entry.id}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Edit Entry")
        self.assertTemplateUsed(response,'learning_logs/topic/edit_entry.html')


class TestAfterJournal(TestCase):

    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.after_journal = AfterJournal.objects.create(
            #id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            owner = cls.user,
            question = "how are you",
            text = "I am a text",
        )
    def setup(self):
        self.client = Client() 
        self.client.login(username = 'usertest',
            password = 'test123')    

    def test_topic_entry_creation(self):
        topic = AfterJournal.objects.get(pk=self.after_journal.id)
        self.assertEqual(topic.text,"I am a text")    

    def test_question_item_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/after_answer/{self.after_journal.id}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.after_journal.question)
        self.assertTemplateUsed(response,'learning_logs/question/question_item.html')
  
    def test_after_answer_date_rendering(self):
        self.setup()
        response = self.client.get(reverse('learning_logs:after_answer_date'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"After Session Questions List")
        self.assertTemplateUsed(response,'learning_logs/question/after_by_date.html')

    def test_after_answer_question_rendering(self):
        self.setup()
        response = self.client.get(reverse('learning_logs:after_answer_question'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"After Session Questions List-By question")
        self.assertTemplateUsed(response,'learning_logs/question/after_by_question.html')
   
    def test_new_question_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/new_question/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Create an After Session Entry:")
        self.assertTemplateUsed(response,'learning_logs/question/create_Question.html')

    def test_edit_entry_rendering(self):
        self.setup()
        response = self.client.get(f'/learning/edit_question/{self.after_journal.id}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Edit Entry")
        self.assertTemplateUsed(response,'learning_logs/question/edit_Question.html')

