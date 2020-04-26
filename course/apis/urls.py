from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CourseList, \
    CourseCreate, \
    CourseUpdate, \
    CategoryList, \
    TopicList, \
    TopicUpdate, \
    LectureList, \
    LectureUpdate, \
    NestedList, \
    NestedUpdate

urlpatterns = [
    path('course/', CourseList.as_view(), name='course-list'),
    path('course/create/', CourseCreate.as_view(), name='course-create'),
    path('course/<int:pk>/', CourseUpdate.as_view(), name='course-update'),
    path('cat/', CategoryList.as_view(), name='Category-list'),
    path('topic/', TopicList.as_view(), name='Topic-list'),
    path('topic/<int:pk>/', TopicUpdate.as_view(), name='Topic-update'),
    path('lecture/', LectureList.as_view(), name='Lecture-list'),
    path('lecture/<int:pk>/', LectureUpdate.as_view(), name='Lecture-update'),
    path('batch/', NestedList.as_view(), name='batchLearn-list'),
    path('batch/<int:pk>/', NestedUpdate.as_view(), name='batchLearn-update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
