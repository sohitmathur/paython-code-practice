from django.db import models

# Create your models here.
class Student(models.Model):
    stud_id=models.IntegerField()
    sname=models.CharField(max_length=100)
    stud_email=models.EmailField(max_length=100)
    stud_pass=models.CharField(max_length=100)




