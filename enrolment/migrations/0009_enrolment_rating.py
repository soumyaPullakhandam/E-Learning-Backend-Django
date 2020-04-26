# Generated by Django 3.0.5 on 2020-04-25 10:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolment', '0008_auto_20200423_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolment',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
