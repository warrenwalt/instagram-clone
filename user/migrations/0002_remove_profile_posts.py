# Generated by Django 2.2.7 on 2020-09-15 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
    ]
