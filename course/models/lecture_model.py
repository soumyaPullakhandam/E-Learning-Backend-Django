from django.db import models
from .course_model import Course
from home.models import UserProfile
from .topic_model import Topic


def upload_lecture(instance, filename):
    return "lecture/{user}/{course}/{filename}".format(user=instance.topic.course.author.username,
                                                       course=instance.topic.course.title,
                                                       filename=filename)


class Lecture(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    duration = models.FloatField()
    res_file = models.FileField(upload_to=upload_lecture, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
