from django.db import models

# Create your models here.
class Capybara(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.TextField(max_length=500)