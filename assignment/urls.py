from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from assignment import views

urlpatterns = [
    path('assignment/', views.assignmentList.as_view()),
    path('assignment/<int:pk>/', views.assignmentDetail.as_view()),

    path('quiz/', views.quizList.as_view()),
    path('quiz/<int:pk>/', views.quizDetail.as_view()),

    path('question/', views.questionList.as_view()),
    path('question/<int:pk>/', views.questionDetail.as_view()),

    path('choice/', views.choiceList.as_view()),
    path('choice/<int:pk>/', views.choiceDetail.as_view()),
]
