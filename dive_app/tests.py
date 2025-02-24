from django.test import TestCase
from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Creation,Shadow,AssembleModel
from accounts.models import UserStatus

#todo Test and review Shadow

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
        cls.user_status = UserStatus.objects.create(
            user=cls.user,
            therapist=False,
            diver=False,
        )
        cls.user_status_data = {'therapist':True,'diver':True}

        cls.creation_data = {
            "title":"posting data",
            "goal":"post data",
            "text_sensation":"content",
            "text_conection":"content",
            "text_metaphore":"content",
            "text_concepts":"content",
            "text_craft":"content",
            }

    def post_diver(self,response,follow=True):
        response = self.client.post(reverse('accounts:edit_status'),self.user_status_data, follow=follow)
        return response
    
    def setup(self,add_perm=True):
        self.client.login(username = 'usertest',
            password = 'test123')
        if add_perm:
            self.client.post(reverse('accounts:edit_status'),self.user_status_data,follow=True)


    def rendering_checks(self,url:str,contains:str,template:str):
        """checks for correct status of url, containing a string and correct templated used"""
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,contains)
        self.assertTemplateUsed(response,template)


    def test_creation_object_creation(self):
        topic = Creation.objects.get(pk=self.creation.id)
        self.assertEqual(topic.title,"a title")    

    def test_creation_item_renderig(self): # Now I check for three things with one function
        self.setup()
        response = f'/diver/creation/{self.creation.id}/'
        contains = self.creation.title
        template = 'dive_app/creating/creation_item.html'
        self.rendering_checks(response,contains,template)
  
    def test_creation_item_permissions(self): #checks for redirects for permissions
        response = self.client.get(f'/diver/creation/{self.creation.id}/')
        self.assertRedirects(response,f'/accounts/login/?next=/diver/creation/{self.creation.pk}/',302) #needs to be sign in
        self.setup(add_perm=False)
        response = self.client.get(f'/diver/creation/{self.creation.id}/')
        self.assertRedirects(response,f'/accounts/edit_status/?next=/diver/creation/{self.creation.pk}/',302) #needs to have permissions
  
    def test_creation_item_next(self): # Tests the next brings you back to a post
        self.setup(add_perm=False)
        response = self.client.post(f'/accounts/edit_status/?next=/diver/creation/{self.creation.pk}/',
                    self.user_status_data)
        self.assertRedirects(response,f'/diver/creation/{self.creation.pk}/',302) #needs to have permissions
  
    def test_creations_by_date_date_rendering(self):
        self.setup()
        response = reverse('dive_app:creations_by_date')
        contains = self.creation.title
        template = 'dive_app/creating/creation_by_date.html'
        self.rendering_checks(response,contains,template)

    def test_creations_by_title_rendering(self):
        self.setup()
        response = reverse('dive_app:creations_by_title')
        contains = self.creation.title.title()
        template = 'dive_app/creating/creation_by_title.html'
        self.rendering_checks(response,contains,template)
   
    def test_new_creation_rendering(self):
        self.setup()
        response = self.client.get('/diver/new_creation/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"A guided creative reflection:")
        self.assertTemplateUsed(response,'dive_app/creating/create_reflection.html')

    def test_edit_creation_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/edit_creation/{self.creation.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Edit Creation")
        self.assertTemplateUsed(response,'dive_app/creating/edit_creation.html')

    def test_new_creation_post(self):
        self.setup()
        response = self.client.post('/diver/new_creation/',self.creation_data)
        self.assertRedirects(response,
                reverse('dive_app:index'),302)
        
    def test_edit_creation_post(self):
        self.setup()
        response = self.client.post(f'/diver/edit_creation/{self.creation.pk}/',self.creation_data)
        self.assertRedirects(response,
                f'/diver/creation/{self.creation.pk}/',302)
        
 

#* Testing Shadow

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
        cls.user_status = UserStatus.objects.create(
            user=cls.user,
            therapist=False,
            diver=False,
        )

        cls.user_status_data = {'therapist':True,'diver':True}

        cls.shadow_data = {
            "title":"some content",
            "goal":"some content",
            "text_opossite_style":"some content",
            "text_opposite_sex":"some content",
            "text_oppossite_elements":"some content",
            #wounded healer
            "text_transf_characters":"some content",
            "text_furor_curandis":"some content",
            "text_trauma_history":"some content",
            "text_trauma_triggers":"some content",
            #plan
            "text_care_plan":"some content",

        }

    def setup(self,add_perm=True):
        self.client.login(username = 'usertest',
            password = 'test123')
        if add_perm:
            self.client.post(reverse('accounts:edit_status'),self.user_status_data,follow=True)


    def test_shadows_by_date_rendering(self):
        self.setup()
        response = self.client.get(reverse('dive_app:shadows_by_date'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.shadow.title.title())
        self.assertTemplateUsed(response,'dive_app/shadow/shadow_by_date.html') 

    def test_shadows_by_title_rendering(self):
        self.setup()
        response = self.client.get(reverse('dive_app:shadows_by_title'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.shadow.title.title())
        self.assertTemplateUsed(response,'dive_app/shadow/shadow_by_title.html')


    def test_shadow_item_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/shadow/{self.shadow.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.shadow.title)
        self.assertTemplateUsed(response,'dive_app/shadow/shadow_item.html')


    def test_new_shadow_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/new_shadow/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Shadow Reflections")
        self.assertTemplateUsed(response,'dive_app/shadow/new_shadow.html')


    def test_edit_shadow_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/edit_shadow/{self.shadow.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Edit Shadow")
        self.assertTemplateUsed(response,'dive_app/shadow/edit_shadow.html')

    def test_new_shadow_post(self):
        self.setup()
        response = self.client.post('/diver/new_shadow/',self.shadow_data)
        self.assertRedirects(response,
                reverse('dive_app:index'),302)
        
    def test_edit_shadow_post(self):
        self.setup()
        response = self.client.post(f'/diver/edit_shadow/{self.shadow.pk}/',self.shadow_data)
        self.assertRedirects(response,
                f'/diver/shadow/{self.shadow.pk}/',302)


#* Testing Assemble a model

class TestAssembleModel(TestCase):

    @classmethod
    def setUpTestData(cls):    
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )
        cls.assemble = AssembleModel.objects.create(
            #id = "74dc3d3f-5cd6-4660-9709-763a95a9ab3a",
            owner = cls.user,
            title = "some content",
            position = "some content",
            reality_assumptions = "some content",
            change = "some content",
            relational = "some content",
            ontology = "some content",
            knowledge = "some content",
            traditions = "some content",
            components = "some content",
            clients = "some content",
            simple_words = "some content",
        )
        cls.user_status = UserStatus.objects.create(
            user=cls.user,
            therapist=False,
            diver=False,
        )

        cls.user_status_data = {'therapist':True,'diver':True}

        cls.assemble_data = {
            "title":"some content",
            "position":"some content",
            "reality_assumptions":"some content",
            "change":"some content",
            "relational":"some content",
            "ontology":"some content",
            "knowledge":"some content",
            "traditions":"some content",
            "components":"some content",
            "clients":"some content",
            "simple_words":"some content"
        }

    def setup(self,add_perm=True):
        self.client.login(username = 'usertest',
            password = 'test123')
        if add_perm:
            self.client.post(reverse('accounts:edit_status'),self.user_status_data,follow=True)


    def test_assemble_by_date_rendering(self):
        self.setup()
        response = self.client.get(reverse('dive_app:assemble_by_date'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.assemble.title.title())
        self.assertTemplateUsed(response,'dive_app/assemble/assemble_by_date.html') 

    def test_assemble_by_title_rendering(self):
        self.setup()
        response = self.client.get(reverse('dive_app:assemble_by_title'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.assemble.title.title())
        self.assertTemplateUsed(response,'dive_app/assemble/assemble_by_title.html')


    def test_assemble_item_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/assemble/{self.assemble.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.assemble.title)
        self.assertTemplateUsed(response,'dive_app/assemble/assemble_item.html')


    def test_new_assemble_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/new_assemble/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Assemble Model: Exercise")
        self.assertTemplateUsed(response,'dive_app/assemble/new_assemble.html')


    def test_edit_assemble_rendering(self):
        self.setup()
        response = self.client.get(f'/diver/edit_assemble/{self.assemble.pk}/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Edit Assemble")
        self.assertTemplateUsed(response,'dive_app/assemble/edit_assemble.html')

    def test_new_assemble_post(self):
        self.setup()
        response = self.client.post('/diver/new_assemble/',self.assemble_data)
        self.assertRedirects(response,
                reverse('dive_app:index'),302)
        
    def test_edit_assemble_post(self):
        self.setup()
        response = self.client.post(f'/diver/edit_assemble/{self.assemble.pk}/',self.assemble_data)
        self.assertRedirects(response,
                f'/diver/assemble/{self.assemble.pk}/',302)