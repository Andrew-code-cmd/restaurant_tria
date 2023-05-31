from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()

class Salat(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()

class Fish(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()

class Soup(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()    
    
class Cart(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username =  models.CharField(max_length=51)
    name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    mail =  models.EmailField()
    phone =  models.PositiveIntegerField()

class Guest(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()