# Generated by Django 4.1.4 on 2023-02-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0003_alter_mobilemodel_colours'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilemodel',
            name='network_band',
            field=models.CharField(choices=[('4G', '4G'), ('5G', '5G'), ('6G', '6G')], default='BLACK', max_length=6),
        ),
    ]
