# Generated by Django 4.2.9 on 2024-03-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestpreferenceapp', '0004_alter_preferencemodel_airconditioner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencemodel',
            name='airconditioner',
            field=models.BooleanField(choices=[('on', 'True'), ('off', 'False')], default='Boolean_choice[1]'),
        ),
    ]
