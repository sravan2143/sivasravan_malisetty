# Generated by Django 5.0 on 2023-12-13 03:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]