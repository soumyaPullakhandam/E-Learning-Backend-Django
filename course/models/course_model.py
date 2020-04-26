from django.db import models
from django.core.validators import MaxValueValidator

from home.models import UserProfile
from languages.fields import LanguageField


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(10)], blank=True, null=True, default=0)
    language = LanguageField(max_length=20, default='en', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courses')
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title
