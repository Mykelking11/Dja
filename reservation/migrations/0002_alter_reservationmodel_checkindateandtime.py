# Generated by Django 4.2.9 on 2024-01-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='checkInDateandTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
