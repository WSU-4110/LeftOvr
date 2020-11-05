from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


def profile_Image(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def default_profile_image():
    return "profile_images/defaultprofilepic.png"

class Customer(AbstractBaseUser):
    firstName       = models.CharField(max_length=30)
    lastName        = models.CharField(max_length=30)
    idNum           = models.CharField(verbose_name="idNum", max_length=13, unique=True)
    email           = models.EmailField(verbose_name="email", max_length=70, unique=True)
    passWords       = models.CharField(max_length=30, unique=True)
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    custAddress     = models.CharField(max_length=90)

    is_admin        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_superuser    =models.BooleanField(default=False)

    profile_image   =models.ImageField(max_length=255, upload_to=profile_Image, null=True, blank=True, default=default_profile_image)
    hide_email      =models.BooleanField(default=True)

    USERNAME_FIELD  =['email', 'passWords']
    REQUIRED_FIELDS =['firstName', 'lastName', 'idNum', 'custAddress']

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.email + ' ' + self.last_login

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def profile_image_fileName(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

class Restaurant(AbstractBaseUser):
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

class ContactUs(AbstractBaseUser):
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

class Profile(AbstractBaseUser):
    user = models.OneToOneField(AbstractBaseUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

