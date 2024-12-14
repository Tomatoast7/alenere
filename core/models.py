from django.db import models
from django.urls import reverse
# Create your models here.

class tablename(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    fav_color = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("core_index")
    
# Practice
    
class product(models.Model):
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("productview")

class inventory(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("perindexview")


class info(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
  
    def get_absolute_url(self):
        return reverse("newindex")
    
class alenereproduct(models.Model):
    product = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("alenereindex")