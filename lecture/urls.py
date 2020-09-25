from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from lecture import views

urlpatterns = [
    path('lecture/', views.lectureList.as_view()),
    path('lecture/<int:pk>/', views.lectureDetail.as_view()),
]
