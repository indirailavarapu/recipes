from django.db import models

# Create your models here.
class Traditional(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Chips(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Fries(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class SpringRolls(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)
