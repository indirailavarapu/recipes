from django.db import models

# Create your models here.
class Soups(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Curries(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class VegBiryani(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class FastFood(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Starters(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class StirFry(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class QuickAndEasy(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)