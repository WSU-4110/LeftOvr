from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    idNum = models.CharField(max_length=12)
    email = models.CharField(max_length=500)
    passWords = models.CharField(max_length=500)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.idNum

class Restaurant(models.Model):
    busName = models.CharField(max_length=500)
    busAddress = models.CharField(max_length=500)
    einNum = models.CharField(max_length=9)
    busEmail = models.CharField(max_length=750)
    busPassWords = models.CharField(max_length=500)

    def __str__(self):
        return self.busName + ' ' + self.einNum

class Meals(models.Model):
    mealType = models.CharField(max_length=500)
    mealAvail = models.CharField(max_length=1000)

    def __str__(self):
        return self.mealAvail + ' ' + self.mealType

class slots(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal


