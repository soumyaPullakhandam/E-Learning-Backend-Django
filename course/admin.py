from django.contrib import admin
from .models import Course, Topic, Lecture, Category, LectureFile


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'topic')
    list_filter = [
        ('topic', admin.RelatedOnlyFieldListFilter)
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'pub_date', 'author', 'rating', 'price', 'duration')
    list_filter = [
        ('author', admin.RelatedOnlyFieldListFilter)
    ]

    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'author', None) is None:
    #         obj.author = request.user
    #     obj.save()


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = [
        ('course', admin.RelatedOnlyFieldListFilter)
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(LectureFile)
