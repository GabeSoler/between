from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Personal_Style
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

    def test_profile_list_view(self):
        response = self.client.get(reverse('between_app:results_list'), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"14,03,2024")
        self.assertTemplateUsed(response,'between_app/personalstyle_list.html')
    
    def test_profile_detail_view(self):
        response = self.client.get(self.profile.get_absolute_url())
        no_response = self.client.get('between/123')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "Your Position")
        self.assertTemplateUsed(response, 'between_app/results.thml')

