from django.db import models

# Create your models here.
class CourseInfoModel(models.Model):
    cname = models.CharField(max_length=25)
    cduration = models.FloatField()
    cfees = models.IntegerField()
    cmentor = models.CharField(max_length=25)

class StudRegistration(models.Model):
    sname=models.CharField(max_length=25)
    smobile=models.IntegerField()
    semail = models.EmailField()
    saddress= models.TextField()

