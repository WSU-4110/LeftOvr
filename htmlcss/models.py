from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    idNum = models.CharField(max_length=13)
    email = models.CharField(max_length=500)
    passWords = models.CharField(max_length=500)


    custAddress = " "

    def __str__(self):
        return self.firstName + ' ' + self.lastName + '   ' + self.custAddress + '   ' + self.idNum

class Restaurant(models.Model):
    busName = models.CharField(max_length=500)
    busAddress = models.CharField(max_length=500)
    einNum = models.CharField(max_length=9)
    busEmail = models.CharField(max_length=750)
    busPassWords = models.CharField(max_length=500)

    def __str__(self):
        return self.busName + '  ' + self.busAddress + '   ' + self.einNum

class Meals(models.Model):
    mealType = models.CharField(max_length=500)
    mealAvail = models.CharField(max_length=1000)

    def __str__(self):
        return self.mealAvail + ' ' + self.mealType

class ContactUs(models.Model):
    nameC = models.CharField(max_length=300)
    emailC = models.CharField(max_length=500)
    phoneC = models.CharField(max_length=13)
    messageC = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nameC + ' ' + self.emailC + ' ' + self.phoneC + ' ' + self.messageC

class LocationArea(models.Model):
    localArea = models.DecimalField(decimal_places=2, max_digits=10000)
    localName = models.CharField(max_length=500)

    def __str__(self):
        return self.localName + ' ' + self.localArea

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

