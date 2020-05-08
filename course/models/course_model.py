from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from home.models import UserProfile
from languages.fields import LanguageField
import django.utils.timezone


class Category(models.Model):
    title = models.CharField(max_length=200)
    # title_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


def upload_course(instance, filename):
    return "course/{user}/{filename}".format(user=instance.author.username, filename=filename)


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True, null=True,
                                 default=0)
    language = LanguageField(max_length=20, default='en', blank=True, null=True)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)
    image = models.ImageField(upload_to=upload_course, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courses')
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title
