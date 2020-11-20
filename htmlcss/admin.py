from django.contrib import admin
from .models import Customer
from .models import Restaurant
from .models import ContactUs
from .models import profile

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(ContactUs)
admin.site.register(profile)
