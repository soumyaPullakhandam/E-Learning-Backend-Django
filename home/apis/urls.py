from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserProfileList

urlpatterns = [
    path('', UserProfileList.as_view(), name='userprofile-list'),
    # path('<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
