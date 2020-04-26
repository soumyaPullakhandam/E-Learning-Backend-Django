from rest_framework import generics
from ELearning.restconf.permission import IsOwnerOrReadOnlyTopic
from rest_framework import permissions
from course.models import Topic
from ..serializers.topic_serializer import TopicSerializers


class TopicList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyTopic]
    serializer_class = TopicSerializers

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Topic.objects.all()
        course = self.request.query_params.get('course')
        course__author = self.request.query_params.get('author')

        if course__author:
            queryset = queryset.filter(course__author=course__author)

        elif course:
            queryset = queryset.filter(course=course)

        return queryset


class TopicUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyTopic]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers
