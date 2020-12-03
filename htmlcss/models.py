from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    customerAddress = models.CharField(max_length=90, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.firstName



class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    businessName = models.CharField(verbose_name="Business Name", max_length=50)
    businessAddress = models.CharField(verbose_name="busAddress", max_length=90, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.businessName


class ContactUs(models.Model):

    name = models.CharField(max_length=300)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=13)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


