from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    writedate = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)


class Latlng(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)

class Seoul(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)

class GIG(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)

class CD(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)

class JG(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)

class GDBU(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)

class Jeju(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=7, decimal_places=3)
    lng = models.DecimalField(max_digits=7, decimal_places=3)
    address = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.name + "," + str(self.lat) + "," + str(self.lng) + "," + str(self.address) + "," + str(self.homepage)
