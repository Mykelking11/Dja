# Generated by Django 4.2.9 on 2024-01-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_remove_reservationmodel_payment'),
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='reservation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.reservationmodel'),
        ),
    ]
