# Generated by Django 3.0.5 on 2020-04-25 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20200425_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='author',
        ),
    ]
