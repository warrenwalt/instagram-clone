# Generated by Django 2.2.7 on 2020-09-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_posts', '0002_auto_20200915_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='no_of_comments',
            field=models.IntegerField(),
        ),
    ]