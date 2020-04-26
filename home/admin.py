from django.contrib import admin
from .models import UserProfile,Languages

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Languages)