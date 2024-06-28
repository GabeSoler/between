from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Personal_Style,Components,BigTraditions
from django.utils import timezone

# Create your tests here.
class PersonalStyleTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )

        cls.profile = Personal_Style.objects.create(
                created_at = "2024-03-14 11:14:07.738883+00:00",
                updated_at = "2024-03-14 11:14:07.738883+00:00",
                user = cls.user,
                follower_1 = 1,
                propositive_1 = 2,
                challenger_1 = 6,
                acceptant_1 = 10,
                intensive_1 = -5,
                extensive_1 = 6,
                divider_1 = 3,
                containment_1 = 1,
                becoming_1 = 1,
                development_1 = 6,
                individuation_1 = 10,
                belonging_1 = 3,
                ) 
    def test_Profile_creation(self):
        self.assertEqual(f"{self.profile.follower_1}",'1')
        self.assertEqual(f"{self.profile.containment_1}",'1')
        self.assertEqual(f"{self.profile.created_at}","2024-03-14 11:14:07.738883+00:00")

    def test_test_home_view(self):
        response = self.client.get(reverse('between_app:test_home'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Therapist Style")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/test-home.html')


    def test_position_list_view(self):
        response = self.client.get(reverse('between_app:position_list'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"14,03,2024")
        self.assertTemplateUsed(response,'between_app/templates/between_app/personal_style/positions_list.html')
    

    def test_take_profile_test(self):
        response = self.client.get(reverse('between_app:profile_test'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Take a Personal Profile Test")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/personal_style/profile_test.html')
    
    def test_style_detail_view(self):
        response = self.client.get(Personal_Style.get_absolute_url())
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Therapist Style: Scores")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/personal_style/style_detail.html')

    def test_ps_results_view(self):
        response = self.client.get(reverse('between_app:results',self.profile.id), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Results")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/personal_style/results_email.html')

    def test_content_view(self):
        response = self.client.get(reverse('between_app:content'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "categories explained")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/personal_style/content.html')


   

class ComponentsTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )

        cls.profile = Components.objects.create(
                created_at = "2024-03-14 11:14:07.738883+00:00",
                updated_at = "2024-03-14 11:14:07.738883+00:00",
                user = cls.user,
                body = 30,
                feelings = 40,
                expression = 1,
                thoughts = 1,
                narrative = 60,
                #extended awareness
                dreaming = 1,
                re_prog = 1,
                subliminal = 70,
                subparts = 1,
                spiritual = 1,
                #Context work
                relational = 1,
                systems = 90,
                setup = 1,
                transOb = 1,
                family = 1,
                #Culture
                antropology = 65,
                arts = 1,
                politics = 1,
                philosophy = 99,
                worldview = 1,
                #identity
                individuation = 1,
                sex_gender = 1,
                values = 1,
                belonging = 30,
                roles = 1,
                ) 
    def test_components_creation(self):
        self.assertEqual(f"{self.profile.politics}",'1')
        self.assertEqual(f"{self.profile.philosophy}",'99')
        self.assertEqual(f"{self.profile.created_at}","2024-03-14 11:14:07.738883+00:00")

    def test_home_view(self):
        response = self.client.get(reverse('between_app:text_home'), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Narrative")
        self.assertTemplateUsed(response,'between_app/test-home.html')

    def test_components_list_view(self):
        response = self.client.get(reverse('between_app:components_list'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Your Components tests")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/Components/components_list.html')

    def test_components_detail_view(self):
        response = self.client.get(reverse('between_app:components_detail'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Components Test")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/Components/components_detail.html')

    def test_take_components_view(self):
        response = self.client.get(reverse('between_app:components_test'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Components test")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/Components/components_test.html')

class BigTraditionsTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username = 'usertest',
            email = 'test@test.com',
            password = 'test123',
        )

        cls.profile = BigTraditions.objects.create(
                created_at = "2024-03-14 11:14:07.738883+00:00",
                updated_at = "2024-03-14 11:14:07.738883+00:00",
                user = cls.user,
                hemeneutic = 20,
                phenomenological = 80,
                cybernetic = 60,
                spiritual = 70,
                scientific = 50,
                constructive = 30,
                participatory = 90,
                            ) 
    def test_components_creation(self):
        self.assertEqual(f"{self.profile.hemeneutic}",'20')
        self.assertEqual(f"{self.profile.cybernetic}",'60')
        self.assertEqual(f"{self.profile.created_at}","2024-03-14 11:14:07.738883+00:00")

    def test_home_view(self):
        response = self.client.get(reverse('between_app:text_home'), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Hemeneutic")
        self.assertTemplateUsed(response,'between_app/test-home.html')

    def test_big_trad_list_view(self):
        response = self.client.get(reverse('between_app:traditions_list'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Your Traditions Tests")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/BigTraditions/traditions_list.html')

    def test_big_trad_detail_view(self):
        response = self.client.get(reverse('between_app:traditions_detail',self.profile.id), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Big Traditions")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/BigTraditions/traditions_detail.html')

    def test_take_components_view(self):
        response = self.client.get(reverse('between_app:traditions_test'), follow=True)
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Traditions Test")
        self.assertTemplateUsed(response, 'between_app/templates/between_app/BigTraditions/traditions_test.html')
