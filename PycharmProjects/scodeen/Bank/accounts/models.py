from django.db import models

# Create your models here.

class AccountDetails(models.Model):
    id=models.IntegerField(primary_key=True)
    account_name = models.CharField(max_length=25)
    bal= models.FloatField()
    acdate = models.DateField()
    email=models.EmailField()
    mobile= models.CharField(max_length=13)
