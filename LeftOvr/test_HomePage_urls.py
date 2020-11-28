from django.urls import reverse,resolve
from django.test import TestCase
from django.http import HttpRequest
from htmlcss.views import (index,about,custReg,
                           cont, regRec, wh)


class TestCase_HomePageURLs(TestCase):
    def test_index_is_resolved(self):
        url= reverse('index')
        print (resolve(url))
        self.assertIn('<title>Home</title>',index)
        self.assertEquals(resolve(url).func, index)

    def test_about_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)
    def test_custReg_is_resolved(self):
        url = reverse('custReg')
        print(resolve(url))
        self.assertEquals(resolve(url).func, custReg)
    def test_why_is_resolved(self):
        url = reverse('wh')
        print(resolve(url))
        self.assertEquals(resolve(url).func, wh)
        """fixed one issue in urls for unittest"""
    def test_cont_is_resolved(self):
        url = reverse('cont')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cont)
    def test_receipt_is_resolved(self):
        url = reverse('regRec')
        f=resolve(url)
        print(f)
        self.assertEquals(f.func,regRec)


