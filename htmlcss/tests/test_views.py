from django.test import TestCase, Client
from django.urls import reverse
import imp

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.proPage = reverse('proPage')
        self.login = reverse('login')
        self.register = reverse('register')
        self.LeoReview = reverse('Leo')
        self.DomReview = reverse('Dom')
        self.ChipReview = reverse('Chip')


    def test_project_login_get(self):
        client = Client()

        response = client.get(self.login)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
