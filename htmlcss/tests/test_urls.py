from unittest import TestCase
from django.urls import reverse, resolve
from htmlcss.views import index
from htmlcss.views import custReg
from htmlcss.views import about
from htmlcss.views import wh
from htmlcss.views import cont
from htmlcss.views import regRec


class TestCase_HomePageURLs(TestCase):

    def test_index_is_resolved(self):
        url= reverse('index')
        print (resolve(url))
        self.assertIn('<title>Home</title>', index)
        self.assertEquals(resolve(url).func.view_class, index)

    def test_about_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, about)

    def test_custReg_is_resolved(self):
        url = reverse('custReg')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, custReg)

    def test_why_is_resolved(self):
        url = reverse('wh')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, wh)
        """fixed one issue in urls for unittest"""

    def test_cont_is_resolved(self):
        url = reverse('cont')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, cont)

    def test_receipt_is_resolved(self):
        url = reverse('regRec')
        f = resolve(url)
        print(f)
        self.assertEquals(f.func.view_class, regRec)
