# Generated by Django 4.0.2 on 2022-06-11 14:04

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newsman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
