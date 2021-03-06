# Generated by Django 3.0.5 on 2020-04-23 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_auto_20200423_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrolment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Enrol'),
        ),
        migrations.AlterField(
            model_name='enrol',
            name='enrol',
            field=models.ManyToManyField(blank=True, null=True, through='course.Course', to=settings.AUTH_USER_MODEL),
        ),
    ]
