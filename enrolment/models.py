from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from home.models import UserProfile
from course.models import Course


class Enrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, unique=False)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, unique=False)
    enrol_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True, null=True,
                                 default=0)
    completion = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)], blank=True, null=True,
                                   default=0)

    class Meta:
        unique_together = [('course', 'student')]
