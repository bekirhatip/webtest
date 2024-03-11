from django.db import models

# Create your models here.

class TestModel(models.Model):
    value= models.CharField(max_length=255, default="No Input")