from django.db import models


# Create your models here.
class employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=15)
    empsal=models.IntegerField()


class FeedbackForm(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField
    city = models.CharField(max_length=20)
