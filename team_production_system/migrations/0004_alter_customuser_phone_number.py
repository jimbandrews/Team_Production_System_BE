# Generated by Django 4.1.7 on 2023-05-04 21:00

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('team_production_system', '0003_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                default=' ',
                max_length=128,
                null=True,
                region=None,
                unique=True,
            ),
        ),
    ]
