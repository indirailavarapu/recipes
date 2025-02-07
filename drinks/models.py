from django.db import models

# Create your models here.
class Milkshakes(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Smoothies(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Tea(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Coffee(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Juices(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)