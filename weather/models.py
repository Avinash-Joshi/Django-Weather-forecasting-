from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Data(models.Model):
    State = models.CharField(max_length=60, primary_key=True)
    Today_Temp = models.FloatField(default="Something Wrong")
    Today_wind = models.FloatField(default="Something wrong")
    Today_condition = models.CharField(
        max_length=40, default="Something wrong")
    TempVsDate = models.ImageField(
        upload_to="weather/images", blank=True, null=True, default="weather/images/Error.png")
    ConditionVsDate = models.ImageField(
        upload_to="weather/images", blank=True, null=True, default="E:/Miniproject/Weatherforecasting/media/weather/images/Error.png")

    def __str__(self):
        return self.State


class Contact(models.Model):
    Name = models.CharField(max_length=60, blank=False)
    Phone = models.BigIntegerField(
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    Email = models.EmailField(max_length=254)
    Issue_or_Feedback = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.Name

    # Today_sunrise = models.TimeField(default="")
    # Today_sunset = models.TimeField(default="")


class CSV(models.Model):
    Name = models.CharField(max_length=50)
    file = models.FileField(upload_to="weather/static/csv", default="")

    def __str__(self):
        return self.Name
