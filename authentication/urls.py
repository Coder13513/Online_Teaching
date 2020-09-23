from django.urls import path
from .views import RegisterAPIView,LoginAPIView,RegisteredBySuperUserAPIView,LoginWithTokenAuthenticationAPIView

from rest_framework.authtoken.views import obtain_auth_token  


urlpatterns=[
    path('login/',LoginAPIView.as_view(),name='login'),
    # path('login/token/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token'),
    path('register/',RegisterAPIView.as_view(),name='register'),
    # path('special/register/',RegisteredBySuperUserAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),



]