from django.db import models

# Create your models here.
class MobileModel(models.Model):
    company_name = models.CharField(max_length=20)
    price = models.FloatField()
    model = models.CharField(max_length=20)
    colour = [('BLACK', 'Black'), ('RED', 'Red'),('SILVER','Silver')]
    colours = models.CharField(max_length=6, choices=colour, default='BLACK', )
    band = [('4G', '4G'), ('5G', '5G'), ('6G', '6G')]
    network_band = models.CharField(max_length=6, choices=band, default='BLACK', )



