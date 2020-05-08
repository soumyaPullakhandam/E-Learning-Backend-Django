from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from ELearning.restconf.permission import IsOwnerOrReadOnlyLec
from rest_framework import permissions
from course.models import Lecture, LectureFile
from ..serializers.lecture_serializer import LectureSerializers, LectureFileSerializer
from django.db.models import Sum
from django.db.models import Q


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


class LectureFileList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyLec]
    serializer_class = LectureFileSerializer
    parser_classes = [MultiPartParser, FormParser]

    # queryset = LectureFile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Message': 'You have successfully register'}, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = LectureFile.objects.all()
        course = self.request.query_params.get('course')
        topic = self.request.query_params.get('topic')

        if course and not topic:
            queryset = queryset.filter(course=course)
        elif topic and not course:
            queryset = queryset.filter(topic=topic)

        elif course and topic:
            queryset = queryset.filter(Q(course=course) & Q(topic=topic))

        return queryset


class LectureFileUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyLec]
    queryset = LectureFile.objects.all()
    serializer_class = LectureFileSerializer
