# Generated by Django 4.2.9 on 2024-01-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guestpreferenceapp', '0001_initial'),
        ('reservation', '0008_alter_reservationmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='preference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestpreferenceapp.preferencemodel'),
        ),
    ]
