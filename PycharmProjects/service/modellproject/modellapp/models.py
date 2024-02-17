from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=45)
    email = models.EmailField()
    date = models.DateTimeField()
    mobile = models.BigIntegerField()
    per = models.FloatField()
    test = models.BooleanField(default=True)


    Gender = [('MALE', 'MALE'),('FEMALE', 'FEMALE'),]
    year_in_school = models.CharField(max_length=6,choices=Gender,default='MALE',)

    def is_upperclass(self):
        return self.year_in_school in {self.MALE,self.FEMALE}

class FeedbackModel(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    city = models.CharField(max_length=15)
