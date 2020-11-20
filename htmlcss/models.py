from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    pass

def profile_pics(self):
    return f'profile_pics/{self.pk}/{"profile_pics.png"}'

def default_profile_pics():
    return "profile_pics/default-picture_0_0.png"

class User(AbstractUser):
    class Types(models.TextChoices):
        Customer = "CUSTOMER", "Customer"
        Restaurant = "RESTAURANT", "Restaurant"

    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.Customer)

    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Customer)

class Customer(User):
    objects = CustomerManager
    class Meta:
        proxy = True

    @property
    def more(self):
        return self.customermore

    #profile_pic = models.ImageField(max_length=255, upload_to=profile_pics, null=True, blank=True, default=default_profile_pics)
    #hide_email = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.Customer
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    #def profile_image_fileName(self):
       # return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]


class CustomerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    idNum = models.CharField(verbose_name="idNum", max_length=13)
    custAddress = models.CharField(max_length=90, null=True)
    profile = models.ForeignKey(profile, related_name="profi", on_delete=models.CASCADE)


class RestaurantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Restaurant)


class RestaurantMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    busName = models.CharField(max_length=500)
    busAddress = models.CharField(max_length=500)
    einNum = models.CharField(max_length=9)
    profile = models.ForeignKey(profile,related_name="profil", on_delete=models.CASCADE)

class Restaurant(User):
    objects = RestaurantManager
    class Meta:
        proxy = True

    @property
    def more(self):
        return self.restaurantmore

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.Restaurant

    def __str__(self):
        return self.email


class ContactUs(models.Model):

    name = models.CharField(max_length=300)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=13)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.message


