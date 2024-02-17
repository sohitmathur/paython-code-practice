# Generated by Django 4.1.4 on 2023-02-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('model', models.CharField(max_length=20)),
                ('colours', models.CharField(choices=[('BLACK', 'BLACK'), ('RED', 'RED'), ('SILVER', 'SILVER')], default='BLACK', max_length=6)),
            ],
        ),
    ]