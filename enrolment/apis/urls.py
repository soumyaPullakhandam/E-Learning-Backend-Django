from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EnrolmentList, EnrolmentUpdate

urlpatterns = [
    path('', EnrolmentList.as_view(), name='enrol-list'),
    path('<int:pk>/', EnrolmentUpdate.as_view(), name='enrol-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
