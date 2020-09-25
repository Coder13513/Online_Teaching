from django.urls import path
from .views import RegisterAPIView,LoginWithTokenAuthenticationAPIView,LoginWithTokenAuthenticationAPIViewT,LoginWithTokenAuthenticationAPIViewS

from rest_framework.authtoken.views import obtain_auth_token 

   

urlpatterns=[
 
    path('login/admin/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token'),
    path('register/',RegisterAPIView.as_view(),name='register'),    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/teacher/',LoginWithTokenAuthenticationAPIViewT.as_view(),name='login for teacher'),
    path('login/student/',LoginWithTokenAuthenticationAPIViewS.as_view(),name='login for student')


]
