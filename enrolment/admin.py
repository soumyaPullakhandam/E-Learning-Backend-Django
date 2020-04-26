from django.contrib import admin
from .models import Enrolment


class EnrolmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating', 'completion', 'enrol_date')
    list_filter = [
        ('student', admin.RelatedOnlyFieldListFilter),
        ('course', admin.RelatedOnlyFieldListFilter),
        # ('rating', admin.RelatedOnlyFieldListFilter)
    ]


admin.site.register(Enrolment, EnrolmentAdmin)
