from rest_framework import mixins
from rest_framework import generics
from ELearning.restconf.permission import IsOwnerOrReadOnly
from rest_framework import permissions
from course.models import Course, Category
from ..serializers.course_serializer import CourseSerializers, CourseListSerializers, CategorySerializer


class CategoryList(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseList(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers

    def get_queryset(self):
        queryset = Course.objects.all()
        author = self.request.query_params.get('author')
        category = self.request.query_params.get('category')

        if author:
            queryset = queryset.filter(author=author)
        if category:
            queryset = queryset.filter(category__title__icontains=category)

        return queryset


class CourseCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
