from rest_framework import generics
from rest_framework import permissions
from ..models import Enrolment
from .serializers import EnrolmentSerializers


def perform_action(self, serializer):
    serializer.save(student=self.request.user)


def perform_query(self):
    queryset = Enrolment.objects.all()
    if self.request.user.groups.filter(name='Student').__len__() > 0:
        queryset = Enrolment.objects.filter(student=self.request.user)
    elif self.request.user.groups.filter(name='Tutor').__len__() > 0:
        queryset = Enrolment.objects.filter(course__author=self.request.user)
    return queryset


class EnrolmentList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = EnrolmentSerializers

    def get_queryset(self):

        queryset = perform_query(self)

        course = self.request.query_params.get('course')
        student = self.request.query_params.get('student')

        if course:
            queryset = queryset.filter(course=course)
        elif student:
            queryset = queryset.filter(student=student)

        return queryset

    def perform_create(self, serializer):
        perform_action(self, serializer)


class EnrolmentUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = EnrolmentSerializers

    def get_queryset(self):
        return perform_query(self)
