from django.db import models

# Create your models here.
class Latest(models.Model):
    name=models.CharField(max_length=100)
    matter=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    ingredients=models.TextField()


class Trending(models.Model):
    name=models.CharField(max_length=100)
    matter=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField()
    ingredients=models.TextField()