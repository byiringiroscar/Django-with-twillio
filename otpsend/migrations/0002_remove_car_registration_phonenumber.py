# Generated by Django 3.1.4 on 2021-10-01 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otpsend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_registration',
            name='phonenumber',
        ),
    ]