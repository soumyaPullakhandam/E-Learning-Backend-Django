# Generated by Django 3.0.5 on 2020-04-25 12:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0012_auto_20200425_1025'),
        ('enrolment', '0014_auto_20200425_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrolment',
            old_name='user',
            new_name='student',
        ),
        migrations.AlterUniqueTogether(
            name='enrolment',
            unique_together={('course', 'student')},
        ),
    ]
