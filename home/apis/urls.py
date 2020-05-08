from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserProfileList, LanguageList

urlpatterns = [
    path('', UserProfileList.as_view(), name='userprofile-list'),
    path('lang/', LanguageList.as_view(), name='languages'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
