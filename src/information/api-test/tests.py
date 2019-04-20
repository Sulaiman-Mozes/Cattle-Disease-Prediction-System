from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from information.models import Disease


User = get_user_model()
class DiseaseApiTestCase(APITestCase):
    def setUp(self):
        user = User(username='testuser', email='test@test.com')
        user.set_password("testpassword")
        user.save()
        disease = Disease.objects.create(
            disease="Hello",
            description="How are you",
            causes="hope",
            symptoms="you",
            treatment="are",
            prevention="good"
        )


    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_Disease(self):
        disease_count = Disease.objects.count()
        self.assertEqual(disease_count, 1)

    def test_list_diseases(self):
        self.client.login(username='testuser', password="testpassword")
        data = {}
        url = reverse('api:ListCreate')
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_a_disease(self):
        self.client.login(username='testuser', password="testpassword")
        data = {
            "disease":"Hello World",
            "description": "How are you doning",
            "causes": "hope its good",
            "symptoms": "you okay",
            "treatment": "are you kawa",
            "prevention": "good or better"
        }
        url = reverse('api:ListCreate')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_single_disease(self):
        self.client.login(username='testuser', password="testpassword")
        data = {}
        disease = Disease.objects.first()
        url = disease.get_api_url()
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_single_disease(self):
        self.client.login(username='testuser', password="testpassword")
        data = {
            "disease":"new Hello",
            "description": "new How",
            "causes": "new hope",
            "symptoms": "new okay",
            "treatment": "new are",
            "prevention": "new good"
        }
        disease = Disease.objects.first()
        url = disease.get_api_url()
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_single_disease(self):
        self.client.login(username='testuser', password="testpassword")
        data = {}
        disease = Disease.objects.first()
        url = disease.get_api_url()
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)