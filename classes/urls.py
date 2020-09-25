from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from classes import views

urlpatterns = [
    path('class/', views.classesList.as_view()),
    path('class/<int:pk>/', views.classesDetail.as_view()),
]
