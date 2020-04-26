from django.db import models
from .course_model import Course
from home.models import UserProfile


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    # author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='topics')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
