from django.db import models

# Create your models here.
class ShirtModel(models.Model):
    name=models.CharField(max_length=15)
    size=models.CharField(max_length=15)
    img = models.ImageField(upload_to="xyz")

