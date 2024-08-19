from django.db import models

# Create your models here.

class PopularTour(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to = 'images/')
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TopPackage(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    
    def __Str__(self):
        return self.name

class DomesticPackage(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    def __Str__(self):
        return self.name

class InternationalPackage(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    def __Str__(self):
        return self.name

class MedicalPackage(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    def __Str__(self):
        return self.name

class HotelBooking(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    def __Str__(self):
        return self.name

class TicketBooking(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    def __Str__(self):
        return self.name



