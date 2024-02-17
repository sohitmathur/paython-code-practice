from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    mobile = models.BigIntegerField()
    per = models.FloatField()

