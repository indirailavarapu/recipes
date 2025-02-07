from django.db import models

# Create your models here.
class Idly(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Dosa(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Puri(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Vada(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Chapati(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)

class Parota(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    video=models.URLField(null=True,max_length=500)