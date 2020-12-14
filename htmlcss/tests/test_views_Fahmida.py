from django.urls import reverse,resolve
from django.test import TestCase, Client

class Test(TestCase):

    def test_customer_Homepage(self):
        client = Client()
        self.client = Client()
        self.index = reverse('index')
        response = client.get(self.index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

