# Generated by Django 4.1.5 on 2023-01-12 01:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Fecha Nacimiento'),
        ),
    ]