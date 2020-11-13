from django.db import models
from django.contrib.auth.models import  User, AbstractBaseUser, BaseUserManager


def profile_Image(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def default_profile_image():
    return "profile_images/defaultprofilepic.png"

class Customer(models.Model):
    firstName       = models.CharField(max_length=30)
    lastName        = models.CharField(max_length=30)
    idNum           = models.CharField(verbose_name="idNum", max_length=13)
    email           = models.EmailField(max_length=70, unique=True)
    password       = models.CharField(max_length=30, unique=True, null=True)
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    custAddress     = models.CharField(max_length=90, null=True)

    is_admin        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_superuser    =models.BooleanField(default=False)

    #profile_image   =models.ImageField(max_length=255, upload_to=profile_Image, null=True, blank=True, default=default_profile_image)
    hide_email      =models.BooleanField(default=True)

    def __str__(self):
        return self.email

    def profile_image_fileName(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

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

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'