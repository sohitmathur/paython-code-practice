# Generated by Django 4.1.4 on 2023-02-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modellapp', '0003_student_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=6),
        ),
    ]
