# Generated by Django 3.2 on 2023-01-27 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_profile_join_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_new',
            field=models.DateField(blank=True, default='2012-09-04 06:00:00.000000-08:00', null=True, verbose_name='وقت الإنضمام: '),
        ),
    ]
