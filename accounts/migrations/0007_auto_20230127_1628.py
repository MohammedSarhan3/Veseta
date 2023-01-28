# Generated by Django 3.2 on 2023-01-27 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_join_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_us',
        ),
        migrations.AddField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='وقت الإنضمام: '),
            preserve_default=False,
        ),
    ]
