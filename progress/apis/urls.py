from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProgressList, ProgressUpdate

urlpatterns = [
    path('', ProgressList.as_view(), name='progress-list'),
    path('<int:pk>/', ProgressUpdate.as_view(), name='progress-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
