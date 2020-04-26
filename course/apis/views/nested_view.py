from rest_framework import generics
from ELearning.restconf.permission import IsOwnerOrReadOnlyLec
from rest_framework import permissions
from course.models import Topic
from ..serializers.nested_serializer import TopicNestedSerializers


class NestedList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyLec]
    serializer_class = TopicNestedSerializers
    queryset = Topic.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class NestedUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnlyLec]
    queryset = Topic.objects.all()
    serializer_class = TopicNestedSerializers
