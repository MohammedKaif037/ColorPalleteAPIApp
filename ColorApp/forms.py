from django.db import models

# Create your models here.
class Color(models.Model):
    name=models.CharField(max_length=100)
    hex_code=models.CharField(max_length=100)

