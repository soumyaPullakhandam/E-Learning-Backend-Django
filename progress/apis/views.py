from rest_framework import generics
from rest_framework import permissions

from enrolment.models import Enrolment
from ..models import Progress
from .serializers import ProgressSerializers


def perform_action(self, serializer):
    serializer.save(student=self.request.user)


def perform_query(self):
    queryset = Progress.objects.filter(student=self.request.user)
    return queryset


class ProgressList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = ProgressSerializers

    def get_queryset(self):

        queryset = perform_query(self)

        lecture = self.request.query_params.get('lecture')
        student = self.request.query_params.get('student')

        if lecture:
            queryset = queryset.filter(course=lecture)
        elif student:
            queryset = queryset.filter(student=student)

        return queryset

    def perform_create(self, serializer):
        perform_action(self, serializer)


class ProgressUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = ProgressSerializers
    queryset = Progress.objects.all()

    def get_queryset(self):
        return perform_query(self)

    def perform_update(self, serializer):
        progress = serializer.save(student=self.request.user)

        course_duration = progress.lecture.topic.course.duration
        progress_duration = progress.lecture.duration
        percent = (progress_duration * 100) / course_duration

        course = progress.lecture.topic.course
        user = self.request.user

        enrol = Enrolment.objects.filter(course=course.id, student=user.id)
        enrol_per = enrol[0]
        enrol_per.completion = percent
        enrol_per.save()

        return progress
