from rest_framework import generics
from ELearning.restconf.permission import IsOwnerOrReadOnlyLec
from rest_framework import permissions
from course.models import Lecture
from ..serializers.lecture_serializer import LectureSerializers
from django.db.models import Sum


def perform_duration(self, serializer):
    new_lec = serializer.save()
    lecture = Lecture.objects.filter(topic__course__author=self.request.user)
    lec_total = lecture.aggregate(Sum('duration'))
    new_lec.topic.course.duration = lec_total['duration__sum']
    new_lec.topic.course.save()


class LectureList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyLec]
    serializer_class = LectureSerializers

    def perform_create(self, serializer):
        perform_duration(self, serializer)

    def get_queryset(self):
        queryset = Lecture.objects.all()
        course = self.request.query_params.get('course')
        author = self.request.query_params.get('author')
        topic = self.request.query_params.get('topic')

        if course:
            queryset = queryset.filter(course=course)
        elif author:
            queryset = queryset.filter(topic__course__author=author)
        elif topic:
            queryset = queryset.filter(topic=topic)

        return queryset


class LectureUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyLec]
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializers

    def perform_update(self, serializer):
        perform_duration(self, serializer)
