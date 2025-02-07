from django.db import models

# Create your models here.
class Chicken(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Seafood(models.Model):
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

class Meat(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Beef(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Pork(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)