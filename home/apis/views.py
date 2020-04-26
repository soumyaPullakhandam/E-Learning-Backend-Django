from rest_framework import mixins
from rest_framework import generics

from ..models import UserProfile
from .serializers import UserProfileSerializers


### mixins based view -- rest api list ###

class UserProfileList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ### mixins based view -- rest api details ###
# class UserProfileDetail(mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         generics.GenericAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
