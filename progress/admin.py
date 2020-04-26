from django.contrib import admin
from .models import Progress


class ProgressAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'student', 'completion', 'timestamp')
    list_filter = [
        ('lecture', admin.RelatedOnlyFieldListFilter),
        ('student', admin.RelatedOnlyFieldListFilter)
    ]


admin.site.register(Progress,ProgressAdmin)
