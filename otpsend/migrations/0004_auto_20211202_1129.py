# Generated by Django 3.2.7 on 2021-12-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpsend', '0003_car_registration_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
