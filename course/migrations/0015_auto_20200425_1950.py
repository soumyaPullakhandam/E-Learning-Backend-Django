# Generated by Django 3.0.5 on 2020-04-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_remove_topic_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='course.Category'),
        ),
    ]
