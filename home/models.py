from django.db import models
from django.contrib.auth.models import AbstractUser
from languages.fields import LanguageField


class Languages(models.Model):
    language = LanguageField(max_length=20)

    def __str__(self):
        return self.language


class UserProfile(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    language = models.ManyToManyField(Languages)
    website = models.URLField(blank=True, null=True, max_length=200)
    qualification = models.CharField(blank=True, null=True, max_length=200)
    phone = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return super().username
