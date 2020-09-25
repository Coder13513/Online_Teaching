from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from subject import views

urlpatterns = [
    path('subject/', views.subjectList.as_view()),
    path('subject/<int:pk>/', views.subjectDetail.as_view()),
]
