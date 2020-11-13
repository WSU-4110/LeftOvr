from django.db import models
from django.contrib.auth.models import  User, AbstractBaseUser, BaseUserManager


def profile_Image(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def default_profile_image():
    return "profile_images/defaultprofilepic.png"

class Customer(models.Model):
    def __str__(self, port):
        self.port=port
        self.firstName  = models.CharField(max_length=30)
        self.lastName        = models.CharField(max_length=30)
        self.idNum           = models.CharField(verbose_name="idNum", max_length=13)
        self.email           = models.EmailField(max_length=70, unique=True)
        self.password       = models.CharField(max_length=30, unique=True, null=True)
        self.date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
        self.last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
        self.custAddress     = models.CharField(max_length=90, null=True)

    is_admin        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_superuser    =models.BooleanField(default=False)

    #profile_image   =models.ImageField(max_length=255, upload_to=profile_Image, null=True, blank=True, default=default_profile_image)
    hide_email      =models.BooleanField(default=True)

    def build(self):
        return Port(self.email)
    def profile_Image(self):
        return Port(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

class Restaurant(models.Model):
    def __str__(self, port):
        self.busName = models.CharField(max_length=500)
        self.busAddress = models.CharField(max_length=500)
        self.einNum = models.CharField(max_length=9)
        self.busEmail = models.CharField(max_length=750)
        self.busPassWords = models.CharField(max_length=500)

    def build(self):
        return Port(self.busName + '  ' + self.busAddress + '   ' + self.einNum+ '   '+self.busEmail+ '   '+self.busPassWords)

class Meals(models.Model):
    def __str__(self, port):
        self.mealType = models.CharField(max_length=500)
        self.mealAvail = models.CharField(max_length=1000)

    def build(self):
        return Port(self.mealAvail + ' ' + self.mealType)

class ContactUs(models.Model):
    def __str__(self, port):
        self.nameC = models.CharField(max_length=300)
        self.emailC = models.CharField(max_length=500)
        self.phoneC = models.CharField(max_length=13)
        self.messageC = models.TextField(blank=True, null=True)

    def build(self):
        return Port(self.nameC + ' ' + self.emailC + ' ' + self.phoneC + ' ' + self.messageC)

class LocationArea(models.Model):
    def __str__(self, port):
        self.localArea = models.DecimalField(decimal_places=2, max_digits=10000)
        self.localName = models.CharField(max_length=500)

    def build(self):
        return Port(self.localName + ' ' + self.localArea)

class Profile(models.Model):
    def __str__(self, port):
        self.user = models.OneToOneField(User, on_delete=models.CASCADE)
        self.image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def build(self):
        return f'{self.user.username} Profile'