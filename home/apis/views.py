from rest_framework import mixins
from rest_framework import generics

from ..models import UserProfile, Languages
from .serializers import UserProfileSerializer, LanguageSerializer


def perform_query(self):
    queryset = UserProfile.objects.filter(username=self.request.user)
    return queryset


class UserProfileList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    # queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = perform_query(self)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LanguageList(generics.ListAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
