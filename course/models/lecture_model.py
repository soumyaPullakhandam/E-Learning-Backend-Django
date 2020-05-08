from django.db import models
from .topic_model import Topic
from .course_model import Course
import django.utils.timezone


def upload_lecture(instance, filename):
    return "lecture/{user}/{course}/{filename}".format(user=instance.course.author.username,
                                                       course=instance.course.title,
                                                       filename=filename)


class LectureFile(models.Model):
    file = models.FileField(upload_to=upload_lecture, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Lecture(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    duration = models.FloatField()
    lectureFile = models.ForeignKey(LectureFile, on_delete=models.CASCADE);
    timestamp = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title
