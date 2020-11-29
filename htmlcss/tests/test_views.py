from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.cont = reverse('cont')
        self.register = reverse('register')
        self.LeoReview = reverse('Leo')
        self.DomReview = reverse('Dom')
        self.ChipReview = reverse('Chip')

    def test_project_index_get(self):
        client = Client()

        response = client.get(self.index)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_contact_get(self):
        client = Client()

        response = client.get(self.cont)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_project_register_get(self):
        client = Client()

        response = client.get(self.register)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_project_LeosConey_get(self):
        client = Client()

        response = client.get(self.LeoReview)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'LeosReview.html')

    def test_project_Dominos_get(self):
        client = Client()

        response = client.get(self.DomReview)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DominosReview.html')

    def test_project_Chipotele_get(self):
        client = Client()

        response = client.get(self.ChipReview)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ChipotleReview.html')