# Generated by Django 3.2 on 2023-01-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230127_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='google',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='google'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twiter',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='twiter'),
        ),
    ]