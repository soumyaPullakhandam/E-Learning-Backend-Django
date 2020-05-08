from django.db import models
from .course_model import Course
import django.utils.timezone


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    timestamp = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title
