# Generated by Django 3.1.4 on 2021-10-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpsend', '0002_remove_car_registration_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_registration',
            name='phonenumber',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
