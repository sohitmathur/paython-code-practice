# Generated by Django 4.1.4 on 2023-02-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modellapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
