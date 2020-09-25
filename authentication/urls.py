from django.urls import path
from .views import RegisterAPIView,LoginWithTokenAuthenticationAPIView

from rest_framework.authtoken.views import obtain_auth_token 

   

urlpatterns=[
 
    path('login/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token'),
    path('register/',RegisterAPIView.as_view(),name='register'),    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/teacher/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token'),
    path('login/student/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token')


]
