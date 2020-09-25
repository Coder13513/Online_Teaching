from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from chapter import views

urlpatterns = [
    path('chapter/', views.chapterList.as_view()),
    path('chapter/<int:pk>/', views.chapterDetail.as_view()),
]
