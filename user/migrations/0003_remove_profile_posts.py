# Generated by Django 2.2.7 on 2020-07-29 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_prof_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
    ]
